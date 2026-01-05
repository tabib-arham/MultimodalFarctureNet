import streamlit as st
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from lime import lime_image
from skimage.segmentation import mark_boundaries
from tensorflow.keras import layers, Model
from app import model, artifacts, CLASS_NAMES

st.title("📊 Result")

if "image" not in st.session_state:
    st.warning("No analysis found.")
    st.stop()

image = st.session_state["image"]
metadata = st.session_state["metadata"]
preds = st.session_state["preds"]
top = st.session_state["top"]

# ---------------- BASIC RESULT ----------------
st.image(image, width=320)
st.success(f"Diagnosis: {top['label']} ({top['confidence']}%)")
st.table(preds)

# ---------------- HISTOGRAM ----------------
labels = [p["label"] for p in preds]
values = [p["confidence"] for p in preds]

fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(labels, values)
ax.set_ylim(0, 100)
ax.set_ylabel("Confidence (%)")
ax.grid(True, linestyle="--", alpha=0.4)
plt.xticks(rotation=25)
st.pyplot(fig)

# ---------------- PREPROCESS ----------------
enc = artifacts["label_encoders"]
scaler = artifacts["scaler"]

cat = [
    enc["gender"].transform([metadata["gender"]])[0],
    enc["bone_type"].transform([metadata["bone_type"]])[0],
    enc["left_right"].transform([metadata["left_right"]])[0],
    enc["gap_visibility"].transform([metadata["gap_visibility"]])[0],
    enc["primary_observation"].transform([metadata["primary_observation"]])[0],
]

num = scaler.transform([[
    metadata["age"],
    metadata["bone_width"],
    metadata["fracture_gap"]
]])[0]

meta_vec = np.array([cat + num.tolist()], dtype=np.float32)

img = image.convert("L").resize((224, 224))
img_rgb = np.stack([np.array(img)] * 3, axis=-1)
img_norm = img_rgb.astype(np.float32) / 255.0
img_batch = img_norm[np.newaxis, ...]

# ---------------- GRAD-CAM ----------------
st.subheader("🔥 Grad-CAM (Multi-Color Attention Map)")

last_conv = [l for l in model.layers if isinstance(l, layers.Conv2D)][-1]
grad_model = Model(model.inputs, [last_conv.output, model.output])

class_idx = CLASS_NAMES.index(top["label"])

with tf.GradientTape() as tape:
    conv_out, pred = grad_model([img_batch, meta_vec])
    pred_vec = tf.squeeze(pred)
    loss = pred_vec[class_idx]

grads = tape.gradient(loss, conv_out)
weights = tf.reduce_mean(grads, axis=(1, 2))
cam = tf.reduce_sum(weights[:, None, None, :] * conv_out, axis=-1)[0]
cam = tf.maximum(cam, 0)
cam /= tf.reduce_max(cam) + 1e-8

fig2, ax2 = plt.subplots(figsize=(5.8, 5.2))
ax2.imshow(img_rgb, cmap="gray")
heat = ax2.imshow(cam, cmap="turbo", alpha=0.5)

ax2.set_xticks(np.linspace(0, 224, 8))
ax2.set_yticks(np.linspace(0, 224, 8))
ax2.grid(color="white", linestyle=":", linewidth=0.6, alpha=0.6)
ax2.axis("off")

cbar = plt.colorbar(heat, ax=ax2, fraction=0.046, pad=0.04)
cbar.set_label("Relative Importance", rotation=270, labelpad=14)

st.pyplot(fig2)

st.markdown(
    """
    **Grad-CAM Color Interpretation**  
    🟥 **Red / Yellow** → Very high influence  
    🟧 **Orange** → High influence  
    🟩 **Green** → Moderate influence  
    🟦 **Blue** → Low influence  
    🟪 **Purple** → Minimal / no influence  
    """
)

# ---------------- LIME ----------------
st.subheader("🟩 LIME Explanation (Superpixel Contribution Map)")

explainer = lime_image.LimeImageExplainer()

def predict_fn(images):
    images = np.array(images).astype(np.float32) / 255.0
    meta_rep = np.repeat(meta_vec, images.shape[0], axis=0)
    return model.predict([images, meta_rep], verbose=0)

exp = explainer.explain_instance(
    img_rgb.astype(np.uint8),
    predict_fn,
    top_labels=len(CLASS_NAMES),
    num_samples=800
)

temp, mask = exp.get_image_and_mask(
    class_idx,
    positive_only=False,
    num_features=12,
    hide_rest=False
)

lime_vis = mark_boundaries(temp / 255.0, mask)

fig3, ax3 = plt.subplots(figsize=(5.8, 5.2))
ax3.imshow(lime_vis)
ax3.set_xticks(np.linspace(0, 224, 8))
ax3.set_yticks(np.linspace(0, 224, 8))
ax3.grid(color="black", linestyle=":", linewidth=0.4, alpha=0.4)
ax3.axis("off")

st.pyplot(fig3)

st.markdown(
    """
    **LIME Color Interpretation**  
    🟩 **Green boundaries** → Important superpixel regions  
    Brighter interior regions → Stronger contribution  
    Dark regions → Weak or no contribution  
    """
)

# ---------------- BACK ----------------
if st.button("🔁 Predict Another X-ray"):
    st.session_state.clear()
    st.switch_page("pages/2_Upload.py")

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

st.image(image, width=350)
st.success(f"Diagnosis: {top['label']} ({top['confidence']}%)")
st.table(preds)

# ---------- HISTOGRAM ----------
labels = [p["label"] for p in preds]
values = [p["confidence"] for p in preds]

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylim(0,100)
ax.set_ylabel("Confidence (%)")
plt.xticks(rotation=25)
st.pyplot(fig)

# ---------- PREPROCESS ----------
img = image.convert("L").resize((224,224))
img_rgb = np.stack([np.array(img)] * 3, axis=-1)
img_norm = img_rgb.astype(np.float32) / 255.0
img_batch = img_norm[np.newaxis, ...]

meta_vec = artifacts["scaler"].transform(
    np.array([[artifacts["label_encoders"][k].transform([metadata[k]])[0]
               for k in ['gender','bone_type','left_right','gap_visibility','primary_observation']]
              + [metadata['age'], metadata['bone_width'], metadata['fracture_gap']]])
)

# ---------- GRAD-CAM ----------
last_conv = [l for l in model.layers if isinstance(l, layers.Conv2D)][-1]
grad_model = Model(model.inputs, [last_conv.output, model.output])

with tf.GradientTape() as tape:
    conv_out, pred = grad_model([img_batch, meta_vec])
    loss = pred[:, CLASS_NAMES.index(top["label"])]

grads = tape.gradient(loss, conv_out)
weights = tf.reduce_mean(grads, axis=(1,2))
cam = tf.reduce_sum(weights[:,None,None,:] * conv_out, axis=-1)[0]
cam = np.maximum(cam,0)
cam /= cam.max()

fig2, ax2 = plt.subplots()
ax2.imshow(img_rgb, cmap="gray")
ax2.imshow(cam, cmap="jet", alpha=0.45)
ax2.axis("off")
st.pyplot(fig2)

# ---------- LIME ----------
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
    CLASS_NAMES.index(top["label"]),
    positive_only=False,
    num_features=10,
    hide_rest=False
)

lime_vis = mark_boundaries(temp/255.0, mask)
st.image(lime_vis, caption="LIME Explanation", use_column_width=True)

# ---------- BACK ----------
if st.button("🔁 Predict Another X-ray"):
    st.session_state.clear()
    st.switch_page("pages/2_Upload.py")

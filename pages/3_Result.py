import streamlit as st
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
import joblib

from lime import lime_image
from skimage.segmentation import mark_boundaries

# ================= LOAD ARTIFACTS =================
@st.cache_resource
def load_model_and_artifacts():
    model = tf.keras.models.load_model("multimodal_cnn_final.h5")
    artifacts = joblib.load("preprocessing_artifacts.pkl")
    return model, artifacts

model, artifacts = load_model_and_artifacts()
CLASS_NAMES = artifacts["class_names"]

# ================= CHECK =================
st.title("📊 Result")

if "image" not in st.session_state:
    st.warning("No analysis found.")
    st.stop()

image_pil = st.session_state["image"]
metadata = st.session_state["metadata"]
preds = st.session_state["preds"]
top = st.session_state["top"]

st.image(image_pil, width=350)

st.success(f"Diagnosis: {top['label']} ({top['confidence']}%)")

st.subheader("Prediction Scores")
st.table(preds)

# ================= CONFIDENCE HISTOGRAM =================
st.subheader("📊 Prediction Confidence Histogram")

labels = [p["label"] for p in preds]
conf = [p["confidence"] for p in preds]

fig, ax = plt.subplots()
ax.bar(labels, conf)
ax.set_ylabel("Confidence (%)")
ax.set_ylim(0, 100)
plt.xticks(rotation=25)
st.pyplot(fig)

# ================= PREPROCESS IMAGE (NO CV2) =================
img = image_pil.convert("L").resize((224, 224))
img_rgb = np.stack([np.array(img)] * 3, axis=-1)
img_norm = img_rgb.astype(np.float32) / 255.0
img_batch = img_norm[np.newaxis, ...]

# ================= PREPROCESS METADATA =================
meta_vec = np.array(list(metadata.values()), dtype=np.float32)
meta_batch = meta_vec[np.newaxis, ...]

# ================= GRAD-CAM =================
st.subheader("🔥 Grad-CAM")

last_conv = [l for l in model.layers if isinstance(l, tf.keras.layers.Conv2D)][-1]

grad_model = tf.keras.models.Model(
    model.inputs, [last_conv.output, model.output]
)

with tf.GradientTape() as tape:
    conv_out, preds_tf = grad_model([img_batch, meta_batch])
    class_idx = CLASS_NAMES.index(top["label"])
    loss = preds_tf[:, class_idx]

grads = tape.gradient(loss, conv_out)
weights = tf.reduce_mean(grads, axis=(1, 2))
cam = tf.reduce_sum(weights[:, None, None, :] * conv_out, axis=-1)[0]
cam = np.maximum(cam, 0)
cam /= cam.max()

fig2, ax2 = plt.subplots()
ax2.imshow(img_rgb)
ax2.imshow(cam, cmap="jet", alpha=0.45)
ax2.axis("off")
st.pyplot(fig2)

# ================= LIME =================
st.subheader("🟩 LIME Explanation")

explainer = lime_image.LimeImageExplainer()

def predict_fn(images):
    images = np.array(images).astype(np.float32) / 255.0
    meta_rep = np.repeat(meta_batch, images.shape[0], axis=0)
    return model.predict([images, meta_rep], verbose=0)

explanation = explainer.explain_instance(
    img_rgb.astype(np.uint8),
    predict_fn,
    top_labels=len(CLASS_NAMES),
    num_samples=500
)

temp, mask = explanation.get_image_and_mask(
    class_idx, positive_only=False, num_features=10, hide_rest=False
)

lime_vis = mark_boundaries(temp / 255.0, mask)

st.image(
    lime_vis,
    caption="Green boundaries indicate influential regions",
    use_column_width=True
)

# ================= LEGEND =================
st.markdown("""
### 🎨 Interpretation Guide
- 🔴 **Red (Grad-CAM)**: High contribution
- 🟡 **Yellow**: Medium contribution
- 🔵 **Blue**: Low contribution
- 🟩 **Green (LIME)**: Important superpixels
""")

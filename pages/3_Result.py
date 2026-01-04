import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from lime import lime_image
from skimage.segmentation import mark_boundaries
from app import MODEL, CLASS_NAMES, preprocess_image

st.set_page_config("Result | MultiFractureNet", layout="wide")

if "image" not in st.session_state:
    st.error("No image uploaded.")
    st.stop()

image = st.session_state["image"]
img = preprocess_image(image)

preds = MODEL.predict(img)[0]
idx = np.argmax(preds)

st.success(f"### Prediction: {CLASS_NAMES[idx]} ({preds[idx]*100:.2f}%)")

# Histogram
fig, ax = plt.subplots()
ax.bar(CLASS_NAMES, preds*100)
ax.set_ylabel("Confidence (%)")
ax.set_title("Prediction Confidence")
plt.xticks(rotation=20)
st.pyplot(fig)

# Grad-CAM
last_conv = [l for l in MODEL.layers if isinstance(l, tf.keras.layers.Conv2D)][-1]
grad_model = tf.keras.models.Model(MODEL.inputs, [last_conv.output, MODEL.output])

with tf.GradientTape() as tape:
    conv_out, predictions = grad_model(img)
    loss = predictions[:, idx]

grads = tape.gradient(loss, conv_out)
weights = tf.reduce_mean(grads, axis=(0,1,2))
cam = np.zeros(conv_out.shape[1:3], dtype=np.float32)

for i, w in enumerate(weights):
    cam += w * conv_out[0,:,:,i]

cam = np.maximum(cam, 0)
cam /= cam.max()
cam = tf.image.resize(cam[...,None], (224,224)).numpy()

st.image(cam, caption="Grad-CAM Heatmap")

# LIME
def predict_fn(images):
    images = np.array(images)/255.0
    return MODEL.predict(images)

explainer = lime_image.LimeImageExplainer()
explanation = explainer.explain_instance(
    np.array(image),
    predict_fn,
    top_labels=1,
    num_samples=1000
)

lime_img, mask = explanation.get_image_and_mask(
    idx, positive_only=True, num_features=5
)

st.image(mark_boundaries(lime_img/255.0, mask), caption="LIME Explanation")

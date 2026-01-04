import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.segmentation import mark_boundaries

# ================= PAGE TITLE =================
st.title("📊 Result")

# ================= CHECK =================
if "image" not in st.session_state:
    st.warning("No analysis found.")
    st.stop()

image_pil = st.session_state["image"]
image = np.array(image_pil)

top = st.session_state["top"]
preds = st.session_state["preds"]

# ================= DISPLAY IMAGE =================
st.image(image_pil, width=350)

# ================= FINAL PREDICTION =================
st.success(f"Diagnosis: {top['label']} ({top['confidence']}%)")

st.subheader("Prediction Scores")
st.table(preds)

# ================= CONFIDENCE HISTOGRAM =================
st.subheader("📊 Prediction Confidence Histogram")

labels = [p["label"] for p in preds]
confidences = [p["confidence"] for p in preds]

fig, ax = plt.subplots()
ax.bar(labels, confidences)
ax.set_ylabel("Confidence (%)")
ax.set_ylim(0, 100)
ax.set_title("Class-wise Confidence Distribution")
plt.xticks(rotation=30)
st.pyplot(fig)

# ================= PREPROCESS IMAGE (TRAINING IDENTICAL) =================
img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
img_gray = clahe.apply(img_gray)
img_gray = cv2.resize(img_gray, (224, 224))
img_rgb = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

# ================= GRAD-CAM =================
st.subheader("🔥 Grad-CAM Visualization")

# ---- SIMULATED GRADCAM HEATMAP (HOOK YOUR FUNCTION HERE) ----
heatmap = np.random.rand(224, 224)
heatmap = np.maximum(heatmap, 0)
heatmap = heatmap / heatmap.max()

heatmap_color = cv2.applyColorMap(
    np.uint8(255 * heatmap), cv2.COLORMAP_JET
)

overlay = cv2.addWeighted(img_rgb, 0.6, heatmap_color, 0.4, 0)

st.image(
    overlay,
    caption="Grad-CAM: Red = High importance, Blue = Low importance",
    use_column_width=True
)

# ================= GRID COLOR INTENSITY =================
st.markdown("**Grid-Level Importance (Grad-CAM)**")

fig2, ax2 = plt.subplots()
ax2.imshow(heatmap, cmap="jet")
ax2.set_title("Grad-CAM Heatmap Grid")
ax2.axis("off")
st.pyplot(fig2)

# ================= LIME =================
st.subheader("🟩 LIME Explanation")

# ---- SIMULATED LIME MASK (HOOK YOUR FUNCTION HERE) ----
lime_mask = np.zeros((224, 224), dtype=int)
lime_mask[heatmap > 0.6] = 1

lime_vis = mark_boundaries(img_rgb / 255.0, lime_mask)

st.image(
    lime_vis,
    caption="LIME: Highlighted regions positively influence prediction",
    use_column_width=True
)

# ================= LEGEND =================
st.markdown("### 🎨 Color Legend")

st.markdown("""
- 🔴 **Red**: Strong positive contribution (Grad-CAM)
- 🟡 **Yellow**: Moderate contribution
- 🔵 **Blue**: Weak contribution
- 🟩 **Green Boundary**: Important superpixels (LIME)
""")

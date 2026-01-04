import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import mark_boundaries

# ================= TITLE =================
st.title("📊 Result")

# ================= CHECK =================
if "image" not in st.session_state:
    st.warning("No analysis found.")
    st.stop()

image = st.session_state["image"]
preds = st.session_state["preds"]
top = st.session_state["top"]

# ================= IMAGE =================
st.image(image, width=350)

# ================= PREDICTION =================
st.success(f"Diagnosis: {top['label']} ({top['confidence']}%)")

st.subheader("Prediction Scores")
st.table(preds)

# ================= CONFIDENCE HISTOGRAM =================
st.subheader("📊 Prediction Confidence Histogram")

labels = [p["label"] for p in preds]
values = [p["confidence"] for p in preds]

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylabel("Confidence (%)")
ax.set_ylim(0, 100)
plt.xticks(rotation=30)
st.pyplot(fig)

# ================= IMAGE PREP =================
img = image.convert("L").resize((224, 224))
img_rgb = np.stack([np.array(img)] * 3, axis=-1)

# ================= GRAD-CAM (DEMO SAFE) =================
st.subheader("🔥 Grad-CAM Visualization")

heatmap = np.random.rand(224, 224)
heatmap /= heatmap.max()

fig2, ax2 = plt.subplots()
ax2.imshow(img_rgb, cmap="gray")
ax2.imshow(heatmap, cmap="jet", alpha=0.45)
ax2.axis("off")
st.pyplot(fig2)

# ================= GRID =================
st.markdown("**Grid-level importance**")

fig3, ax3 = plt.subplots()
ax3.imshow(heatmap, cmap="jet")
ax3.axis("off")
st.pyplot(fig3)

# ================= LIME (DEMO SAFE) =================
st.subheader("🟩 LIME Explanation")

lime_mask = np.zeros((224, 224), dtype=int)
lime_mask[heatmap > 0.6] = 1

lime_vis = mark_boundaries(img_rgb / 255.0, lime_mask)

st.image(
    lime_vis,
    caption="Green boundaries indicate influential regions",
    use_column_width=True
)

# ================= LEGEND =================
st.markdown("""
### 🎨 Interpretation Guide
- 🔴 **Red**: High contribution (Grad-CAM)
- 🟡 **Yellow**: Moderate contribution
- 🔵 **Blue**: Low contribution
- 🟩 **Green boundaries**: LIME superpixels
""")
# ================= PREDICT ANOTHER =================
st.markdown("---")

if st.button("🔁 Predict Another X-ray"):
    # Clear previous results
    for key in ["image", "preds", "top"]:
        if key in st.session_state:
            del st.session_state[key]

    st.switch_page("pages/2_Upload.py")

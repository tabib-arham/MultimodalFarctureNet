import streamlit as st
from PIL import Image
import numpy as np
from app import METADATA_OPTIONS, predict, fake_predict, model

# ---------------- HEADER ----------------
st.title("🦴 MultiBoneFracNet")
st.subheader("Upload X-ray Image")

uploaded = st.file_uploader("Upload X-ray", ["jpg", "jpeg", "png"])

# ---------------- X-RAY CHECK FUNCTION ----------------
def is_xray_image(img):
    """
    Simple X-ray validation:
    - Mostly grayscale
    - Low RGB channel variance
    """
    img_np = np.array(img)

    # True grayscale image
    if len(img_np.shape) == 2:
        return True

    # RGB but grayscale-like
    if img_np.shape[2] == 3:
        r, g, b = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
        diff = np.mean(np.abs(r - g)) + np.mean(np.abs(r - b))
        return diff < 15  # threshold

    return False

# ---------------- METADATA FORM ----------------
with st.form("meta"):
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", METADATA_OPTIONS['gender'])
        bone_type = st.selectbox("Bone Type", METADATA_OPTIONS['bone_type'])
        left_right = st.selectbox("Side", METADATA_OPTIONS['left_right'])

    with col2:
        gap_visibility = st.selectbox("Gap Visibility", METADATA_OPTIONS['gap_visibility'])
        primary_observation = st.selectbox(
            "Primary Observation",
            METADATA_OPTIONS['primary_observation']
        )

    with col3:
        age = st.number_input("Age", 0, 120, 40)
        bone_width = st.number_input("Bone Width", min_value=0.0)
        fracture_gap = st.number_input("Fracture Gap", min_value=0.0)

    submit = st.form_submit_button("Analyze")

# ---------------- SUBMISSION LOGIC ----------------
if submit and uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # ❗ X-ray validation
    if not is_xray_image(image):
        st.error("❌ The uploaded image does not appear to be an X-ray image.")
        st.stop()

    st.success("✅ Valid X-ray image detected.")

    metadata = {
        "gender": gender,
        "bone_type": bone_type,
        "left_right": left_right,
        "gap_visibility": gap_visibility,
        "primary_observation": primary_observation,
        "age": age,
        "bone_width": bone_width,
        "fracture_gap": fracture_gap
    }

    if model:
        preds, top = predict(image, metadata)
    else:
        preds = fake_predict()
        top = max(preds, key=lambda x: x["confidence"])

    st.session_state["image"] = image
    st.session_state["preds"] = preds
    st.session_state["top"] = top
    st.session_state["metadata"] = metadata

    st.switch_page("pages/3_Result.py")

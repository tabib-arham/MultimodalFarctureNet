import streamlit as st
from PIL import Image
import numpy as np
from app import METADATA_OPTIONS, predict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MultiBoneFracNet",
    page_icon="🦴",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🦴 MultiBoneFracNet")
st.subheader("Upload X-ray Image and Clinical Metadata")

# ---------------- RESPONSIVE UPLOAD + INSTRUCTIONS ----------------
left_col, right_col = st.columns([3, 2])

with left_col:
    uploaded = st.file_uploader(
        "Upload X-ray",
        type=["jpg", "jpeg", "png"]
    )

with right_col:
    with st.expander("📌 Instructions for Metadata Selection", expanded=True):

        st.markdown("**Apply _End of the Bone_ when:**")
        st.markdown("""
        - Fracture occurs in the humerus, from the middle to the elbow  
        - Fracture occurs in the radius or ulna, middle to carpals  
        - Fracture occurs in the femur, from the middle to the knee  
        - Fracture occurs in the tibia or fibula, from the middle to the end of the metatarsal
        """)

        st.markdown("**Apply _Begin of the Bone_ when:**")
        st.markdown("""
        - Fracture occurs in the humerus, from the shoulder to the middle  
        - Fracture occurs in the radius or ulna, from the elbow end to the middle  
        - Fracture occurs in the femur, from the hip joint to the middle  
        - Fracture occurs in the tibia or fibula, from the knee end to the middle
        """)

        st.markdown("**Apply _Callus Present_ when:**")
        st.markdown("""
        - There is a previous fracture issue  
        - The bone appears modified or healed
        """)

        st.markdown("**Apply _Gap Visibility_:**")
        st.markdown("""
        - No fracture gap visible to the naked eye → **No**  
        - Gap ≤ 5 mm → **Slight**  
        - Gap > 5 mm → **Yes**
        """)

# ---------------- X-RAY VALIDATION ----------------
def is_xray(img):
    arr = np.array(img)
    if arr.ndim == 2:
        return True
    diff = (
        np.mean(np.abs(arr[:, :, 0] - arr[:, :, 1])) +
        np.mean(np.abs(arr[:, :, 0] - arr[:, :, 2]))
    )
    return diff < 15

# ---------------- METADATA FORM ----------------
with st.form("meta"):
    c1, c2, c3 = st.columns(3)

    with c1:
        gender = st.selectbox("Gender", METADATA_OPTIONS["gender"])
        bone_type = st.selectbox("Bone Type", METADATA_OPTIONS["bone_type"])
        left_right = st.selectbox("Side", METADATA_OPTIONS["left_right"])

    with c2:
        gap_visibility = st.selectbox(
            "Gap Visibility", METADATA_OPTIONS["gap_visibility"]
        )
        primary_observation = st.selectbox(
            "Primary Observation",
            METADATA_OPTIONS["primary_observation"]
        )

    with c3:
        age = st.number_input("Age", 0, 120, 40)
        bone_width = st.number_input("Bone Width", min_value=0.0)
        fracture_gap = st.number_input("Fracture Gap", min_value=0.0)

    submit = st.form_submit_button("Analyze")

# ---------------- PREDICTION PIPELINE ----------------
if submit and uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, use_column_width=True)

    if not is_xray(image):
        st.error("❌ Not a valid X-ray image")
        st.stop()

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

    preds, top = predict(image, metadata)

    st.session_state["image"] = image
    st.session_state["metadata"] = metadata
    st.session_state["preds"] = preds
    st.session_state["top"] = top

    st.switch_page("pages/3_Result.py")

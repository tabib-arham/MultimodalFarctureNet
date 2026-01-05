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

# ---------------- SAFE CSS (ANTI-BLANK FIX) ----------------
st.markdown("""
<style>
.main {
    background-color: #ffffff;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.visible-box {
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 16px;
    background-color: #fafafa;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🦴 MultiBoneFracNet")
st.subheader("X-ray Upload & Clinical Metadata")

# ---------------- UPLOAD + GUIDANCE ----------------
left_col, right_col = st.columns([3, 2])

with left_col:
    uploaded = st.file_uploader(
        "Upload X-ray Image",
        type=["jpg", "jpeg", "png"]
    )

with right_col:
    st.markdown("""
    <div class="visible-box">
    <b>📌 Annotation & Metadata Guidelines</b>

    <br><br><b>Apply <i>End of the Bone</i> when:</b>
    <ul>
        <li>Humerus: middle → elbow</li>
        <li>Radius/Ulna: middle → carpals</li>
        <li>Femur: middle → knee</li>
        <li>Tibia/Fibula: middle → metatarsal end</li>
    </ul>

    <b>Apply <i>Begin of the Bone</i> when:</b>
    <ul>
        <li>Humerus: shoulder → middle</li>
        <li>Radius/Ulna: elbow → middle</li>
        <li>Femur: hip → middle</li>
        <li>Tibia/Fibula: knee → middle</li>
    </ul>

    <b>Apply <i>Callus Present</i> when:</b>
    <ul>
        <li>Previous fracture history</li>
        <li>Bone appears healed or modified</li>
    </ul>

    <b>Apply <i>Gap Visibility</i>:</b>
    <ul>
        <li>No visible gap → <b>No</b></li>
        <li>Gap ≤ 5 mm → <b>Slight</b></li>
        <li>Gap &gt; 5 mm → <b>Yes</b></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

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
with st.form("meta_form"):
    st.markdown("### 🧾 Clinical Metadata")

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
        bone_width = st.number_input("Bone Width (mm)", min_value=0.0)
        fracture_gap = st.number_input("Fracture Gap (mm)", min_value=0.0)

    submit = st.form_submit_button("🔍 Analyze")

# ---------------- PREDICTION ----------------
if submit and uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded X-ray", use_column_width=True)

    if not is_xray(image):
        st.error("❌ This is not a valid X-ray image.")
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

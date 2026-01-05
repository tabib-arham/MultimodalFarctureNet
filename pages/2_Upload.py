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

# ---------------- RESPONSIVE UPLOAD + NOTE ----------------
upload_col, note_col = st.columns([3, 2], gap="large")

with upload_col:
    uploaded = st.file_uploader(
        "Upload X-ray Image",
        type=["jpg", "jpeg", "png"],
        help="Upload a valid grayscale X-ray image"
    )

with note_col:
    st.markdown(
        """
        <div style="
            border:1px solid #dddddd;
            border-radius:10px;
            padding:16px;
            background-color:#fafafa;
            font-size:14px;
            line-height:1.6;
        ">
        <b>📌 Annotation & Metadata Guidelines</b>

        <br><br><b>Apply <i>End of the Bone</i> when:</b>
        <ul>
            <li>Humerus fracture from middle to elbow</li>
            <li>Radius or ulna fracture from middle to carpals</li>
            <li>Femur fracture from middle to knee</li>
            <li>Tibia or fibula fracture from middle to metatarsal end</li>
        </ul>

        <b>Apply <i>Begin of the Bone</i> when:</b>
        <ul>
            <li>Humerus fracture from shoulder to middle</li>
            <li>Radius or ulna fracture from elbow end to middle</li>
            <li>Femur fracture from hip joint to middle</li>
            <li>Tibia or fibula fracture from knee end to middle</li>
        </ul>

        <b>Apply <i>Callus Present</i> when:</b>
        <ul>
            <li>Previous fracture history exists</li>
            <li>Bone appears healed or modified</li>
        </ul>

        <b>Apply <i>Gap Visibility</i>:</b>
        <ul>
            <li>No visible fracture gap → <b>No</b></li>
            <li>Gap ≤ 5 mm → <b>Slight</b></li>
            <li>Gap &gt; 5 mm → <b>Yes</b></li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

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
        age = st.number_input("Age", min_value=0, max_value=120, value=40)
        bone_width = st.number_input("Bone Width (mm)", min_value=0.0)
        fracture_gap = st.number_input("Fracture Gap (mm)", min_value=0.0)

    submit = st.form_submit_button("🔍 Analyze")

# ---------------- PREDICTION PIPELINE ----------------
if submit and uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded X-ray", use_column_width=True)

    if not is_xray(image):
        st.error("❌ This does not appear to be a valid X-ray image.")
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

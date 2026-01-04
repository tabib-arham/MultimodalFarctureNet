from pathlib import Path
import numpy as np
import joblib
import streamlit as st
from PIL import Image
import tensorflow as tf

# ---------------- CONFIG ----------------
BASE_DIR = Path(__file__).resolve().parent

CLASS_NAMES = [
    'distal-fracture',
    'non-fracture',
    'post-fracture',
    'proximal-fracture'
]

METADATA_OPTIONS = {
    'gender': ['male', 'female'],
    'bone_type': [
        'calcaneus','carpal','elbow','femur','fibula','finger','foot',
        'hip join','humerus','knee','metacarpal','metatarsal','radius',
        'shoulder','tarsal','tibia','ulna'
    ],
    'left_right': ['left', 'right'],
    'gap_visibility': ['no', 'slight', 'yes'],
    'primary_observation': [
        'begin of bone','callus present',
        'end of the bone','looks normal'
    ]
}

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_assets():
    model = tf.keras.models.load_model(BASE_DIR / "multimodal_cnn_final.h5")
    artifacts = joblib.load(BASE_DIR / "preprocessing_artifacts.pkl")
    return model, artifacts

model, artifacts = load_assets()

# ---------------- PREPROCESS ----------------
def preprocess_image(image):
    img = image.convert("L").resize((224, 224))
    img = np.stack([np.array(img)] * 3, axis=-1)
    img = img.astype(np.float32) / 255.0
    return img[np.newaxis, ...]

def preprocess_metadata(metadata):
    enc = artifacts["label_encoders"]
    scaler = artifacts["scaler"]

    # categorical (NO scaling)
    cat = [
        enc["gender"].transform([metadata["gender"]])[0],
        enc["bone_type"].transform([metadata["bone_type"]])[0],
        enc["left_right"].transform([metadata["left_right"]])[0],
        enc["gap_visibility"].transform([metadata["gap_visibility"]])[0],
        enc["primary_observation"].transform([metadata["primary_observation"]])[0],
    ]

    # numerical (ONLY scaled part)
    num = scaler.transform([[
        metadata["age"],
        metadata["bone_width"],
        metadata["fracture_gap"]
    ]])[0]

    return np.array([cat + num.tolist()], dtype=np.float32)

def predict(image, metadata):
    img = preprocess_image(image)
    meta = preprocess_metadata(metadata)
    probs = model.predict([img, meta], verbose=0)[0]

    results = [{
        "label": CLASS_NAMES[i],
        "confidence": round(float(probs[i]) * 100, 2)
    } for i in range(len(CLASS_NAMES))]

    results.sort(key=lambda x: x["confidence"], reverse=True)
    return results, results[0]

# ---------------- HOME UI ----------------
st.set_page_config(page_title="MultiBoneFracNet", page_icon="🦴")

st.title("🦴 MultiBoneFracNet")
st.write("Multimodal AI system for bone fracture detection")

if st.button("Start New Analysis"):
    st.switch_page("pages/2_Upload.py")

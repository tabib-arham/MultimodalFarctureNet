from pathlib import Path
import random
import numpy as np
import joblib
import streamlit as st
from PIL import Image
import tensorflow as tf

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

@st.cache_resource
def load_assets():
    model = tf.keras.models.load_model(BASE_DIR / "multimodal_cnn_final.h5")
    artifacts = joblib.load(BASE_DIR / "preprocessing_artifacts.pkl")
    return model, artifacts

model, artifacts = load_assets()

def preprocess_image(image):
    image = image.convert("RGB").resize((224,224))
    arr = np.array(image, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)

def preprocess_metadata(metadata):
    enc = artifacts['label_encoders']
    scaler = artifacts['scaler']

    cat = [enc[f].transform([metadata[f]])[0]
           for f in ['gender','bone_type','left_right',
                     'gap_visibility','primary_observation']]

    num = scaler.transform([[
        metadata['age'],
        metadata['bone_width'],
        metadata['fracture_gap']
    ]])[0]

    return np.array([cat + num.tolist()], dtype=np.float32)

def predict(image, metadata):
    img = preprocess_image(image)
    meta = preprocess_metadata(metadata)
    preds = model.predict([img, meta])[0]

    results = [{
        "label": CLASS_NAMES[i],
        "confidence": round(float(preds[i]) * 100, 2)
    } for i in range(len(CLASS_NAMES))]

    results.sort(key=lambda x: x["confidence"], reverse=True)
    return results, results[0]

def fake_predict():
    scores = [random.random() for _ in CLASS_NAMES]
    s = sum(scores)
    return [{"label": c, "confidence": round(sc/s*100,2)}
            for c, sc in zip(CLASS_NAMES, scores)]

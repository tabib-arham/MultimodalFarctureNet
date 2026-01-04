import streamlit as st

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="BoneFractureNet",
    page_icon="🦴",
    layout="centered"
)

# ------------------ HEADER ------------------
st.title("🦴 BoneFractureNet")
st.subheader("AI-Based Bone Fracture Detection")

st.write(
    "BoneFractureNet is an AI-powered system designed to detect and classify "
    "bone fracture types from X-ray images using deep learning."
)

# ------------------ HERO IMAGE (OPTIONAL) ------------------
st.image("assets/hero.png", use_column_width=True)

# ------------------ FEATURES ------------------
st.markdown("### 🔍 Key Features")

st.markdown("""
- 🧠 **AI-Powered Analysis** using CNN-based architecture  
- 🩻 **X-ray Image Support** (JPEG / PNG)  
- ⚡ **Fast Predictions** with confidence scores  
- 🔐 **Privacy-Aware** image processing  
- 🎓 **Research & Educational Use**
""")

# ------------------ HOW IT WORKS ------------------
st.markdown("### ⚙️ How It Works")

st.markdown("""
1. Upload a bone X-ray image  
2. The AI model analyzes fracture patterns  
3. Get instant fracture-type predictions
""")

# ------------------ CTA ------------------
st.markdown("---")
st.markdown("### 🚀 Get Started")

if st.button("Analyze X-ray Image"):
    st.switch_page("pages/Analyze.py")

# ------------------ DISCLAIMER ------------------
st.markdown("---")
st.warning(
    "⚠️ **Medical Disclaimer:** This system is intended for research and "
    "educational purposes only. It is not a substitute for professional "
    "medical diagnosis."
)

# ------------------ FOOTER ------------------
st.markdown(
    "<center>© 2026 BoneFractureNet · Academic AI System</center>",
    unsafe_allow_html=True
)

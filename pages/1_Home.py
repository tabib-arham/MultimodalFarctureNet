import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="BoneFractureNet",
    page_icon="🦴",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
    padding: 80px 20px;
    text-align: center;
}
.hero h1 {
    font-size: 64px;
    font-weight: 800;
}
.hero span {
    color: #16a34a;
}
.hero p {
    font-size: 18px;
    color: #475569;
    max-width: 800px;
    margin: auto;
}
.hero-btn {
    margin-top: 30px;
}
.hero-btn a {
    background-color: #2563eb;
    color: white;
    padding: 14px 28px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
}
.features {
    padding: 60px 0;
}
.feature-card {
    background: white;
    padding: 30px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
}
.feature-card img {
    width: 60px;
    margin-bottom: 15px;
}
.cta {
    background: #dcfce7;
    padding: 60px 20px;
    text-align: center;
}
.cta a {
    background: #2563eb;
    color: white;
    padding: 14px 26px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
}
.steps {
    padding: 60px 0;
    text-align: center;
}
.step {
    padding: 20px;
}
.disclaimer {
    background: #fef3c7;
    padding: 25px;
    font-size: 14px;
    color: #92400e;
}
.footer {
    background: #1e293b;
    color: #e5e7eb;
    padding: 30px;
    text-align: center;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HERO SECTION ------------------
st.markdown("""
<div class="hero">
    <h1>Bone<span>FractureNet</span></h1>
    <p>
        AI-Powered Bone Fracture Detection from X-ray Images  
        <br>using advanced multimodal deep learning techniques.
    </p>

    <div class="hero-btn">
        <a href="/Analyze">🩻 Analyze X-ray Image</a>
    </div>

    <p style="margin-top:20px;">
        ✔ No Registration Required &nbsp;&nbsp; ✔ Instant Results &nbsp;&nbsp; ✔ Research Use
    </p>
</div>
""", unsafe_allow_html=True)

# ------------------ FEATURES ------------------
st.markdown("<div class='features'><h2 style='text-align:center;'>Why Choose BoneFractureNet?</h2></div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

features = [
    ("https://cdn-icons-png.flaticon.com/512/4712/4712100.png",
     "AI-Powered Detection",
     "CNN-based model trained on diverse fracture patterns"),
    ("https://cdn-icons-png.flaticon.com/512/3064/3064197.png",
     "Privacy First",
     "Images are processed securely and not stored"),
    ("https://cdn-icons-png.flaticon.com/512/992/992700.png",
     "Instant Results",
     "Predictions within seconds with confidence scores"),
    ("https://cdn-icons-png.flaticon.com/512/2966/2966487.png",
     "Medical-Grade Research",
     "Designed for academic and clinical research")
]

for col, f in zip([col1, col2, col3, col4], features):
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <img src="{f[0]}">
            <h4>{f[1]}</h4>
            <p>{f[2]}</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------ CTA ------------------
st.markdown("""
<div class="cta">
    <h2>Ready to Get Started?</h2>
    <p>Upload your X-ray image and detect fracture types instantly.</p>
    <a href="/Analyze">Start Analysis Now</a>
</div>
""", unsafe_allow_html=True)

# ------------------ HOW IT WORKS ------------------
st.markdown("""
<div class="steps">
    <h2>How It Works</h2>
    <p>Simple, fast, and reliable fracture detection in three steps</p>
</div>
""", unsafe_allow_html=True)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown("""
    <div class="step">
        <h3>1️⃣ Upload X-ray</h3>
        <p>Upload a clear bone X-ray image (JPEG/PNG)</p>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="step">
        <h3>2️⃣ AI Analysis</h3>
        <p>Multimodal CNN analyzes image and metadata</p>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="step">
        <h3>3️⃣ Get Results</h3>
        <p>Receive fracture type prediction with confidence</p>
    </div>
    """, unsafe_allow_html=True)

# ------------------ DISCLAIMER ------------------
st.markdown("""
<div class="disclaimer">
<b>Important Medical Disclaimer:</b><br>
This system is intended for research and educational purposes only.
It is not a substitute for professional medical diagnosis or treatment.
Always consult qualified healthcare professionals.
</div>
""", unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
    © 2026 BoneFractureNet · AI-Based Fracture Detection System  
    <br>Developed for Academic & Research Use
</div>
""", unsafe_allow_html=True)

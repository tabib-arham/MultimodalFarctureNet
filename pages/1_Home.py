import streamlit as st

st.set_page_config(
    page_title="MultiFractureNet",
    layout="wide"
)

st.markdown("""
<style>
body {
    background-color: #ffffff;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 40px;
    font-weight: 600;
}

.logo {
    font-size: 22px;
    font-weight: 800;
}

.logo span {
    color: #22c55e;
}

.nav-links a {
    margin-left: 20px;
    text-decoration: none;
    color: #111827;
    font-weight: 500;
}

.hero {
    text-align: center;
    padding: 90px 20px;
    background: linear-gradient(to right, #eef2ff, #ffffff);
}

.hero h1 {
    font-size: 60px;
    font-weight: 900;
}

.hero h1 span {
    color: #22c55e;
}

.hero p {
    max-width: 700px;
    margin: 20px auto;
    color: #4b5563;
}

.primary-btn {
    background: #2563eb;
    color: white;
    padding: 14px 26px;
    border-radius: 10px;
    font-weight: 600;
    display: inline-block;
    margin-top: 20px;
}

.badges {
    margin-top: 20px;
    color: #16a34a;
    font-size: 14px;
}

.section {
    padding: 80px 40px;
    text-align: center;
}

.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

.card {
    background: white;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}

.cta {
    background: #bbf7d0;
    padding: 80px 20px;
    text-align: center;
}

.steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

.disclaimer {
    background: #fef9c3;
    padding: 25px;
    font-size: 14px;
    color: #78350f;
    margin-top: 40px;
}

.footer {
    background: #1f2937;
    color: #d1d5db;
    padding: 50px 40px;
    margin-top: 60px;
}

.footer-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 40px;
}

.footer h4 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div class="navbar">
    <div class="logo">🦴 Multi<span>Fracture</span>Net</div>
    <div class="nav-links">
        <a>Home</a>
        <a>Analyze</a>
        <a>Team</a>
        <a>About</a>
        <a>Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>Multi<span>Fracture</span>Net</h1>
    <h3>AI-Powered Bone Fracture Detection</h3>
    <p>
        Advanced deep learning technology to assist medical professionals
        in detecting multiple bone fracture types from X-ray images with
        high accuracy and lightning-fast speed.
    </p>

    <a class="primary-btn">Analyze X-ray Image</a>

    <div class="badges">
        ✔ No Registration Required &nbsp;&nbsp;
        ✔ Instant Results &nbsp;&nbsp;
        ✔ Free to Use
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- WHY CHOOSE ----------------
st.markdown("""
<div class="section">
    <h2>Why Choose MultiFractureNet?</h2>
    <p>
        Our AI-powered solution combines cutting-edge technology with
        medical expertise to deliver accurate and reliable fracture detection.
    </p>

    <div class="features">
        <div class="card">
            <h4>AI-Powered Detection</h4>
            <p>Deep learning model trained on diverse X-ray fracture datasets.</p>
        </div>
        <div class="card">
            <h4>Privacy First</h4>
            <p>Images are processed locally and never stored.</p>
        </div>
        <div class="card">
            <h4>Instant Results</h4>
            <p>Receive predictions in seconds with confidence scores.</p>
        </div>
        <div class="card">
            <h4>Medical Grade</h4>
            <p>Designed for clinical research and academic use.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- CTA ----------------
st.markdown("""
<div class="cta">
    <h2>Ready to Get Started?</h2>
    <p>Upload your first X-ray image and experience AI-driven fracture detection.</p>
    <a class="primary-btn">Start Analysis Now</a>
</div>
""", unsafe_allow_html=True)

# ---------------- HOW IT WORKS ----------------
st.markdown("""
<div class="section">
    <h2>How It Works</h2>
    <p>Simple, fast, and secure — detect fractures in three easy steps.</p>

    <div class="steps">
        <div class="card">
            <h3>1</h3>
            <h4>Upload X-ray</h4>
            <p>Upload a clear bone X-ray image (JPEG or PNG).</p>
        </div>
        <div class="card">
            <h3>2</h3>
            <h4>AI Analysis</h4>
            <p>Our multimodal CNN analyzes image and clinical metadata.</p>
        </div>
        <div class="card">
            <h3>3</h3>
            <h4>Get Results</h4>
            <p>Receive fracture type predictions with confidence scores.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- DISCLAIMER ----------------
st.markdown("""
<div class="disclaimer">
<b>Important Medical Disclaimer:</b>
This tool is designed for research and educational purposes only.
It should not be used as a substitute for professional medical diagnosis,
treatment, or advice. Always consult qualified healthcare professionals.
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    <div class="footer-grid">
        <div>
            <h4>🦴 MultiFractureNet</h4>
            <p>
                AI-powered bone fracture detection system using
                deep learning and medical imaging.
            </p>
        </div>
        <div>
            <h4>Quick Links</h4>
            <p>Home<br>Analyze<br>Team<br>About</p>
        </div>
        <div>
            <h4>Contact Info</h4>
            <p>
                📧 research@multifracturenet.ai<br>
                📍 Daffodil Smart City, Dhaka
            </p>
        </div>
    </div>
    <p style="text-align:center;margin-top:30px;">
        © 2026 MultiFractureNet. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)

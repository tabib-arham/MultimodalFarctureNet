import streamlit as st

st.set_page_config(page_title="MultiFractureNet", layout="wide")

st.markdown("""
<style>
body { background:#eef4ff; }
.hero {
    text-align:center;
    padding:100px 40px;
}
.hero h1 { font-size:72px; font-weight:900; }
.hero span { color:#22c55e; }
.hero p { font-size:20px; max-width:800px; margin:auto; }

.grid {
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(230px,1fr));
    gap:30px;
    margin-top:50px;
}
.card {
    background:white;
    padding:30px;
    border-radius:18px;
    box-shadow:0 12px 30px rgba(0,0,0,.08);
    text-align:center;
}

.cta {
    background:#bbf7d0;
    padding:70px;
    border-radius:24px;
    text-align:center;
    margin:80px 0;
}

.footer {
    background:#1f2937;
    color:#d1d5db;
    padding:40px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🦴 Multi<span>Fracture</span>Net</h1>
<h3>AI-Powered Multimodal Bone Fracture Detection</h3>
<p>
Deep learning system combining X-ray images and clinical metadata
to detect multiple fracture types with high accuracy.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="grid">
<div class="card">🧠 <b>Multimodal AI</b><br>Image + Metadata</div>
<div class="card">⚡ <b>Fast Diagnosis</b><br>Seconds per scan</div>
<div class="card">📊 <b>Explainable AI</b><br>Grad-CAM & LIME</div>
<div class="card">🔒 <b>Privacy First</b><br>No data stored</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cta">
<h2>🚀 Ready to Analyze an X-ray?</h2>
<p>Upload an image and get instant AI-powered fracture insights.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
© 2026 MultiFractureNet • Research & Educational Use Only
</div>
""", unsafe_allow_html=True)

import streamlit as st

st.title("🏥 Our Team")

st.markdown("""
## Welcome to BoneFractureNet Team

We are a multidisciplinary team of experts dedicated to revolutionizing bone fracture detection through artificial intelligence and machine learning.

### Our Mission
To provide accurate, fast, and accessible bone fracture detection tools that assist healthcare professionals in making informed diagnostic decisions.

### Our Vision
Leveraging cutting-edge AI technology to improve patient outcomes and streamline the diagnostic process in orthopedic care.
""")

st.markdown("---")

# Team Statistics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Team Members", "8", delta="Growing")

with col2:
    st.metric("Specializations", "5+", delta="Expanding")

with col3:
    st.metric("Projects", "12", delta="+3")

with col4:
    st.metric("Publications", "15", delta="+2")

st.markdown("---")

# Team Expertise Areas
st.subheader("🎯 Areas of Expertise")

expertise_cols = st.columns(3)

with expertise_cols[0]:
    st.markdown("""
    **🤖 Artificial Intelligence**
    - Deep Learning
    - Computer Vision
    - Neural Networks
    - Model Optimization
    """)

with expertise_cols[1]:
    st.markdown("""
    **🏥 Medical Imaging**
    - Radiology
    - X-ray Analysis
    - Image Processing
    - Clinical Validation
    """)

with expertise_cols[2]:
    st.markdown("""
    **💻 Software Development**
    - Full Stack Development
    - Cloud Deployment
    - UI/UX Design
    - Data Engineering
    """)

st.markdown("---")

# Call to action
st.info("👥 **Want to know more about our team members?** Visit the [About](/About) page to meet each team member individually!")

st.markdown("---")

# Achievements
st.subheader("🏆 Recent Achievements")

st.success("✅ Successfully deployed AI model with 95%+ accuracy in fracture detection")
st.success("✅ Published research paper on multimodal CNN architecture for bone fracture classification")
st.success("✅ Collaborated with 3 major hospitals for clinical validation")
st.success("✅ Processed over 10,000 X-ray images for training and validation")

import streamlit as st

st.title("📞 Contact Us")

st.markdown("""
We'd love to hear from you! Whether you have questions about our bone fracture detection system, 
want to collaborate, or need support, feel free to reach out.
""")

st.markdown("---")

# Contact Form
st.subheader("📝 Send us a Message")

with st.form("contact_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name *", placeholder="John Doe")
        email = st.text_input("Email Address *", placeholder="john.doe@example.com")
    
    with col2:
        phone = st.text_input("Phone Number", placeholder="+1 (555) 123-4567")
        subject = st.selectbox("Subject *", [
            "General Inquiry",
            "Technical Support",
            "Collaboration Opportunity",
            "Research Partnership",
            "Bug Report",
            "Feature Request",
            "Other"
        ])
    
    message = st.text_area("Message *", placeholder="Tell us more about your inquiry...", height=150)
    
    submitted = st.form_submit_button("Send Message", use_container_width=True)
    
    if submitted:
        if name and email and message:
            st.success("✅ Thank you for your message! We'll get back to you within 24-48 hours.")
            st.balloons()
        else:
            st.error("⚠️ Please fill in all required fields (marked with *).")

st.markdown("---")

# Contact Information
st.subheader("📍 Contact Information")

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.markdown("""
    **🏢 Office Address**  
    BoneFractureNet Research Lab  
    123 Medical AI Boulevard  
    Innovation District  
    San Francisco, CA 94158  
    United States
    
    **📧 Email**  
    info@bonefracturenet.com  
    support@bonefracturenet.com
    """)

with info_col2:
    st.markdown("""
    **📱 Phone**  
    Main: +1 (555) 123-4567  
    Support: +1 (555) 987-6543  
    Fax: +1 (555) 123-4568
    
    **🕐 Business Hours**  
    Monday - Friday: 9:00 AM - 6:00 PM PST  
    Saturday: 10:00 AM - 2:00 PM PST  
    Sunday: Closed
    """)

st.markdown("---")

# Social Media Links
st.subheader("🌐 Connect With Us")

social_cols = st.columns(5)

with social_cols[0]:
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/company/bonefracturenet)")

with social_cols[1]:
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bonefracturenet)")

with social_cols[2]:
    st.markdown("[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/bonefracturenet)")

with social_cols[3]:
    st.markdown("[![ResearchGate](https://img.shields.io/badge/ResearchGate-00CCBB?style=for-the-badge&logo=researchgate&logoColor=white)](https://researchgate.net/lab/BoneFractureNet)")

with social_cols[4]:
    st.markdown("[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@bonefracturenet)")

st.markdown("---")

# FAQ Section
with st.expander("❓ Frequently Asked Questions"):
    st.markdown("""
    **Q: How accurate is the BoneFractureNet system?**  
    A: Our system achieves over 95% accuracy in detecting and classifying bone fractures across multiple bone types.
    
    **Q: Can I use this for clinical diagnosis?**  
    A: This tool is designed to assist healthcare professionals. Always consult with a qualified radiologist for final diagnosis.
    
    **Q: What types of fractures can the system detect?**  
    A: The system can detect distal, proximal, and post-fractures, as well as identify non-fracture cases.
    
    **Q: Is my data secure?**  
    A: Yes, we follow HIPAA compliance and industry-standard security practices to protect patient data.
    
    **Q: How can I collaborate with your team?**  
    A: Please use the contact form above or email us at collaboration@bonefracturenet.com
    """)

st.markdown("---")
st.info("💡 **Note:** This is a demonstration contact page. Update contact information with actual details.")

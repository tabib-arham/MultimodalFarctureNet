import streamlit as st

st.title("👥 About Our Team")

st.markdown("""
This page showcases our dedicated team of professionals working on the BoneFractureNet project.
Our multidisciplinary team combines expertise in AI, medical imaging, and healthcare to deliver accurate bone fracture detection.
""")

# Custom CSS for card styling
st.markdown("""
<style>
.team-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 20px;
    height: 100%;
}
.team-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}
.team-avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    margin: 0 auto 15px;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
    font-weight: bold;
    color: #667eea;
}
.team-name {
    color: white;
    font-size: 20px;
    font-weight: bold;
    margin: 10px 0;
}
.team-role {
    color: #e0e7ff;
    font-size: 14px;
    margin: 5px 0 15px;
}
.team-link {
    display: inline-block;
    background: white;
    color: #667eea;
    padding: 8px 20px;
    border-radius: 20px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
}
.team-link:hover {
    background: #f0f4ff;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# Team members data (placeholder)
team_members = [
    {
        "name": "Dr. Sarah Johnson",
        "role": "Lead Radiologist",
        "avatar": "SJ",
        "link": "https://linkedin.com/in/sarah-johnson"
    },
    {
        "name": "Michael Chen",
        "role": "ML Engineer",
        "avatar": "MC",
        "link": "https://github.com/michael-chen"
    },
    {
        "name": "Dr. Emily Rodriguez",
        "role": "Medical AI Specialist",
        "avatar": "ER",
        "link": "https://linkedin.com/in/emily-rodriguez"
    },
    {
        "name": "David Kim",
        "role": "Data Scientist",
        "avatar": "DK",
        "link": "https://github.com/david-kim"
    },
    {
        "name": "Dr. James Wilson",
        "role": "Orthopedic Consultant",
        "avatar": "JW",
        "link": "https://linkedin.com/in/james-wilson"
    },
    {
        "name": "Priya Patel",
        "role": "Computer Vision Engineer",
        "avatar": "PP",
        "link": "https://github.com/priya-patel"
    },
    {
        "name": "Dr. Robert Taylor",
        "role": "Clinical Advisor",
        "avatar": "RT",
        "link": "https://linkedin.com/in/robert-taylor"
    },
    {
        "name": "Lisa Anderson",
        "role": "Full Stack Developer",
        "avatar": "LA",
        "link": "https://github.com/lisa-anderson"
    }
]

# Display team members in a 4-column grid
st.markdown("---")
st.subheader("Meet the Team")

# Create rows of 4 columns each
for i in range(0, len(team_members), 4):
    cols = st.columns(4)
    for j in range(4):
        if i + j < len(team_members):
            member = team_members[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="team-card">
                    <div class="team-avatar">{member['avatar']}</div>
                    <div class="team-name">{member['name']}</div>
                    <div class="team-role">{member['role']}</div>
                    <a href="{member['link']}" target="_blank" class="team-link">Connect</a>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.info("💡 **Note:** This is a demonstration with placeholder data. Update team member information as needed.")

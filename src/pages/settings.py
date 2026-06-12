"""Settings Page"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

def render():
    """Render Settings page"""
    st.markdown("## ⚙️ Settings")
    
    # User preferences
    st.markdown("### 👤 User Preferences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name", "Your Name")
        email = st.text_input("Email", "your@email.com")
    
    with col2:
        country = st.selectbox("Country", ["USA", "India", "UK", "Canada", "Other"])
        target_companies = st.multiselect(
            "Target Companies",
            ["Microsoft", "Google", "Amazon", "TCS", "Infosys", "Accenture"]
        )
    
    # Career preferences
    st.markdown("### 🎯 Career Preferences")
    
    col1, col2 = st.columns(2)
    
    with col1:
        target_role = st.selectbox("Target Role", [
            "AI Engineer", "Data Scientist", "ML Engineer", "Cloud Engineer",
            "Software Engineer", "Data Analyst"
        ])
    
    with col2:
        experience_level = st.radio("Experience Level", ["Fresher", "Junior (1-2 years)", "Mid-level (3-5 years)"])
    
    # Notification preferences
    st.markdown("### 🔔 Notifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        email_updates = st.checkbox("Email Updates", value=True)
        job_alerts = st.checkbox("Job Alerts", value=True)
    
    with col2:
        opportunity_alerts = st.checkbox("Opportunity Alerts", value=True)
        weekly_digest = st.checkbox("Weekly Digest", value=True)
    
    # Data & Privacy
    st.markdown("### 🔐 Data & Privacy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Download My Data"):
            st.success("✅ Data export started")
    
    with col2:
        if st.button("🗑️ Delete My Account"):
            st.warning("⚠️ This action cannot be undone")
    
    # Save settings
    if st.button("💾 Save Settings", use_container_width=True):
        st.success("✅ Settings saved successfully!")

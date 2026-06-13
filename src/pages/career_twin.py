"""Career Twin Page - Visualize future career profile"""
import streamlit as st
from pathlib import Path
import sys
import plotly.graph_objects as go

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.career_agents import CareerTwinAgent

def render():
    """Render Career Twin page"""
    st.markdown("## 🤖 AI Career Twin")
    st.markdown("Meet your future self - an AI-generated profile showing your ideal career state.")
    
    if st.session_state.resume_data is None:
        st.info("👋 Please upload your resume first in Resume Analyzer")
        return
    
    # Select target role
    target_role = st.selectbox("Select Target Role", [
        "AI Engineer", "Data Scientist", "ML Engineer", "Cloud Engineer",
        "Software Engineer", "Data Analyst"
    ])
    
    # Timeline
    timeline_months = st.slider("Timeline (months)", 3, 24, 12)
    
    if st.button("🤖 Generate Career Twin", use_container_width=True):
        with st.spinner("Generating your future career profile..."):
            agent = CareerTwinAgent()
            twin_profile = agent.generate_career_twin(
                st.session_state.resume_data,
                target_role,
                timeline_months
            )
        
        st.success("✅ Career Twin generated!")
        
        # Display twin profile
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Current Profile")
            st.metric("Skills", len(st.session_state.resume_data.get('skills', [])))
            st.metric("Projects", len(st.session_state.resume_data.get('projects', [])))
            st.metric("Certifications", len(st.session_state.resume_data.get('certifications', [])))
        
        with col2:
            st.markdown("### Target Profile")
            ideal = twin_profile['ideal_future_state']
            st.metric("Skills", len(ideal['skills']))
            st.metric("Projects", ideal['projects'])
            st.metric("Certifications", len(ideal['certifications']))
        
        # Missing elements
        st.markdown("### 📋 Missing Elements")
        missing = twin_profile['missing_elements']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"**Skills to Learn:** {len(missing['skills'])}")
            for skill in missing['skills'][:5]:
                st.markdown(f"- {skill}")
        
        with col2:
            st.markdown(f"**Certifications:** {len(missing['certifications'])}")
            for cert in missing['certifications'][:3]:
                st.markdown(f"- {cert}")
        
        with col3:
            st.markdown(f"**Projects to Build:** {missing['projects']}")
            st.markdown("**Experience Gap:** ~" + str(missing.get('experience_gap', 2)) + " years")
        
        # Timeline
        st.markdown("### 🎯 Milestone Checkpoints")
        for milestone in twin_profile['milestone_checkpoints']:
            with st.expander(f"Month {milestone['month']}: {milestone['milestone']}"):
                st.markdown(f"**Deliverables:**")
                for deliverable in milestone['deliverables']:
                    st.markdown(f"- ✅ {deliverable}")
        
        # Success probability
        st.markdown("### 📊 Success Probability")
        success_rate = twin_profile['estimated_success_rate']
        st.progress(success_rate / 100)
        st.markdown(f"**Estimated Success Rate: {success_rate:.1f}%**")
        
        # Monthly targets
        st.markdown("### 📅 Monthly Targets")
        for target in twin_profile['monthly_targets'][:3]:
            with st.expander(f"Month {target['month']}"):
                for action in target['actions']:
                    st.markdown(f"- {action}")
"""Career GPS Page - Personalized roadmaps"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.career_agents import CareerGPSAgent

def render():
    """Render Career GPS page"""
    st.markdown("## 💼 Career GPS")
    st.markdown("Generate personalized 30/60/90 day roadmaps")
    
    if st.session_state.resume_data is None:
        st.info("👋 Please upload your resume first")
        return
    
    col1, col2 = st.columns(2)
    
    with col1:
        target_role = st.selectbox("Target Role", [
            "AI Engineer", "Data Scientist", "ML Engineer", "Cloud Engineer",
            "Software Engineer", "Data Analyst"
        ])
    
    with col2:
        duration = st.radio("Roadmap Duration", [30, 60, 90])
    
    if st.button("🗺️ Generate Roadmap", use_container_width=True):
        with st.spinner(f"Generating {duration}-day roadmap..."):
            agent = CareerGPSAgent()
            roadmap = agent.generate_career_roadmap(
                st.session_state.resume_data,
                target_role,
                duration
            )
        
        st.success("✅ Roadmap generated!")
        
        # Learning path
        st.markdown("### 📚 Learning Path")
        for week in roadmap['learning_path']:
            with st.expander(f"Week {week['week']}: {week['focus']} ({week['hours_per_week']}h/week)"):
                for topic in week['topics']:
                    st.markdown(f"- {topic}")
        
        # Weekly milestones
        st.markdown("### 🎯 Weekly Milestones")
        for milestone in roadmap['weekly_milestones'][:4]:
            st.markdown(f"**Week {milestone['week']}:** {milestone['milestone']}")
            for deliverable in milestone['deliverables']:
                st.markdown(f"  - ✅ {deliverable}")
        
        # Action items
        st.markdown("### ⚡ Action Items")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Immediate (This Week)**")
            for action in roadmap['action_items']['immediate'][:3]:
                st.markdown(f"- {action}")
        
        with col2:
            st.markdown("**Weekly**")
            for action in roadmap['action_items']['weekly'][:3]:
                st.markdown(f"- {action}")
        
        with col3:
            st.markdown("**Monthly**")
            for action in roadmap['action_items']['monthly'][:3]:
                st.markdown(f"- {action}")
        
        # Projects
        st.markdown("### 💻 Project Timeline")
        for project in roadmap['project_roadmap']:
            st.markdown(f"**{project['project_num']}. {project['name']}** (Week {project['start_week']}, {project['difficulty']})")
            st.caption(project['description'])
        
        # Resources
        st.markdown("### 📖 Resources")
        resources = roadmap['resources']
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Courses:**")
            for course in resources['courses']:
                st.markdown(f"- {course}")
        
        with col2:
            st.markdown("**Platforms:**")
            for platform in resources['platforms']:
                st.markdown(f"- {platform}")
        
        # Community
        st.markdown("### 🤝 Community Involvement")
        for task in roadmap['community_involvement'][:5]:
            st.markdown(f"- {task}")
        
        # Download roadmap
        st.download_button(
            "📥 Download Roadmap",
            str(roadmap),
            f"roadmap_{duration}_days.txt",
            "text/plain"
        )

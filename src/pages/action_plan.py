"""Action Plan Page"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

def render():
    """Render Action Plan page"""
    st.markdown("## ⚡ Personalized Action Plan")
    st.markdown("Get prioritized tasks tailored to your goals")
    
    if st.session_state.resume_data is None:
        st.info("👋 Please upload your resume first")
        return
    
    goal = st.selectbox("What's your primary goal?", [
        "Get a job offer",
        "Switch careers",
        "Build a strong portfolio",
        "Get certifications",
        "Improve interview skills",
        "Learn new technologies"
    ])
    
    timeline = st.slider("Target timeline (weeks)", 4, 26, 12)
    
    if st.button("🎯 Generate Action Plan", use_container_width=True):
        with st.spinner("Generating personalized action plan..."):
            # Sample action plan
            action_plan = {
                "immediate": [
                    {"task": "Update LinkedIn profile", "priority": "High", "days": 1},
                    {"task": "Polish GitHub profile", "priority": "High", "days": 2},
                    {"task": "Fix resume formatting", "priority": "High", "days": 1},
                ],
                "weekly": [
                    {"task": "Learn new skill", "priority": "High", "days": 7},
                    {"task": "Build mini-project", "priority": "Medium", "days": 7},
                    {"task": "Network with professionals", "priority": "Medium", "days": 7},
                    {"task": "Practice coding problems", "priority": "High", "days": 7},
                ],
                "monthly": [
                    {"task": "Complete course module", "priority": "High", "days": 30},
                    {"task": "Build portfolio project", "priority": "High", "days": 30},
                    {"task": "Attend meetup/conference", "priority": "Medium", "days": 30},
                    {"task": "Mock interview", "priority": "High", "days": 30},
                ]
            }
        
        st.success("✅ Action plan created!")
        
        # Immediate actions
        st.markdown("### 🚨 Immediate Actions (This Week)")
        for action in action_plan['immediate']:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"**{action['task']}**")
            with col2:
                st.markdown(f"_{action['priority']}_")
            with col3:
                st.checkbox(f"✅", key=f"imm_{action['task']}")
        
        # Weekly actions
        st.markdown("### 📅 Weekly Actions")
        week = st.slider("Week", 1, timeline // 4, 1)
        
        for action in action_plan['weekly']:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"**{action['task']}**")
            with col2:
                st.markdown(f"_{action['priority']}_")
            with col3:
                st.checkbox(f"✅", key=f"week_{week}_{action['task']}")
        
        # Monthly milestones
        st.markdown("### 🎯 Monthly Milestones")
        for month in range(1, (timeline // 4) + 1):
            with st.expander(f"Month {month}"):
                for action in action_plan['monthly']:
                    st.markdown(f"- {action['task']}")
        
        # Progress tracking
        st.markdown("### 📊 Progress Tracking")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tasks Completed", "0", "0%")
        with col2:
            st.metric("On Track", "Yes", "💚")
        
        # Download plan
        st.download_button(
            "📥 Download Action Plan",
            str(action_plan),
            "action_plan.txt",
            "text/plain"
        )

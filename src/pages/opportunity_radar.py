"""Opportunity Radar Page"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.helpers import kb_manager

def render():
    """Render Opportunity Radar page"""
    st.markdown("## 🎪 Opportunity Radar")
    st.markdown("Discover ranked opportunities (internships, certifications, projects, hackathons)")
    
    if st.session_state.resume_data is None:
        st.info("👋 Please upload your resume first")
        return
    
    opportunities = kb_manager.load_opportunities()
    
    # Filter by type
    opp_type = st.selectbox("Opportunity Type", ["certifications", "projects", "internships"])
    
    if opp_type in opportunities:
        items = opportunities[opp_type]
        
        st.markdown(f"### Top {opp_type.title()}")
        
        for i, item in enumerate(items[:5], 1):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**{i}. {item.get('title') or item.get('name', 'N/A')}**")
                st.caption(item.get('description', ''))
                
                if 'duration_weeks' in item or 'duration_months' in item:
                    duration = item.get('duration_weeks') or item.get('duration_months', 'N/A')
                    st.markdown(f"⏱️ **Duration:** {duration}")
                
                if 'difficulty' in item or 'level' in item:
                    difficulty = item.get('difficulty') or item.get('level', 'N/A')
                    st.markdown(f"📊 **Level:** {difficulty}")
                
                if 'relevance_score' in item:
                    st.progress(item['relevance_score'] / 100)
            
            with col2:
                if 'relevance_score' in item:
                    st.metric("Match", f"{item['relevance_score']:.0f}%")
                if 'cost' in item:
                    st.metric("Cost", f"${item['cost']}")
                elif 'value_score' in item:
                    st.metric("Value", f"{item['value_score']}/10")

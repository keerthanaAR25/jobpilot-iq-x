"""Company Readiness Page"""
import streamlit as st
from pathlib import Path
import sys
import plotly.graph_objects as go

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.foundry_iq import FoundryIQEngine
from utils.helpers import kb_manager

def render():
    """Render company readiness page"""
    st.markdown("## 🎯 Dream Company Readiness")
    st.markdown("Assess your readiness for your dream companies.")
    
    if st.session_state.resume_data is None:
        st.info("👋 Please upload your resume first")
        return
    
    kb = {
        'companies': kb_manager.load_companies(),
        'roles': kb_manager.load_roles()
    }
    
    # Select company
    companies = list(kb['companies'].keys())
    selected_company = st.selectbox("Select Dream Company", companies)
    
    if st.button("🔍 Analyze Readiness", use_container_width=True):
        with st.spinner(f"Analyzing readiness for {selected_company}..."):
            engine = FoundryIQEngine(str(Path(__file__).parent.parent.parent / 'data' / 'knowledge_base'))
            readiness = engine.assess_company_readiness(
                st.session_state.resume_data,
                selected_company,
                kb
            )
        
        st.success("✅ Analysis complete!")
        
        # Overall readiness
        col1, col2 = st.columns(2)
        
        with col1:
            readiness_score = readiness['readiness_score']
            st.metric("Overall Readiness Score", f"{readiness_score}/100")
            st.progress(readiness_score / 100)
        
        with col2:
            st.metric("Skill Match", f"{readiness['skill_match_percentage']:.1f}%")
            st.metric("Experience Alignment", f"{readiness['experience_alignment']:.0f}%")
            st.metric("Certification Alignment", f"{readiness['certification_alignment']:.0f}%")
        
        # Company info
        company_info = kb['companies'][selected_company]
        
        st.markdown("### 🏢 Company Overview")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**Industry:** {company_info.get('industry', 'N/A')}")
            st.markdown(f"**Culture:** {company_info.get('company_culture', 'N/A')}")
        
        with col2:
            st.markdown("**Hiring Process:**")
            for step in company_info.get('hiring_process', []):
                st.markdown(f"- {step}")
        
        # Missing requirements
        st.markdown("### ⚠️ Missing Requirements")
        missing = readiness['missing_requirements']
        if missing:
            for skill in missing[:5]:
                st.markdown(f"- 📚 {skill}")
        else:
            st.success("✅ You have all key requirements!")
        
        # Action plan
        st.markdown("### 📋 Preparation Plan")
        for action in readiness['action_plan'][:5]:
            st.markdown(f"- 🎯 {action}")
        
        # Interview tips
        st.markdown("### 💡 Interview Tips")
        for tip in company_info.get('interview_tips', []):
            st.markdown(f"- {tip}")
        
        # Application tips
        st.markdown("### 📝 Application Tips")
        for tip in company_info.get('application_tips', []):
            st.markdown(f"- {tip}")
        
        # Reasoning trace
        with st.expander("🔍 View Reasoning Trace (Foundry IQ)"):
            for step in readiness['reasoning_trace'][:6]:
                st.markdown(f"**Step {step['step_number']}: {step['title']}**")
                st.caption(step['description'])
                st.text(f"Confidence: {step.get('confidence', 'N/A')}")

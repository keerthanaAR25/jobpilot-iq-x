"""Shortlist Analyzer Page - Hero Feature"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.foundry_iq import FoundryIQEngine
from utils.helpers import kb_manager, report_generator

def render():
    """Render Shortlist Analyzer page - Hero Feature"""
    st.markdown("## ❓ Why Am I Not Getting Shortlisted?")
    st.markdown("Hero Feature: Deep analysis of why your applications are not succeeding")
    
    if st.session_state.resume_data is None:
        st.info("👋 Please upload your resume first")
        return
    
    st.info("💡 This feature uses Foundry IQ's multi-step reasoning to identify exact issues preventing your success.")
    
    if st.button("🔍 Analyze My Shortlist Chances", use_container_width=True):
        with st.spinner("Performing deep analysis using Foundry IQ..."):
            kb = {
                'companies': kb_manager.load_companies(),
                'roles': kb_manager.load_roles()
            }
            
            engine = FoundryIQEngine(str(Path(__file__).parent.parent.parent / 'data' / 'knowledge_base'))
            analysis = engine.analyze_shortlist_issues(st.session_state.resume_data, kb)
        
        st.success("✅ Analysis complete!")
        
        # Overall score
        col1, col2 = st.columns(2)
        
        with col1:
            score = analysis['shortlist_score']
            st.metric("Shortlist Success Score", f"{score}/100")
            st.progress(score / 100)
        
        with col2:
            if score >= 80:
                st.success("🟢 Excellent chances of getting shortlisted")
            elif score >= 60:
                st.warning("🟡 Good chances with some improvements needed")
            elif score >= 40:
                st.warning("🟠 Moderate chances - significant improvements needed")
            else:
                st.error("🔴 Low chances - major overhaul required")
        
        # Main issues
        st.markdown("### 🚨 Main Issues Identified")
        
        issues = analysis['main_issues']
        if issues:
            for i, issue in enumerate(issues[:5], 1):
                st.markdown(f"**{i}. {issue}**")
        else:
            st.success("✅ No major issues found!")
        
        # Category breakdown
        st.markdown("### 📊 Detailed Assessment")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            completeness = analysis['profile_completeness']
            st.metric("Profile Completeness", f"{completeness}/100")
            st.progress(completeness / 100)
        
        with col2:
            portfolio = analysis['portfolio_assessment']
            st.markdown(f"**Portfolio Quality:** {portfolio}")
        
        with col3:
            certs = len(analysis['certification_gaps'])
            st.metric("Missing Certifications", certs)
        
        # Skill gaps
        st.markdown("### 💼 Skill Gaps")
        skill_gaps = analysis['skill_gaps']
        if skill_gaps:
            for skill in skill_gaps:
                st.markdown(f"- 📚 {skill}")
        else:
            st.success("✅ Your skills are strong!")
        
        # Immediate actions
        st.markdown("### ✅ Immediate Actions (Next 7 Days)")
        for action in analysis['immediate_actions']:
            st.markdown(f"- 🎯 {action}")
        
        # Long-term improvements
        st.markdown("### 🚀 Long-term Improvements (30-90 Days)")
        for improvement in analysis['long_term_improvements']:
            st.markdown(f"- 📈 {improvement}")
        
        # Reasoning trace
        with st.expander("🔍 View Foundry IQ Reasoning Trace"):
            st.markdown("### Multi-Step Reasoning Process")
            
            for step in analysis['reasoning_trace'][:6]:
                with st.expander(f"Step {step['step_number']}: {step['title']}"):
                    st.markdown(f"**{step['description']}**")
                    st.markdown(f"Confidence: {step.get('confidence', 'N/A')}")
                    
                    if step.get('citations'):
                        st.markdown("**Sources:**")
                        for citation in step['citations']:
                            st.caption(f"- {citation}")
        
        # Generate report
        st.markdown("---")
        report = report_generator.generate_shortlist_analysis_report(analysis)
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "📥 Download Full Report",
                report,
                "shortlist_analysis_report.md",
                "text/markdown"
            )
        
        with col2:
            if st.button("📋 Create Detailed Action Plan"):
                st.session_state.page_selection = "⚡ Action Plan"
                st.rerun()

"""
Dashboard Page - Main overview of career profile
"""
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

def render():
    """Render dashboard page"""
    
    # Check if user has uploaded resume
    if st.session_state.resume_data is None and st.session_state.health_score is None:
        st.info("👋 Welcome to JobPilot IQ X! Start by uploading your resume in the Resume Analyzer.")
        
        # Quick start guide
        st.markdown("## 🚀 Quick Start Guide")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### Step 1: Upload Resume
            📄 Share your resume to get started
            - PDF format supported
            - Auto-extract information
            - Secure & private
            """)
        
        with col2:
            st.markdown("""
            ### Step 2: Career Assessment
            📊 Get comprehensive analysis
            - Career Health Score
            - Skill Gap Analysis
            - Company Readiness
            """)
        
        with col3:
            st.markdown("""
            ### Step 3: Action Plan
            🎯 Personalized roadmap
            - 30/60/90 day plans
            - Opportunity ranking
            - Interview prep
            """)
        
        # Feature highlights
        st.markdown("## ✨ Key Features")
        
        features = {
            "🎯 Career Twin": "AI version of your future self",
            "💼 Company Readiness": "Target company preparation",
            "🎪 Opportunity Radar": "Ranked opportunities",
            "🎤 Interview Arena": "Practice & evaluation",
            "⚡ Action Plan": "Prioritized tasks",
            "❓ Shortlist Analysis": "Why you're not shortlisted"
        }
        
        cols = st.columns(3)
        for idx, (feature, desc) in enumerate(features.items()):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="card success-card">
                    <h4>{feature}</h4>
                    <p>{desc}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Call to action
        st.markdown("---")
        if st.button("📄 Upload Your Resume", key="upload_btn", use_container_width=True):
            st.session_state.page_selection = "📄 Resume Analyzer"
            st.rerun()
    
    else:
        # User has data, show dashboard
        st.markdown("## 📊 Career Dashboard")
        
        # KPI Cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.session_state.health_score:
                health = st.session_state.health_score.get('overall_score', 0)
                st.metric("Health Score", f"{health}/100", delta="📊")
            else:
                st.metric("Health Score", "N/A", help="Complete resume upload")
        
        with col2:
            skills_count = len(st.session_state.resume_data.get('skills', [])) if st.session_state.resume_data else 0
            st.metric("Skills", skills_count, help="Technical skills identified")
        
        with col3:
            projects_count = len(st.session_state.resume_data.get('projects', [])) if st.session_state.resume_data else 0
            st.metric("Projects", projects_count, help="Portfolio projects")
        
        with col4:
            certs_count = len(st.session_state.resume_data.get('certifications', [])) if st.session_state.resume_data else 0
            st.metric("Certifications", certs_count, help="Professional certs")
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.health_score:
                # Health score gauge
                categories = st.session_state.health_score['category_scores']
                
                fig = go.Figure(data=[
                    go.Scatterpolar(
                        r=[categories[cat]['score'] for cat in categories.keys()],
                        theta=[cat.replace('_', ' ').title() for cat in categories.keys()],
                        fill='toself',
                        marker_color='#00D9FF',
                        showlegend=False
                    )
                ])
                
                fig.update_layout(
                    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                    title="Career Health Profile",
                    height=400,
                    paper_bgcolor='rgba(22, 33, 62, 0.6)',
                    font=dict(color='white')
                )
                
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if st.session_state.health_score and 'category_scores' in st.session_state.health_score:
                categories = st.session_state.health_score['category_scores']
                
                fig = go.Figure(data=[
                    go.Bar(
                        y=[cat.replace('_', ' ').title() for cat in categories.keys()],
                        x=[categories[cat]['score'] for cat in categories.keys()],
                        orientation='h',
                        marker_color=['#00D9FF', '#FF006E', '#FFD60A', '#00D084', '#FFA500', '#FF1744'],
                        showlegend=False
                    )
                ])
                
                fig.update_layout(
                    title="Category Breakdown",
                    xaxis_title="Score",
                    height=400,
                    paper_bgcolor='rgba(22, 33, 62, 0.6)',
                    font=dict(color='white'),
                    xaxis=dict(range=[0, 100])
                )
                
                st.plotly_chart(fig, use_container_width=True)
        
        # Recommendations
        st.markdown("## 💡 Recommended Actions")
        
        if st.session_state.health_score:
            recommendations = st.session_state.health_score.get('recommendations', [])
            for i, rec in enumerate(recommendations[:3]):
                st.markdown(f"""
                <div class="card">
                    <b>{i+1}. {rec}</b>
                </div>
                """, unsafe_allow_html=True)
        
        # Next steps
        st.markdown("## 🎯 Next Steps")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🤖 View Career Twin", use_container_width=True):
                st.session_state.page_selection = "🤖 Career Twin"
                st.rerun()
        
        with col2:
            if st.button("🎯 Check Company Readiness", use_container_width=True):
                st.session_state.page_selection = "🎯 Dream Company Readiness"
                st.rerun()
        
        with col3:
            if st.button("⚡ Create Action Plan", use_container_width=True):
                st.session_state.page_selection = "⚡ Action Plan"
                st.rerun()

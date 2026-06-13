"""
Resume Analyzer Page - Upload and analyze resumes
"""
import streamlit as st
import tempfile
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.resume_parser import parse_resume
from modules.career_health import CareerHealthEngine
from utils.helpers import kb_manager, ui_helper, report_generator

def render():
    """Render resume analyzer page"""
    
    st.markdown("## 📄 Resume Analyzer")
    st.markdown("Upload your resume to extract skills, experience, and generate a career health score.")
    
    # Upload resume
    uploaded_file = st.file_uploader("Choose your resume (PDF)", type=['pdf'], key="resume_upload")
    
    if uploaded_file:
        st.info(f"📤 Analyzing: {uploaded_file.name}")
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name
        
        try:
            # Parse resume
            with st.spinner("🔍 Extracting resume information..."):
                resume_data = parse_resume(tmp_file_path)
            
            # Store in session
            st.session_state.resume_data = resume_data
            
            # Display extracted information
            st.success("✅ Resume analyzed successfully!")
            
            # Tabs for different sections
            tabs = st.tabs(["👤 Personal Info", "💼 Experience", "🎓 Education", "🛠️ Skills", "💻 Projects", "📜 Certifications"])
            
            with tabs[0]:
                st.subheader("Personal Information")
                personal_info = resume_data.get('personal_info', {})

                if personal_info.get('name'):
                    st.markdown(f"### {personal_info['name']}")
                if personal_info.get('title'):
                    st.markdown(f"*{personal_info['title']}*")

                col1, col2 = st.columns(2)
                with col1:
                    if personal_info.get('email'):
                        st.markdown(f"**Email:** `{personal_info['email']}`")
                    if personal_info.get('phone'):
                        st.markdown(f"**Phone:** `{personal_info['phone']}`")
                
                with col2:
                    if personal_info.get('linkedin'):
                        st.markdown(f"**LinkedIn:** [{personal_info['linkedin']}](https://{personal_info['linkedin']})")
                    if personal_info.get('github'):
                        st.markdown(f"**GitHub:** [{personal_info['github']}](https://{personal_info['github']})")
                
                # Summary
                summary = resume_data.get('summary', '')
                if summary:
                    st.markdown(f"**Professional Summary:**\n\n{summary}")
            
            with tabs[1]:
                st.subheader("Work Experience")
                experience = resume_data.get('experience', [])

                if experience:
                    for i, exp in enumerate(experience, 1):
                        title = exp.get('title', 'N/A')
                        duration = exp.get('duration', '')
                        header = f"**{i}. {title}**"
                        if duration:
                            header += f"  \n*{duration}*"
                        st.markdown(header)
                        if exp.get('company'):
                            st.markdown(f"{exp['company']}")
                        if exp.get('keyword'):
                            st.caption(f"Category: {exp['keyword']}")
                        if exp.get('description'):
                            st.write(exp['description'])
                        st.markdown("---")
                else:
                    st.info("No work experience found")
            
            with tabs[2]:
                st.subheader("Education")
                education = resume_data.get('education', [])

                if education:
                    for i, edu in enumerate(education, 1):
                        line = f"**{i}. {edu.get('degree', 'N/A')}**"
                        if edu.get('year'):
                            line += f"  \n*{edu['year']}*"
                        st.markdown(line)
                        if edu.get('institution'):
                            st.markdown(edu['institution'])
                        st.markdown("---")
                else:
                    st.info("No education details found")
            
            with tabs[3]:
                st.subheader("Technical Skills")
                skills = resume_data.get('skills', [])
                
                if skills:
                    col1, col2, col3 = st.columns(3)
                    for i, skill in enumerate(skills):
                        col = [col1, col2, col3][i % 3]
                        with col:
                            st.markdown(f"✅ {skill}")
                    
                    st.markdown(f"\n**Total Skills:** {len(skills)}")
                else:
                    st.warning("⚠️ No technical skills extracted. Try uploading a more detailed resume.")
            
            with tabs[4]:
                st.subheader("Projects & Portfolio")
                projects = resume_data.get('projects', [])

                if projects:
                    for i, proj in enumerate(projects, 1):
                        st.markdown(f"**{i}. {proj.get('title', 'Project')}**")
                        if proj.get('subtitle'):
                            st.markdown(f"*{proj['subtitle']}*")
                        if proj.get('tech_stack'):
                            st.markdown(f"**Tech Stack:** {proj['tech_stack']}")
                        if proj.get('description'):
                            st.write(proj['description'])
                        st.markdown("---")
                    st.markdown(f"\n**Total Projects:** {len(projects)}")
                else:
                    st.info("No projects found. Consider adding projects to your resume!")
            
            with tabs[5]:
                st.subheader("Certifications")
                certs = resume_data.get('certifications', [])
                
                if certs:
                    for i, cert in enumerate(certs, 1):
                        st.markdown(f"**{i}.** {cert}")
                    st.markdown(f"\n**Total Certifications:** {len(certs)}")
                else:
                    st.info("No certifications found")
            
            # Generate Career Health Score
            st.markdown("---")
            st.markdown("## 📊 Career Health Score")
            
            if st.button("🎯 Calculate Career Health Score", use_container_width=True):
                with st.spinner("Computing career health metrics..."):
                    # Calculate health score
                    engine = CareerHealthEngine()
                    health_score = engine.calculate_health_score(resume_data)
                    st.session_state.health_score = health_score
                
                # Display results
                st.success("✅ Health score calculated!")
                
                # Overall score
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    # Progress bar
                    overall_score = health_score['overall_score']
                    st.metric("Overall Career Health Score", f"{overall_score}/100", help="Composite score across all categories")
                    st.progress(overall_score / 100)
                    st.markdown(f"**Grade:** {health_score['grade']}")
                
                with col2:
                    st.markdown("### Score Range\n- 90-100: A+ (Excellent)\n- 80-89: A (Very Good)\n- 70-79: B (Good)\n- 60-69: C (Average)\n- <60: F (Needs Work)")
                
                # Category breakdown
                st.markdown("### Category Breakdown")
                
                cols = st.columns(2)
                for idx, (cat, score_data) in enumerate(health_score['category_scores'].items()):
                    with cols[idx % 2]:
                        cat_name = cat.replace('_', ' ').title()
                        score = score_data['score']
                        st.metric(cat_name, f"{score}/100")
                        st.progress(score / 100)
                
                # Strengths
                st.markdown("### 💪 Strengths")
                for strength in health_score['strengths']:
                    st.markdown(f"✅ {strength}")
                
                # Weaknesses
                st.markdown("### 📈 Areas for Improvement")
                for weakness in health_score['weaknesses']:
                    st.markdown(f"⚠️ {weakness}")
                
                # Recommendations
                st.markdown("### 💡 Recommendations")
                for rec in health_score['recommendations']:
                    st.markdown(f"🎯 {rec}")
                
                # Download report
                col1, col2 = st.columns(2)
                with col1:
                    report = report_generator.generate_career_health_report(health_score)
                    st.download_button(
                        "📥 Download Health Report",
                        report,
                        "career_health_report.md",
                        "text/markdown"
                    )
                
                with col2:
                    if st.button("🚀 Next: Explore More Insights", use_container_width=True):
                        st.session_state.page_selection = "📊 Dashboard"
                        st.rerun()
        
        except Exception as e:
            st.error(f"❌ Error analyzing resume: {str(e)}")
            st.info("💡 Try a different resume or ensure it's in valid PDF format")
    
    else:
        # Placeholder for no file uploaded
        st.markdown("""
        ### 📋 What We Extract:
        
        <div class="stats-grid">
            <div class="card success-card">
                <h4>👤 Personal Info</h4>
                <p>Name, email, phone, LinkedIn, GitHub</p>
            </div>
            <div class="card success-card">
                <h4>💼 Experience</h4>
                <p>Job titles, companies, tenure</p>
            </div>
            <div class="card success-card">
                <h4>🛠️ Skills</h4>
                <p>Technical skills and tools</p>
            </div>
            <div class="card success-card">
                <h4>💻 Projects</h4>
                <p>Notable projects and achievements</p>
            </div>
            <div class="card success-card">
                <h4>📜 Certifications</h4>
                <p>Professional certifications</p>
            </div>
            <div class="card success-card">
                <h4>🎓 Education</h4>
                <p>Degrees and educational background</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🔒 Your Privacy Matters")
        st.markdown("""
        - ✅ Resumes are processed securely
        - ✅ Data stored locally on your machine
        - ✅ No sharing with third parties
        - ✅ Delete anytime
        """)
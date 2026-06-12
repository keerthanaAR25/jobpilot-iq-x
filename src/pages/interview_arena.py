"""Interview Arena Page"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.interview_arena import InterviewArena

def render():
    """Render Interview Arena page"""
    st.markdown("## 🎤 Interview Arena")
    st.markdown("Practice technical, behavioral, and role-specific questions")
    
    if st.session_state.resume_data is None:
        st.info("👋 Please upload your resume first")
        return
    
    target_role = st.selectbox("Target Role", [
        "AI Engineer", "Data Scientist", "ML Engineer", "Cloud Engineer",
        "Software Engineer", "Data Analyst"
    ])
    
    interview_type = st.selectbox("Interview Type", ["technical", "behavioral", "role_specific"])
    
    if st.button("🎯 Generate Questions", use_container_width=True):
        with st.spinner("Generating interview questions..."):
            arena = InterviewArena()
            questions_data = arena.generate_interview_questions(
                st.session_state.resume_data,
                target_role,
                interview_type
            )
        
        st.success("✅ Questions generated!")
        
        # Questions
        for question in questions_data['questions']:
            with st.expander(f"Q{question['id']}: {question['question'][:80]}..."):
                st.markdown(question['question'])
                
                if 'difficulty' in question:
                    st.markdown(f"**Difficulty:** {question['difficulty']}")
                
                if 'expected_duration_minutes' in question:
                    st.markdown(f"⏱️ **Time:** ~{question['expected_duration_minutes']} minutes")
                
                if 'key_points' in question:
                    st.markdown("**Key Points to Cover:**")
                    for point in question['key_points']:
                        st.markdown(f"- {point}")
                
                # Answer input
                user_answer = st.text_area(f"Your Answer to Q{question['id']}", height=150)
                
                if st.button(f"📊 Evaluate Answer", key=f"eval_{question['id']}"):
                    expected_points = question.get('key_points', [])
                    feedback = arena.evaluate_answer(question, user_answer, expected_points)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Score", f"{feedback['score']}/100")
                    with col2:
                        st.markdown(f"**Assessment:** {feedback['overall_assessment']}")
                    
                    st.markdown("**Feedback:**")
                    for fb in feedback['feedback']:
                        st.markdown(f"- {fb}")
        
        # Tips
        st.markdown("### 💡 Preparation Tips")
        for tip in questions_data['preparation_tips']:
            st.markdown(f"- {tip}")

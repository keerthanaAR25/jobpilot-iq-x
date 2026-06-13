"""
Interview Arena Page
Fixed:
- user_answer stored in session_state so it survives rerun when Evaluate is clicked
- evaluation result stored in session_state per question, displayed persistently
- no KeyError on missing question keys
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from modules.interview_arena import InterviewArena


def render():
    st.markdown("## 🎤 Interview Arena")
    st.markdown("Practice technical, behavioral, and role-specific questions with AI evaluation")

    if st.session_state.get('resume_data') is None:
        st.info("👋 Please upload your resume first in Resume Analyzer")
        return

    # ── Init session state ────────────────────────────────────────────────
    if 'interview_questions' not in st.session_state:
        st.session_state.interview_questions = None
    if 'interview_answers' not in st.session_state:
        st.session_state.interview_answers = {}   # {qid: answer_text}
    if 'interview_evals' not in st.session_state:
        st.session_state.interview_evals = {}     # {qid: eval_dict}

    # ── Settings ──────────────────────────────────────────────────────────
    col1, col2 = st.columns(2)
    with col1:
        target_role = st.selectbox("Target Role", [
            "AI Engineer", "Data Scientist", "ML Engineer", "Cloud Engineer",
            "Software Engineer", "Data Analyst"
        ])
    with col2:
        interview_type = st.selectbox("Interview Type", [
            "technical", "behavioral", "role_specific"
        ], format_func=lambda x: x.replace("_", " ").title())

    if st.button("🎯 Generate Questions", use_container_width=True):
        with st.spinner("Generating interview questions..."):
            arena = InterviewArena()
            questions_data = arena.generate_interview_questions(
                st.session_state.resume_data, target_role, interview_type
            )
        # Store in session — survives reruns
        st.session_state.interview_questions = questions_data
        st.session_state.interview_answers = {}
        st.session_state.interview_evals = {}

    # ── Display questions ─────────────────────────────────────────────────
    qdata = st.session_state.interview_questions
    if qdata is None:
        return

    st.success("✅ Questions ready! Answer each one and click Evaluate.")
    st.markdown("---")

    arena = InterviewArena()
    questions = qdata.get('questions', [])

    if not questions:
        st.warning("No questions generated for this combination. Try a different role or type.")
        return

    for question in questions:
        qid = str(question.get('id', 0))
        q_text = question.get('question', 'Question not available')

        with st.expander(f"Q{qid}: {q_text[:70]}{'...' if len(q_text) > 70 else ''}", expanded=(qid == '1')):
            st.markdown(f"**{q_text}**")

            meta_col1, meta_col2 = st.columns(2)
            with meta_col1:
                if question.get('difficulty'):
                    diff = question['difficulty']
                    color = "🟢" if diff == "Easy" else "🟡" if diff == "Intermediate" else "🔴"
                    st.markdown(f"**Difficulty:** {color} {diff}")
            with meta_col2:
                if question.get('expected_duration_minutes'):
                    st.markdown(f"⏱️ **Time:** ~{question['expected_duration_minutes']} min")

            if question.get('key_points'):
                st.markdown("**Key Points to Cover:**")
                for pt in question['key_points']:
                    st.markdown(f"- {pt}")

            # ── Answer box — value read from session_state ─────────────
            saved_answer = st.session_state.interview_answers.get(qid, "")
            answer = st.text_area(
                f"Your Answer",
                value=saved_answer,
                height=150,
                key=f"ans_{qid}",
                placeholder="Type your answer here... (aim for 3-5 sentences minimum)",
            )
            # Save answer immediately on any change
            st.session_state.interview_answers[qid] = answer

            # ── Evaluate button ────────────────────────────────────────
            if st.button(f"📊 Evaluate Answer", key=f"eval_btn_{qid}"):
                if not answer.strip():
                    st.warning("⚠️ Please write your answer before evaluating.")
                else:
                    with st.spinner("Evaluating your answer..."):
                        expected_points = question.get('key_points', [])
                        feedback = arena.evaluate_answer(question, answer, expected_points)
                    st.session_state.interview_evals[qid] = feedback

            # ── Show evaluation if it exists ───────────────────────────
            eval_result = st.session_state.interview_evals.get(qid)
            if eval_result:
                st.markdown("---")
                score = eval_result.get('score', 0)
                assessment = eval_result.get('overall_assessment', '')
                score_color = "🟢" if score >= 75 else "🟡" if score >= 50 else "🔴"

                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    st.metric("Score", f"{score}/100")
                with res_col2:
                    st.markdown(f"**Assessment:** {score_color} {assessment}")

                st.progress(score / 100)

                feedback_items = eval_result.get('feedback', eval_result.get('improvement_areas', []))
                if feedback_items:
                    st.markdown("**Feedback:**")
                    for fb in feedback_items:
                        st.markdown(f"- {fb}")

                missing = eval_result.get('missing_points', [])
                if missing:
                    st.markdown("**Points you missed:**")
                    for mp in missing:
                        st.markdown(f"- ❌ {mp}")

    # ── Session score summary ─────────────────────────────────────────────
    if st.session_state.interview_evals:
        st.markdown("---")
        st.markdown("### 📊 Session Summary")
        scores = [v.get('score', 0) for v in st.session_state.interview_evals.values()]
        avg = sum(scores) / len(scores)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Questions Answered", len(scores))
        with col2:
            st.metric("Average Score", f"{avg:.0f}/100")
        with col3:
            grade = "Excellent 🌟" if avg >= 80 else "Good 👍" if avg >= 60 else "Keep Practicing 💪"
            st.metric("Grade", grade)

    # ── Tips ──────────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("### 💡 Preparation Tips")
    for tip in qdata.get('preparation_tips', []):
        st.markdown(f"- {tip}")
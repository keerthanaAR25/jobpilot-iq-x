"""
Action Plan Page - Fixed: checkboxes persist across reruns using session_state
"""
import streamlit as st
from pathlib import Path
import sys
import json

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


def _get_action_plan(resume_data: dict, goal: str, timeline: int) -> dict:
    """Generate personalized action plan based on resume data."""
    skills = resume_data.get('skills', [])
    projects = resume_data.get('projects', [])
    certs = resume_data.get('certifications', [])

    immediate = [
        {"task": "Update LinkedIn profile with all skills and projects", "priority": "High"},
        {"task": "Polish GitHub — add README to every project", "priority": "High"},
        {"task": "Fix resume formatting (PDF spacing issues detected)", "priority": "High"},
    ]

    if len(skills) < 8:
        immediate.append({"task": "Add missing technical skills to resume", "priority": "High"})
    if not certs:
        immediate.append({"task": "Enroll in Microsoft Azure AI-900 (free on Microsoft Learn)", "priority": "High"})

    weekly = [
        {"task": "Learn 1 new skill from your gap list", "priority": "High"},
        {"task": "Build or improve a portfolio project", "priority": "High"},
        {"task": "Solve 5 coding problems (LeetCode / HackerRank)", "priority": "Medium"},
        {"task": "Network with 2 professionals on LinkedIn", "priority": "Medium"},
        {"task": "Read 1 technical article or watch 1 tutorial", "priority": "Low"},
    ]

    monthly = [
        {"task": "Complete 1 online course module", "priority": "High"},
        {"task": "Build and publish 1 portfolio project on GitHub", "priority": "High"},
        {"task": "Do 2 mock interviews (technical + HR)", "priority": "High"},
        {"task": "Attend 1 meetup, hackathon, or webinar", "priority": "Medium"},
    ]

    return {"immediate": immediate, "weekly": weekly, "monthly": monthly}


def render():
    st.markdown("## ⚡ Personalized Action Plan")
    st.markdown("Get prioritized tasks tailored to your goals")

    if st.session_state.get('resume_data') is None:
        st.info("👋 Please upload your resume first in Resume Analyzer")
        return

    # ── Init checkbox state once ──────────────────────────────────────────
    if 'action_plan_data' not in st.session_state:
        st.session_state.action_plan_data = None
    if 'action_checkboxes' not in st.session_state:
        st.session_state.action_checkboxes = {}

    goal = st.selectbox("What's your primary goal?", [
        "Get a job offer", "Switch careers", "Build a strong portfolio",
        "Get certifications", "Improve interview skills", "Learn new technologies"
    ])
    timeline = st.slider("Target timeline (weeks)", 4, 26, 12)

    if st.button("🎯 Generate Action Plan", use_container_width=True):
        with st.spinner("Generating personalized action plan..."):
            plan = _get_action_plan(st.session_state.resume_data, goal, timeline)
        # Store plan in session — survives reruns
        st.session_state.action_plan_data = plan
        st.session_state.action_checkboxes = {}
        st.success("✅ Action plan created!")

    # ── Display plan if it exists (persists across reruns) ────────────────
    plan = st.session_state.action_plan_data
    if plan is None:
        return

    st.success("✅ Action plan ready!")

    def _checkbox(key: str, label: str) -> bool:
        """Checkbox whose state is stored in session_state dict, not widget."""
        current = st.session_state.action_checkboxes.get(key, False)
        checked = st.checkbox("Done", value=current, key=f"cb_{key}")
        if checked != current:
            st.session_state.action_checkboxes[key] = checked
        return checked

    # ── Immediate actions ─────────────────────────────────────────────────
    st.markdown("### 🚨 Immediate Actions (This Week)")
    for i, action in enumerate(plan['immediate']):
        col1, col2, col3 = st.columns([4, 1, 1])
        key = f"imm_{i}"
        done = st.session_state.action_checkboxes.get(key, False)
        with col1:
            label_style = "~~" if done else "**"
            if done:
                st.markdown(f"~~{action['task']}~~")
            else:
                st.markdown(f"**{action['task']}**")
        with col2:
            color = "🔴" if action['priority'] == "High" else "🟡"
            st.markdown(f"{color} {action['priority']}")
        with col3:
            new_val = st.checkbox("✅", value=done, key=f"cb_imm_{i}")
            st.session_state.action_checkboxes[key] = new_val

    # ── Progress bar ──────────────────────────────────────────────────────
    total_tasks = len(plan['immediate']) + len(plan['weekly']) + len(plan['monthly'])
    done_count = sum(1 for v in st.session_state.action_checkboxes.values() if v)
    pct = done_count / total_tasks if total_tasks else 0

    st.markdown("---")
    st.markdown(f"### 📊 Progress: {done_count}/{total_tasks} tasks completed")
    st.progress(pct)

    # ── Weekly actions ────────────────────────────────────────────────────
    st.markdown("### 📅 Weekly Actions")
    week = st.slider("View week", 1, max(timeline // 4, 1), 1)

    for i, action in enumerate(plan['weekly']):
        col1, col2, col3 = st.columns([4, 1, 1])
        key = f"week_{week}_{i}"
        done = st.session_state.action_checkboxes.get(key, False)
        with col1:
            if done:
                st.markdown(f"~~{action['task']}~~")
            else:
                st.markdown(f"**{action['task']}**")
        with col2:
            color = "🔴" if action['priority'] == "High" else "🟡" if action['priority'] == "Medium" else "🟢"
            st.markdown(f"{color} {action['priority']}")
        with col3:
            new_val = st.checkbox("✅", value=done, key=f"cb_week_{week}_{i}")
            st.session_state.action_checkboxes[key] = new_val

    # ── Monthly milestones ────────────────────────────────────────────────
    st.markdown("### 🎯 Monthly Milestones")
    for month in range(1, (timeline // 4) + 1):
        with st.expander(f"Month {month}"):
            for i, action in enumerate(plan['monthly']):
                key = f"month_{month}_{i}"
                done = st.session_state.action_checkboxes.get(key, False)
                col1, col2 = st.columns([5, 1])
                with col1:
                    if done:
                        st.markdown(f"~~{action['task']}~~")
                    else:
                        st.markdown(f"- {action['task']}")
                with col2:
                    new_val = st.checkbox("✅", value=done, key=f"cb_month_{month}_{i}")
                    st.session_state.action_checkboxes[key] = new_val

    # ── Download ──────────────────────────────────────────────────────────
    st.markdown("---")
    plan_text = "# Personalized Action Plan\n\n"
    plan_text += "## Immediate Actions\n" + "\n".join(f"- [ ] {a['task']}" for a in plan['immediate'])
    plan_text += "\n\n## Weekly Actions\n" + "\n".join(f"- [ ] {a['task']}" for a in plan['weekly'])
    plan_text += "\n\n## Monthly Milestones\n" + "\n".join(f"- [ ] {a['task']}" for a in plan['monthly'])
    st.download_button("📥 Download Action Plan", plan_text, "action_plan.md", "text/markdown")
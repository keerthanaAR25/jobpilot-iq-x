"""Page stubs for JobPilot IQ X"""

def create_page_stub(page_name, emoji, description):
    content = f'''"""
{page_name} Page
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.helpers import kb_manager

def render():
    """Render {page_name} page"""
    st.markdown("## {emoji} {page_name}")
    st.markdown("{description}")
    
    if st.session_state.resume_data is None:
        st.info("👋 Please upload your resume first in Resume Analyzer")
        return
    
    st.markdown("### Loading {page_name}...")
    st.spinner("Feature coming soon...")
'''
    return content

pages = {
    "career_twin.py": ("Career Twin", "🤖", "Visualize your future self with AI Career Twin"),
    "company_readiness.py": ("Dream Company Readiness", "🎯", "Assess readiness for top companies"),
    "career_gps.py": ("Career GPS", "💼", "Generate 30/60/90 day personalized roadmaps"),
    "opportunity_radar.py": ("Opportunity Radar", "🎪", "Discover ranked opportunities"),
    "interview_arena.py": ("Interview Arena", "🎤", "Practice technical and behavioral interviews"),
    "action_plan.py": ("Action Plan", "⚡", "Get prioritized action items"),
    "shortlist_analyzer.py": ("Shortlist Analyzer", "❓", "Understand why you're not getting shortlisted"),
    "settings.py": ("Settings", "⚙️", "Configure your preferences"),
}

for filename, (name, emoji, desc) in pages.items():
    content = create_page_stub(name, emoji, desc)
    with open(f'/jobpilot-iq-x/src/pages/{filename}', 'w') as f:
        f.write(content)
    print(f"Created {filename}")

print("All page stubs created!")

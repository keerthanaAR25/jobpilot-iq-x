"""
JobPilot IQ X - Main Streamlit Application
AI Career Command Center
"""
import streamlit as st
import sys
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))
sys.path.insert(0, str(Path(__file__).parent))

# Navigation helper function
def navigate_to(page_name):
    """Navigate to a different page by updating session state"""
    page_map = {
        "📊 Dashboard": "📊 Dashboard",
        "📄 Resume Analyzer": "📄 Resume Analyzer",
        "🤖 Career Twin": "🤖 Career Twin",
        "🎯 Dream Company Readiness": "🎯 Dream Company Readiness",
        "💼 Career GPS": "💼 Career GPS",
        "🎪 Opportunity Radar": "🎪 Opportunity Radar",
        "🎤 Interview Arena": "🎤 Interview Arena",
        "⚡ Action Plan": "⚡ Action Plan",
        "❓ Why Not Shortlisted?": "❓ Why Not Shortlisted?",
        "⚙️ Settings": "⚙️ Settings",
    }
    if page_name in page_map:
        st.session_state.page_selection = page_map[page_name]
        st.rerun()

# Page configuration
st.set_page_config(
    page_title="JobPilot IQ X - AI Career Command Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
def load_custom_css():
    """Load custom CSS for styling"""
    css = """
    <style>
        :root {
            --primary-color: #00D9FF;
            --secondary-color: #FF006E;
            --background: #0A0E27;
            --surface: #16213E;
            --text-primary: #FFFFFF;
            --text-secondary: #B0B0B0;
            --accent: #FFD60A;
        }
        
        * {
            margin: 0;
            padding: 0;
        }
        
        body {
            background-color: var(--background);
            color: var(--text-primary);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        .main {
            background: linear-gradient(135deg, rgba(10, 14, 39, 0.95), rgba(22, 33, 62, 0.95));
        }
        
        .stMetric {
            background: rgba(22, 33, 62, 0.6);
            padding: 15px;
            border-radius: 12px;
            border-left: 4px solid var(--primary-color);
            backdrop-filter: blur(10px);
        }
        
        .stButton > button {
            background: linear-gradient(135deg, #00D9FF, #FF006E);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(0, 217, 255, 0.3);
        }
        
        h1 {
            background: linear-gradient(135deg, #00D9FF, #FF006E);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            margin-bottom: 20px;
        }
        
        h2, h3 {
            color: var(--primary-color);
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        .card {
            background: rgba(22, 33, 62, 0.6);
            border: 1px solid rgba(0, 217, 255, 0.2);
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            backdrop-filter: blur(10px);
        }
        
        .success-card {
            border-left: 4px solid #00D084;
        }
        
        .warning-card {
            border-left: 4px solid #FFA500;
        }
        
        .danger-card {
            border-left: 4px solid #FF1744;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Load styling
load_custom_css()

# Initialize session state
if 'user_id' not in st.session_state:
    st.session_state.user_id = f"user_{datetime.now().timestamp()}"
    st.session_state.current_page = "Dashboard"
    st.session_state.user_profile = None
    st.session_state.resume_data = None
    st.session_state.health_score = None
    st.session_state.page_selection = "📊 Dashboard"

if 'page_selection' not in st.session_state:
    st.session_state.page_selection = "📊 Dashboard"

# Sidebar navigation
st.sidebar.markdown("# 🚀 JobPilot IQ X")
st.sidebar.markdown("### AI Career Command Center")
st.sidebar.markdown("---")

pages = {
    "📊 Dashboard": "pages/dashboard",
    "📄 Resume Analyzer": "pages/resume_analyzer",
    "🤖 Career Twin": "pages/career_twin",
    "🎯 Dream Company Readiness": "pages/company_readiness",
    "💼 Career GPS": "pages/career_gps",
    "🎪 Opportunity Radar": "pages/opportunity_radar",
    "🎤 Interview Arena": "pages/interview_arena",
    "⚡ Action Plan": "pages/action_plan",
    "❓ Why Not Shortlisted?": "pages/shortlist_analyzer",
    "⚙️ Settings": "pages/settings"
}

page_selection = st.sidebar.radio("Navigation", list(pages.keys()), index=list(pages.keys()).index(st.session_state.page_selection) if st.session_state.page_selection in pages.keys() else 0)
st.session_state.page_selection = page_selection

# User info in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Session ID:** `{st.session_state.user_id[:8]}...`")
st.sidebar.markdown(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Help section
with st.sidebar.expander("📚 Help & Resources"):
    st.markdown("""
    **Getting Started:**
    1. Upload your resume in Resume Analyzer
    2. Get your Career Health Score
    3. Explore your Career Twin profile
    4. Check company readiness
    5. Build your action plan
    
    **Features:**
    - 📊 Real-time career analytics
    - 🎯 Personalized recommendations
    - 📈 Progress tracking
    - 💡 AI-powered insights
    
    **Tips:**
    - Keep your profile updated
    - Complete all assessments
    - Take action on recommendations
    - Join our community
    """)

# Main content area
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <h1>🚀 JobPilot IQ X</h1>
    <p style="color: #B0B0B0; font-size: 18px;">
        Your Personal AI Career Strategist | Powered by Foundry IQ
    </p>
</div>
""", unsafe_allow_html=True)

# Route to selected page
if page_selection == "📊 Dashboard":
    from pages import dashboard
    dashboard.render()
elif page_selection == "📄 Resume Analyzer":
    from pages import resume_analyzer
    resume_analyzer.render()
elif page_selection == "🤖 Career Twin":
    from pages import career_twin
    career_twin.render()
elif page_selection == "🎯 Dream Company Readiness":
    from pages import company_readiness
    company_readiness.render()
elif page_selection == "💼 Career GPS":
    from pages import career_gps
    career_gps.render()
elif page_selection == "🎪 Opportunity Radar":
    from pages import opportunity_radar
    opportunity_radar.render()
elif page_selection == "🎤 Interview Arena":
    from pages import interview_arena
    interview_arena.render()
elif page_selection == "⚡ Action Plan":
    from pages import action_plan
    action_plan.render()
elif page_selection == "❓ Why Not Shortlisted?":
    from pages import shortlist_analyzer
    shortlist_analyzer.render()
elif page_selection == "⚙️ Settings":
    from pages import settings
    settings.render()

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.caption("🔐 Your data is secure and private")
with col2:
    st.caption("🤝 Powered by GitHub Copilot & Foundry IQ")
with col3:
    st.caption("📧 For support: support@jobpilot.ai")

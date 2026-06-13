# 🚀 JobPilot IQ X - AI Career Command Center

> An AI-powered Career Intelligence Platform for the Microsoft Agents League Hackathon

![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Hackathon](https://img.shields.io/badge/Hackathon-Microsoft%20Agents%20League-purple)



## 🎯 Hackathon Submission

**🏆 Creative Apps Track | 🤖 Foundry IQ + GitHub Copilot | 🔍 Transparent AI**

For the complete hackathon submission package, see:
- **[HACKATHON_SUBMISSION.md](HACKATHON_SUBMISSION.md)** - Complete project description & AI value proposition
- **[ARCHITECTURE_DIAGRAM_EXPLAINED.md](ARCHITECTURE_DIAGRAM_EXPLAINED.md)** - Technology integration & design
- **[SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)** - Quick start & deployment guides
- **[SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)** - Final verification checklist

## ⚡ Quick Start (5 Minutes)

```bash
# 1. Clone the repository
git clone https://github.com/[your-username]/jobpilot-iq-x.git
cd jobpilot-iq-x

# 2. Create virtual environment and install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Run the application
streamlit run app.py

# Application opens at http://localhost:8501

```
## 🚀 Quick Start Videos

https://drive.google.com/file/d/13m5iYl6COuUi_GpNMZEk6VNqaaK6BYLw/view?usp=sharing



## 📊 Project Overview

**JobPilot IQ X** is an enterprise-grade AI Career Intelligence Platform that helps students, freshers, career switchers, and job seekers become career-ready through:

- 🤖 **Agentic Knowledge Retrieval** - Multi-step reasoning with transparency
- 📈 **Grounded Recommendations** - Citation-based guidance with reasoning traces
- 💡 **Career Intelligence Engine** - Foundry IQ powered analysis
- 🎯 **Personalized Action Planning** - 30/60/90 day roadmaps
- 🎪 **Opportunity Discovery** - Ranked recommendations with explanations

## ✨ Core Features

### 1. **Resume Analyzer** 📄
- Upload PDF resumes
- Auto-extract skills, projects, certifications, education, experience
- Generate professional summary
- Real-time validation

### 2. **Career Health Score** 📊
- Comprehensive 100-point scoring system
- 6 Category breakdown:
  - Technical Skills (25%)
  - Projects & Portfolio (20%)
  - Certifications (15%)
  - Experience (20%)
  - Communication (10%)
  - Career Readiness (10%)
- Visual gauge charts and breakdowns
- Actionable recommendations

### 3. **AI Career Twin** 🤖
- Generate future career profile (3-24 months)
- Missing skills assessment
- Milestone checkpoints
- Monthly target planning
- Success probability calculation
- Salary expectations

### 4. **Dream Company Readiness** 🎯
- Supported Companies: Microsoft, Google, Amazon, TCS, Infosys, Accenture, + more
- Multi-step Foundry IQ reasoning
- Skill match percentage
- Interview preparation
- Application tips
- Hiring process breakdown

### 5. **Skill Gap Analyzer** 💼
- Supported Roles: AI Engineer, Data Scientist, ML Engineer, Cloud Engineer, Software Engineer, Data Analyst, Business Analyst, Cybersecurity Analyst
- Identify missing skills
- Prioritized learning paths
- Time estimation
- Resource recommendations

### 6. **Career GPS** 🗺️
- 30/60/90 Day personalized roadmaps
- Weekly learning paths
- Milestone tracking
- Project timelines
- Community involvement tasks
- Success metrics

### 7. **Opportunity Radar** 🎪
- Ranked internship recommendations
- Relevant hackathons
- Recommended certifications
- Portfolio project suggestions
- Learning path curation
- Relevance scoring with explanations

### 8. **Interview Arena** 🎤
- Technical questions with key points
- Behavioral interview prep
- Role-specific questions
- Company-specific preparation
- Answer evaluation with feedback
- Interview tips and resources

### 9. **Why Am I Not Getting Shortlisted?** ❓ (HERO FEATURE)
Multi-step Foundry IQ analysis:
- Profile completeness assessment
- Critical skill gap analysis
- Portfolio quality check
- Resume formatting issues
- Certification analysis
- Specific corrective actions
- Full reasoning trace

### 10. **Personalized Action Plan** ⚡
- Immediate actions (7 days)
- Weekly milestones
- Monthly goals
- Prioritized task list
- Progress tracking
- Download-ready format

## 🏗️ Architecture

```
JobPilot IQ X
├── app.py (Main Streamlit Application)
├── config/
│   └── config.py (Configuration & Constants)
├── src/
│   ├── modules/
│   │   ├── resume_parser.py (PDF parsing & extraction)
│   │   ├── career_health.py (Health scoring engine)
│   │   ├── foundry_iq.py (Multi-step reasoning engine) ⭐
│   │   ├── career_agents.py (Twin & GPS agents)
│   │   └── interview_arena.py (Interview questions & evaluation)
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── resume_analyzer.py
│   │   ├── career_twin.py
│   │   ├── company_readiness.py
│   │   ├── career_gps.py
│   │   ├── opportunity_radar.py
│   │   ├── interview_arena.py
│   │   ├── action_plan.py
│   │   ├── shortlist_analyzer.py
│   │   └── settings.py
│   └── utils/
│       ├── database.py (SQLite management)
│       ├── helpers.py (Utilities & managers)
│       └── __init__.py
├── data/
│   ├── knowledge_base/
│   │   ├── companies.json (6+ companies with detailed info)
│   │   ├── roles.json (8+ job roles with requirements)
│   │   └── opportunities.json (Certs, projects, internships)
│   ├── jobpilot.db (SQLite database)
│   └── uploads/ (Resume uploads)
└── docs/
    ├── README.md
    ├── ARCHITECTURE.md
    └── DEPLOYMENT.md
```

## 🧠 Foundry IQ Implementation

JobPilot IQ X implements all 8 Foundry IQ Principles:

### 1. **Agentic Knowledge Retrieval** ✓
- Multi-step reasoning with explicit steps
- Knowledge base queries at each step
- Context-aware decision making

### 2. **Grounded Recommendations** ✓
- Every recommendation backed by knowledge base
- Citation system for traceability
- Evidence-based guidance

### 3. **Multi-Step Reasoning** ✓
```python
Step 1: Parse user profile
Step 2: Retrieve target role requirements
Step 3: Identify skill overlap
Step 4: Calculate missing skills
Step 5: Prioritize skill gaps
Step 6: Generate recommendations
Step 7: Create learning path
Step 8: Build action plan
```

### 4. **Citation-Based Guidance** ✓
- All recommendations include sources
- Knowledge base links for verification
- Transparent reasoning chain

### 5. **Context-Aware Decision Making** ✓
- User experience level considered
- Industry trends factored in
- Company-specific requirements analyzed

### 6. **Opportunity Ranking** ✓
- Relevance scoring algorithm
- Multiple scoring factors
- Diversity in recommendations

### 7. **Reduced Hallucinations** ✓
- Only uses knowledge base data
- No unfounded claims
- Conservative scoring

### 8. **Transparent Reasoning Trace** ✓
- Every analysis shows full reasoning
- User can view step-by-step logic
- Explainable AI throughout

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.8+ |
| **Charts** | Plotly |
| **Database** | SQLite |
| **Knowledge Base** | JSON |
| **Resume Parsing** | PyPDF2 |
| **Styling** | Custom CSS |
| **AI Model** | GitHub Models or OpenAI-compatible |

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- git

### Step 1: Clone Repository
```bash
cd jobpilot-iq-x
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database
```bash
python -c "from src.utils.database import Database; Database()"
```

### Step 5: Run Application
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 🚀 Deployment

### Option 1: Streamlit Cloud (Recommended)
```bash
# Push to GitHub
git push origin main

# Connect GitHub repo to Streamlit Cloud
# Visit: https://share.streamlit.io/
```

### Option 2: Docker
```bash
# Build image
docker build -t jobpilot-iq-x .

# Run container
docker run -p 8501:8501 jobpilot-iq-x
```

### Option 3: Heroku
```bash
# Deploy
git push heroku main
```

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

## 📊 Database Schema

```sql
-- Users
CREATE TABLE users (
    id, user_id, name, email, created_at, updated_at
)

-- Resumes
CREATE TABLE resumes (
    id, user_id, filename, file_path, extracted_data, uploaded_at
)

-- Career Profiles
CREATE TABLE career_profiles (
    id, user_id, current_profile, career_goals, skill_gaps, readiness_scores
)

-- Assessments
CREATE TABLE assessments (
    id, user_id, assessment_type, company_name, role_name, readiness_score, missing_skills
)

-- Action Plans
CREATE TABLE action_plans (
    id, user_id, plan_type, duration_days, milestones
)

-- Reasoning Traces
CREATE TABLE reasoning_traces (
    id, user_id, feature_name, reasoning_steps, citations
)
```

## 📚 Knowledge Base

### Companies (6+ companies)
Each company includes:
- Key competencies
- Required skills
- Hiring process
- Interview tips
- Application guidelines
- Salary ranges

### Roles (8+ roles)
Each role includes:
- Core skills required
- Tools and technologies
- Certifications
- Experience requirements
- Growth paths
- Interview focus areas

### Opportunities (100+ items)
- Certifications with duration and cost
- Projects with difficulty levels
- Internships with requirements
- Learning paths

## 🎨 UI Design

- **Theme**: Dark Mode (Professional)
- **Style**: Glassmorphism with gradients
- **Colors**: Cyan (#00D9FF), Magenta (#FF006E), Gold (#FFD60A)
- **Layouts**: Responsive grid system
- **Charts**: Interactive Plotly visualizations
- **Widgets**: Gauge, Radar, Bar, Timeline charts

## 📈 Key Metrics

- **Career Health Score**: 0-100 points
- **Readiness Scores**: 0-100 for companies and roles
- **Skill Match %**: Percentage match with role/company
- **Success Probability**: Chances of achieving goals
- **Relevance Score**: Opportunity relevance (0-100)

## 🔄 Reasoning Trace Example

```
Feature: Skill Gap Analysis for AI Engineer

Step 1: Parse User Profile ✓
- Extracted 12 technical skills
- Confidence: 95%

Step 2: Retrieve Role Requirements ✓
- AI Engineer needs 10 core skills
- Source: Knowledge base - roles.json

Step 3: Identify Skill Overlap ✓
- Found 8 matching skills
- 80% overlap

Step 4: Calculate Missing Skills ✓
- Missing: TensorFlow, Transformers, MLOps
- Criticality: High

Step 5: Prioritize Skills ✓
- Priority ranking: TensorFlow (2 weeks), Transformers (3 weeks), MLOps (4 weeks)

Step 6: Generate Recommendations ✓
- Recommended courses: TensorFlow Official Course, DeepLearning.AI
- Estimated timeline: 8 weeks

Step 7: Create Learning Path ✓
- Week 1-2: TensorFlow fundamentals
- Week 3-4: Advanced concepts
- Week 5-6: Project building
- Week 7-8: Portfolio refinement
```

## 💡 Usage Example

### For a Fresher
1. Upload resume → Get health score (45/100)
2. View Career Twin → See target profile (AI Engineer)
3. Check skill gaps → Learn Python, TensorFlow, Deep Learning
4. Follow Career GPS → 90-day roadmap
5. Build projects from Opportunity Radar
6. Practice interviews in Interview Arena
7. Implement action plan → Get job ready

### For a Career Switcher
1. Upload previous resume
2. Analyze company readiness for target companies
3. Identify critical skill gaps
4. Follow intensive 60-day plan
5. Get certifications
6. Mock interview practice
7. Apply armed with insights

## 🔐 Privacy & Security

- ✅ Resumes processed locally
- ✅ No data sent to external servers (unless using APIs)
- ✅ SQLite local database
- ✅ Delete data anytime
- ✅ No sharing with third parties
- ✅ GDPR compliant design

## 📝 Files Generated

- Career Health Reports (MD)
- Shortlist Analysis Reports (MD)
- Roadmap Plans (TXT)
- Action Plans (TXT)
- Interview Prep Guides (MD)

## 🤝 Contributing

Contributions welcome! Areas to enhance:

- [ ] Add more companies to knowledge base
- [ ] Expand role templates
- [ ] Integrate with job APIs
- [ ] Add LinkedIn import
- [ ] Implement AI chat feature
- [ ] Add more interview questions
- [ ] Expand certification database
- [ ] Add mobile app
- [ ] Implement progress tracking
- [ ] Add community features

## 📞 Support & Feedback

- Documentation: See `docs/` folder
- Issues: GitHub Issues
- Email: support@jobpilot.ai

## 📄 License

MIT License - See LICENSE file

## 🏆 Hackathon Info

- **Hackathon**: Microsoft Agents League
- **Track**: Creative Apps
- **Primary Tool**: GitHub Copilot
- **Intelligence Layer**: Foundry IQ
- **Status**: Production-ready for hackathon submission

## 📊 Project Stats

- **Lines of Code**: 3000+
- **Modules**: 5 core + 10 page modules
- **Knowledge Base Items**: 100+
- **Companies**: 6+
- **Roles**: 8+
- **Features**: 10 major features
- **Pages**: 10 interactive pages
- **Database Tables**: 7
- **Reasoning Steps**: Multi-step chains

## 🚀 Quick Start Videos

https://drive.google.com/file/d/13m5iYl6COuUi_GpNMZEk6VNqaaK6BYLw/view?usp=sharing

<img width="1907" height="772" alt="image" src="https://github.com/user-attachments/assets/7a4c9fcb-8d8d-4f41-bd7e-9d37ded6779e" />
<img width="1910" height="865" alt="image" src="https://github.com/user-attachments/assets/16a11ccf-4a73-44e3-81f7-52db40669390" />
<img width="1918" height="871" alt="image" src="https://github.com/user-attachments/assets/e0d60798-704f-4039-93cd-2b1e876f0a2c" />
<img width="1912" height="857" alt="image" src="https://github.com/user-attachments/assets/11cb966e-d2ae-4480-9085-89475928d8de" />
<img width="1902" height="901" alt="image" src="https://github.com/user-attachments/assets/d1f47e80-a3db-494c-9d64-fbc98df84ac0" />
<img width="1872" height="862" alt="image" src="https://github.com/user-attachments/assets/b2b741be-c983-4a31-b09c-0673409b9aa9" />
<img width="1912" height="851" alt="image" src="https://github.com/user-attachments/assets/8f2142c0-8cee-4e49-942b-d909c4813a22" />
<img width="1883" height="883" alt="image" src="https://github.com/user-attachments/assets/65ae4e59-377e-47e2-a054-aadb878addfc" />
<img width="1912" height="880" alt="image" src="https://github.com/user-attachments/assets/bce4244d-7e21-476e-b8be-a2d957ea7e3d" />
<img width="1918" height="876" alt="image" src="https://github.com/user-attachments/assets/2e1a630d-bd1e-4cf9-91e3-9dfc387052d3" />
<img width="1912" height="866" alt="image" src="https://github.com/user-attachments/assets/4d72c709-6481-484c-a3a8-ef8072326743" />

---

**Built with ❤️ using GitHub Copilot and Foundry IQ**

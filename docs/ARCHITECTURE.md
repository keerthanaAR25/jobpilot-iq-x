# 🏗️ Architecture & Design Document

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     STREAMLIT UI LAYER                       │
│  ┌──────────────┬──────────────┬──────────────┐              │
│  │  Dashboard   │  Resume      │  Career Twin │              │
│  ├──────────────┼──────────────┼──────────────┤              │
│  │ Company      │  Career GPS  │  Opportunity │              │
│  │ Readiness    │              │  Radar       │              │
│  ├──────────────┼──────────────┼──────────────┤              │
│  │ Interview    │  Action Plan │  Shortlist   │              │
│  │ Arena        │              │  Analyzer    │              │
│  └──────────────┴──────────────┴──────────────┘              │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│               APPLICATION LOGIC LAYER                        │
│  ┌────────────────────────────────────────────────────────┐  │
│  │         Foundry IQ Reasoning Engine (CORE)             │  │
│  │  - Multi-step reasoning                               │  │
│  │  - Knowledge retrieval                                │  │
│  │  - Citation tracking                                 │  │
│  │  - Transparent reasoning traces                      │  │
│  └────────────────────────────────────────────────────────┘  │
│                            ↓                                   │
│  ┌──────────┬──────────────┬─────────────┬──────────────┐     │
│  │ Resume   │ Career Health│ Career Twin │ Interview    │     │
│  │ Parser   │ Engine       │ Agent       │ Arena        │     │
│  └──────────┴──────────────┴─────────────┴──────────────┘     │
│                                                                │
│  ┌──────────┬──────────────┬─────────────┐                    │
│  │ Career   │ Skill Gap    │ Opportunity │                    │
│  │ GPS Agent│ Analyzer     │ Ranker      │                    │
│  └──────────┴──────────────┴─────────────┘                    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│              DATA & KNOWLEDGE LAYER                          │
│  ┌───────────────────┬─────────────────────────────────┐    │
│  │  Knowledge Base   │       SQLite Database           │    │
│  │  ─────────────────│ ─────────────────────────────   │    │
│  │  - companies.json │ - users table                   │    │
│  │  - roles.json     │ - resumes table                │    │
│  │  - opps.json      │ - profiles table               │    │
│  │                   │ - assessments table            │    │
│  │                   │ - reasoning_traces table       │    │
│  └───────────────────┴─────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Module Architecture

### 1. **Resume Parser** (resume_parser.py)
```
Input: PDF Resume
  ↓
[PDF Extraction] → Text extraction using PyPDF2
  ↓
[Pattern Matching] → Regex patterns for:
  - Email, Phone, LinkedIn, GitHub
  - Education, Experience, Skills
  - Projects, Certifications
  ↓
Output: Structured JSON
  {
    personal_info: {},
    skills: [],
    projects: [],
    experience: [],
    certifications: [],
    education: [],
    summary: ""
  }
```

### 2. **Career Health Engine** (career_health.py)
```
Input: User Profile
  ↓
[Calculate Category Scores]
  - Technical Skills (25%)
  - Projects (20%)
  - Certifications (15%)
  - Experience (20%)
  - Communication (10%)
  - Readiness (10%)
  ↓
[Weighted Average]
  ↓
[Grade Assignment] → A+ to F
  ↓
[Identify Strengths & Weaknesses]
  ↓
Output: Health Score Report
  {
    overall_score: 75,
    grade: "B",
    categories: {...},
    strengths: [],
    weaknesses: [],
    recommendations: []
  }
```

### 3. **Foundry IQ Engine** (foundry_iq.py) - CORE ⭐
```
Input: User Profile + Target Context
  ↓
[Multi-Step Reasoning Chain]
  
Step 1: Profile Parsing
  - Extract user capabilities
  - Normalize data
  - Assess completeness
  Confidence: 95%
  
Step 2: Knowledge Retrieval
  - Query knowledge base
  - Get role/company requirements
  - Retrieve opportunities
  Sources: companies.json, roles.json
  
Step 3: Comparative Analysis
  - Match user skills vs requirements
  - Calculate overlap percentage
  - Identify gaps
  Confidence: 92%
  
Step 4: Priority Ranking
  - Score each gap by importance
  - Estimate learning difficulty
  - Rank by ROI
  
Step 5: Recommendation Generation
  - Select relevant learning paths
  - Suggest projects
  - Recommend certifications
  
Step 6: Plan Creation
  - Generate milestones
  - Create timeline
  - Set success metrics
  Confidence: 88%
  ↓
Output: Complete Analysis with Reasoning Trace
  {
    analysis: {...},
    reasoning_steps: [
      {step_number, title, description, confidence, citations},
      ...
    ],
    recommendations: [],
    timeline: "8 weeks"
  }
```

### 4. **Career Twin Agent** (career_agents.py)
```
Input: Current Profile + Target Role + Timeline
  ↓
[Load Ideal Profile for Role]
  - Required skills
  - Certifications
  - Experience
  - Projects
  ↓
[Gap Analysis]
  - Calculate missing elements
  - Estimate learning time
  - Set milestones
  ↓
[Skill Progression]
  - Distribute skills across timeline
  - Set proficiency levels
  - Create monthly targets
  ↓
Output: Future Profile
  {
    ideal_state: {},
    missing_elements: {},
    milestones: [],
    monthly_targets: [],
    success_probability: 85%
  }
```

### 5. **Interview Arena** (interview_arena.py)
```
Input: Target Role + Interview Type
  ↓
[Generate Questions]
  - Technical questions with key points
  - Behavioral questions (STAR method)
  - Role-specific questions
  - Company-specific questions
  ↓
[Prepare Resources]
  - Difficulty levels
  - Time estimates
  - Preparation tips
  - Learning resources
  ↓
[Answer Evaluation]
  Input: User Answer
  - Check against key points
  - Assess depth
  - Evaluate structure
  - Generate feedback
  Output: Score + Feedback
  ↓
Output: Interview Preparation Package
```

## Data Flow Diagram

```
User Uploads Resume
        ↓
[Resume Parser] → Extract Data
        ↓
        ├─→ Store in Database
        │
        └─→ Session State (in-memory)
            ↓
    ┌───────┴────────────────┬─────────────────┐
    ↓                        ↓                  ↓
[Health Score]      [Foundry IQ Analysis]  [Career Twin]
    ↓                        ↓                  ↓
Display Profile      Multi-Step Reasoning   Future Profile
    ↓                        ↓                  ↓
    ├──────────────────────┬─┴──────────────┬──┴────────────┐
    ↓                      ↓                ↓               ↓
Company Readiness   Career GPS Plan   Opportunity Radar  Action Plan
```

## Knowledge Base Structure

### companies.json
```json
{
  "Microsoft": {
    "name": "Microsoft",
    "industry": "Cloud & Software",
    "popular_roles": ["Software Engineer", "Cloud Engineer"],
    "key_competencies": ["Problem Solving", "System Design"],
    "required_skills": ["C++", "Python", "Azure"],
    "hiring_process": ["Online Assessment", "Technical Interviews"],
    "interview_tips": [],
    "application_tips": []
  },
  ... (5+ more companies)
}
```

### roles.json
```json
{
  "AI Engineer": {
    "role_id": "ai_engineer",
    "title": "AI Engineer",
    "core_skills": ["Python", "TensorFlow", "Deep Learning"],
    "tools_required": ["Python", "Jupyter", "Docker"],
    "certifications": ["TensorFlow Developer", "AWS ML Specialty"],
    "key_projects": ["NLP models", "Computer Vision apps"],
    "interview_focus": ["ML algorithms", "Deep learning"]
  },
  ... (7+ more roles)
}
```

### opportunities.json
```json
{
  "certifications": [
    {
      "id": "aws_solutions_architect",
      "name": "AWS Solutions Architect Associate",
      "provider": "Amazon",
      "duration_weeks": 8,
      "cost": 150,
      "difficulty": "Intermediate"
    }
  ],
  "projects": [...],
  "internships": [...]
}
```

## Database Schema

```sql
users
├── id (PK)
├── user_id (UNIQUE)
├── name
├── email (UNIQUE)
├── created_at
└── updated_at

resumes
├── id (PK)
├── user_id (FK)
├── filename
├── file_path
├── extracted_data (JSON)
└── uploaded_at

career_profiles
├── id (PK)
├── user_id (FK, UNIQUE)
├── current_profile (JSON)
├── career_goals (JSON)
├── skill_gaps (JSON)
├── readiness_scores (JSON)
├── created_at
└── updated_at

assessments
├── id (PK)
├── user_id (FK)
├── assessment_type (ENUM)
├── company_name
├── role_name
├── readiness_score
├── missing_skills (JSON)
├── recommendations (JSON)
└── assessment_date

action_plans
├── id (PK)
├── user_id (FK)
├── plan_type
├── duration_days
├── milestones (JSON)
└── created_at

reasoning_traces
├── id (PK)
├── user_id (FK)
├── feature_name
├── reasoning_steps (JSON)
├── citations (JSON)
└── created_at
```

## Reasoning Step Structure

```python
@dataclass
class ReasoningStep:
    step_number: int
    title: str
    description: str
    input_data: Dict[str, Any]
    output_data: Dict[str, Any]
    citations: List[str]  # Sources from knowledge base
    confidence: float  # 0-1 scale
```

## Design Patterns Used

1. **Singleton Pattern**: KnowledgeBaseManager, SessionManager
2. **Factory Pattern**: FoundryIQEngine creates analysis instances
3. **Strategy Pattern**: Different scoring strategies for each category
4. **MVC Pattern**: Streamlit pages as views, modules as models/controllers
5. **Repository Pattern**: Database layer abstraction

## Performance Considerations

- Knowledge base cached in memory (lazy loading)
- Database queries optimized with indices
- Async PDF processing (future enhancement)
- Streaming responses for long operations
- Session state caching

## Security

- No sensitive data in logs
- Local database by default
- Optional encryption support
- Input validation on all forms
- SQL injection prevention (parameterized queries)

## Scalability

- Horizontal scaling via database replication
- Knowledge base versioning support
- Multi-user session management
- Stateless API design (future)
- Cache invalidation strategy

---

**Last Updated**: 2024

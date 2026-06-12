# 📋 TECHNICAL SPECIFICATION - JobPilot IQ X

## Document Information
- **Project**: JobPilot IQ X - AI Career Command Center
- **Version**: 1.0 Production
- **Status**: Ready for Deployment
- **Last Updated**: 2024
- **Framework**: Streamlit + Python

## 1. System Overview

JobPilot IQ X is a comprehensive career intelligence platform implementing Foundry IQ principles for multi-step reasoning, grounded recommendations, and transparent decision-making.

### 1.1 Core Value Proposition
- Solve career confusion through AI-powered intelligence
- Provide actionable, personalized guidance
- Show reasoning behind recommendations
- Help users make informed career decisions

### 1.2 Target Users
- **Students**: College students preparing for employment
- **Freshers**: Recent graduates without experience
- **Career Switchers**: Professionals changing careers
- **Job Seekers**: Early professionals seeking better roles

## 2. Functional Requirements

### 2.1 Resume Processing
- **REQ-001**: Accept PDF resume uploads
- **REQ-002**: Extract 8+ resume sections automatically
- **REQ-003**: Validate extracted data quality
- **REQ-004**: Store extracted data in database
- **REQ-005**: Support resume updates/replacement

### 2.2 Career Health Analysis
- **REQ-006**: Calculate 6-category health score
- **REQ-007**: Generate 0-100 composite score
- **REQ-008**: Provide category breakdowns
- **REQ-009**: Identify strengths and weaknesses
- **REQ-010**: Generate actionable recommendations

### 2.3 Foundry IQ Analysis
- **REQ-011**: Implement 6-9 step reasoning chains
- **REQ-012**: Track citations for each step
- **REQ-013**: Show confidence scores (0-100)
- **REQ-014**: Display complete reasoning trace
- **REQ-015**: Enable reasoning trace download

### 2.4 Company Readiness
- **REQ-016**: Support 6+ company analysis
- **REQ-017**: Calculate multi-factor readiness score
- **REQ-018**: Provide interview preparation
- **REQ-019**: Generate company-specific tips
- **REQ-020**: Show missing requirements

### 2.5 Career Intelligence
- **REQ-021**: Generate career twin profiles
- **REQ-022**: Create 30/60/90 day roadmaps
- **REQ-023**: Rank opportunities by relevance
- **REQ-024**: Provide interview preparation
- **REQ-025**: Generate action plans

## 3. Non-Functional Requirements

### 3.1 Performance
- **NFREQ-001**: Page load < 2 seconds
- **NFREQ-002**: Analysis generation < 10 seconds
- **NFREQ-003**: Database queries < 500ms
- **NFREQ-004**: Support 100+ concurrent users
- **NFREQ-005**: Cache knowledge base in memory

### 3.2 Reliability
- **NFREQ-006**: 99%+ uptime target
- **NFREQ-007**: Automatic error recovery
- **NFREQ-008**: Data persistence guaranteed
- **NFREQ-009**: No data loss
- **NFREQ-010**: Graceful degradation

### 3.3 Security
- **NFREQ-011**: Local-first architecture
- **NFREQ-012**: No unauthorized data access
- **NFREQ-013**: Input validation on all forms
- **NFREQ-014**: SQL injection prevention
- **NFREQ-015**: Secure session management

### 3.4 Scalability
- **NFREQ-016**: Horizontal scaling ready
- **NFREQ-017**: Database replication support
- **NFREQ-018**: Multi-instance deployment
- **NFREQ-019**: Load balancer compatible
- **NFREQ-020**: Stateless API design (future)

### 3.5 Maintainability
- **NFREQ-021**: Code documentation (docstrings)
- **NFREQ-022**: Architecture documentation
- **NFREQ-023**: API documentation
- **NFREQ-024**: Deployment guides
- **NFREQ-025**: Troubleshooting guides

## 4. System Architecture

### 4.1 Technology Stack
```
Frontend:      Streamlit 1.28+
Backend:       Python 3.8+
Database:      SQLite 3
Charts:        Plotly 5.17+
PDF Processing: PyPDF2 3.0+
Deployment:    Docker, Streamlit Cloud, AWS, Heroku, Azure
```

### 4.2 Core Modules
1. **resume_parser.py** (200 lines)
   - PDF text extraction
   - Pattern-based data extraction
   - Data normalization
   - Validation

2. **career_health.py** (300 lines)
   - 6-category scoring
   - Weight calculation
   - Strength/weakness identification
   - Recommendation generation

3. **foundry_iq.py** (500 lines) ⭐
   - Multi-step reasoning engine
   - Citation tracking
   - Confidence scoring
   - Reasoning trace generation
   - 5 analysis types

4. **career_agents.py** (400 lines)
   - Career Twin agent
   - Career GPS agent
   - Profile generation
   - Roadmap creation
   - Timeline management

5. **interview_arena.py** (300 lines)
   - Question generation
   - Answer evaluation
   - Feedback generation
   - Resource curation

### 4.3 Database Design
- **7 tables**: users, resumes, profiles, assessments, action_plans, opportunities, reasoning_traces
- **Normalized schema**: No data redundancy
- **Foreign keys**: Referential integrity
- **Indices**: Optimized queries
- **JSON columns**: Flexible data storage

## 5. User Interface

### 5.1 Pages (10 Total)
1. **Dashboard** - Overview and KPIs
2. **Resume Analyzer** - Upload and extract
3. **Career Twin** - Future profile
4. **Company Readiness** - Company analysis
5. **Career GPS** - Roadmaps (30/60/90)
6. **Opportunity Radar** - Ranked opportunities
7. **Interview Arena** - Q&A preparation
8. **Action Plan** - Prioritized tasks
9. **Shortlist Analyzer** - Hero feature
10. **Settings** - User preferences

### 5.2 Design System
- **Color Scheme**: Dark theme (professional)
- **Primary**: Cyan #00D9FF
- **Secondary**: Magenta #FF006E
- **Accent**: Gold #FFD60A
- **Style**: Glassmorphism
- **Responsive**: Mobile-friendly grid

### 5.3 Components
- Metric cards
- Progress bars
- Gauge charts
- Radar charts
- Bar charts
- Expandable sections
- Modal dialogs
- File uploads
- Text inputs
- Sliders
- Multiselects

## 6. Data Models

### 6.1 Resume Data
```json
{
  "personal_info": {
    "email": "",
    "phone": "",
    "linkedin": "",
    "github": ""
  },
  "skills": [],
  "projects": [
    {"title": "", "description": ""}
  ],
  "experience": [
    {"title": "", "keyword": ""}
  ],
  "certifications": [],
  "education": [
    {"degree": "", "context": ""}
  ],
  "summary": ""
}
```

### 6.2 Health Score
```json
{
  "overall_score": 75,
  "grade": "B",
  "category_scores": {
    "technical_skills": {"score": 80, "details": {}},
    "projects_portfolio": {"score": 70, "details": {}},
    "certifications": {"score": 60, "details": {}},
    "experience": {"score": 80, "details": {}},
    "communication": {"score": 75, "details": {}},
    "readiness": {"score": 70, "details": {}}
  },
  "strengths": [],
  "weaknesses": [],
  "recommendations": []
}
```

### 6.3 Reasoning Step
```json
{
  "step_number": 1,
  "title": "Parse User Profile",
  "description": "Extract and normalize user skills",
  "input_data": {},
  "output_data": {},
  "citations": [],
  "confidence": 0.95
}
```

## 7. API Endpoints (Future REST API)

### 7.1 Resume Endpoints
- `POST /api/resumes/upload` - Upload resume
- `GET /api/resumes/{id}` - Get resume
- `DELETE /api/resumes/{id}` - Delete resume

### 7.2 Analysis Endpoints
- `POST /api/health-score` - Calculate health
- `POST /api/company-readiness/{company}` - Company analysis
- `POST /api/skill-gaps/{role}` - Skill analysis
- `POST /api/shortlist-analysis` - Shortlist analysis

### 7.3 Recommendation Endpoints
- `GET /api/opportunities` - Get opportunities
- `GET /api/roadmap/{duration}` - Get roadmap
- `GET /api/action-plan` - Get action plan

## 8. Knowledge Base

### 8.1 Companies (companies.json)
- **Count**: 6+ companies
- **Data per company**: 15+ fields
- **Fields**: industry, hiring_process, key_competencies, required_skills, certifications, salary_range, tips

### 8.2 Roles (roles.json)
- **Count**: 8+ job roles
- **Data per role**: 12+ fields
- **Fields**: core_skills, tools, certifications, experience, growth_path, interview_focus

### 8.3 Opportunities (opportunities.json)
- **Count**: 100+ items
- **Types**: certifications, projects, internships
- **Data per item**: 8+ fields

## 9. Deployment Specifications

### 9.1 Local Deployment
- Python 3.8+ required
- Virtual environment support
- ~2 minutes setup time
- 500MB disk space

### 9.2 Cloud Deployment
- **Streamlit Cloud**: 1-click deploy
- **Docker**: Multi-platform
- **Heroku**: Easy CD/CI
- **AWS**: EC2, Lightsail, ECS, Lambda
- **Google Cloud**: Cloud Run
- **Azure**: App Service

### 9.3 Resource Requirements
- **CPU**: 0.5-1 vCPU minimum
- **Memory**: 512MB-1GB minimum
- **Storage**: 1GB (with data)
- **Bandwidth**: Minimal (mostly local)

## 10. Testing Strategy

### 10.1 Unit Tests
- Resume parser accuracy
- Score calculation correctness
- Reasoning logic validation
- Database operations

### 10.2 Integration Tests
- End-to-end workflows
- Data flow verification
- API response validation

### 10.3 User Acceptance Tests
- UI/UX testing
- Feature validation
- Performance benchmarks

## 11. Maintenance Plan

### 11.1 Regular Maintenance
- **Weekly**: Log monitoring, backup verification
- **Monthly**: Dependency updates, security patches
- **Quarterly**: Performance optimization, KB updates

### 11.2 Monitoring
- Application performance metrics
- Error rate tracking
- User analytics
- Server health

### 11.3 Backup & Recovery
- Daily database backups
- Transaction logs
- Point-in-time recovery

## 12. Security Considerations

### 12.1 Data Security
- Local processing by default
- Optional encryption at rest
- Secure credential management
- Input validation and sanitization

### 12.2 Access Control
- Session management
- User authentication (future)
- Role-based access (future)

### 12.3 Compliance
- GDPR ready (local-first)
- Data deletion support
- Privacy policy compliance
- No third-party data sharing

## 13. Performance Metrics

### 13.1 Speed Targets
- Page load: < 2 seconds
- Analysis: < 10 seconds
- Database: < 500ms
- Chart rendering: < 1 second

### 13.2 Scalability
- 100+ concurrent users
- 10,000+ total users (with optimization)
- Horizontal scaling ready
- Load balanced deployment

## 14. Future Enhancements

### 14.1 Phase 2
- REST API
- User authentication
- LinkedIn import
- Job board integration

### 14.2 Phase 3
- Mobile app
- AI chat
- Community features
- Mentor matching

### 14.3 Phase 4
- Real-time collaboration
- Advanced analytics
- Machine learning models
- API marketplace

## 15. Success Criteria

- ✅ All 10 features implemented
- ✅ All 8 Foundry IQ principles applied
- ✅ 3000+ lines of code
- ✅ 100% knowledge base coverage
- ✅ Production deployment ready
- ✅ Comprehensive documentation
- ✅ 6+ companies, 8+ roles
- ✅ Multi-step reasoning (6-9 steps)
- ✅ Professional UI/UX
- ✅ Hackathon-ready demo

---

**Specification Version**: 1.0  
**Status**: Approved for Implementation  
**Next Review**: 2024-Q2

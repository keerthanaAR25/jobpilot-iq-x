"""
Utilities for JobPilot IQ X
Knowledge base loading, session management, and helper functions
"""
import json
from pathlib import Path
from typing import Dict, Any, Optional
from config.config import KNOWLEDGE_BASE_DIR, PROJECT_ROOT

class KnowledgeBaseManager:
    """Load and manage knowledge base files"""
    
    _instance = None
    _kb_cache = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.kb_dir = KNOWLEDGE_BASE_DIR
    
    def load_companies(self) -> Dict[str, Any]:
        """Load companies knowledge base"""
        if 'companies' not in self._kb_cache:
            file_path = self.kb_dir / 'companies.json'
            if file_path.exists():
                with open(file_path, 'r') as f:
                    self._kb_cache['companies'] = json.load(f)
            else:
                self._kb_cache['companies'] = {}
        return self._kb_cache['companies']
    
    def load_roles(self) -> Dict[str, Any]:
        """Load roles knowledge base"""
        if 'roles' not in self._kb_cache:
            file_path = self.kb_dir / 'roles.json'
            if file_path.exists():
                with open(file_path, 'r') as f:
                    self._kb_cache['roles'] = json.load(f)
            else:
                self._kb_cache['roles'] = {}
        return self._kb_cache['roles']
    
    def load_opportunities(self) -> Dict[str, Any]:
        """Load opportunities knowledge base"""
        if 'opportunities' not in self._kb_cache:
            file_path = self.kb_dir / 'opportunities.json'
            if file_path.exists():
                with open(file_path, 'r') as f:
                    self._kb_cache['opportunities'] = json.load(f)
            else:
                self._kb_cache['opportunities'] = {}
        return self._kb_cache['opportunities']
    
    def get_all_companies(self) -> list:
        """Get list of all companies"""
        return list(self.load_companies().keys())
    
    def get_all_roles(self) -> list:
        """Get list of all roles"""
        return list(self.load_roles().keys())
    
    def get_company_info(self, company_name: str) -> Optional[Dict[str, Any]]:
        """Get specific company information"""
        companies = self.load_companies()
        return companies.get(company_name)
    
    def get_role_info(self, role_name: str) -> Optional[Dict[str, Any]]:
        """Get specific role information"""
        roles = self.load_roles()
        return roles.get(role_name)

class SessionManager:
    """Manage user session state"""
    
    def __init__(self):
        self.sessions = {}
    
    def create_session(self, user_id: str, user_name: str = "Guest") -> Dict[str, Any]:
        """Create new user session"""
        session = {
            'user_id': user_id,
            'user_name': user_name,
            'profile': None,
            'resume_data': None,
            'health_score': None,
            'assessments': {},
            'recommendations': {},
            'action_plans': {}
        }
        self.sessions[user_id] = session
        return session
    
    def get_session(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user session"""
        return self.sessions.get(user_id)
    
    def update_session(self, user_id: str, key: str, value: Any):
        """Update session data"""
        if user_id in self.sessions:
            self.sessions[user_id][key] = value

class UIHelper:
    """UI helper functions for Streamlit"""
    
    @staticmethod
    def format_score(score: float) -> str:
        """Format score with emoji"""
        if score >= 90:
            return f"🌟 {score}%"
        elif score >= 80:
            return f"⭐ {score}%"
        elif score >= 70:
            return f"👍 {score}%"
        elif score >= 60:
            return f"📈 {score}%"
        else:
            return f"📊 {score}%"
    
    @staticmethod
    def format_readiness(score: int) -> str:
        """Format readiness status"""
        if score >= 80:
            return "🟢 Excellent Readiness"
        elif score >= 60:
            return "🟡 Good Readiness"
        elif score >= 40:
            return "🟠 Average Readiness"
        else:
            return "🔴 Needs Improvement"
    
    @staticmethod
    def create_metric_card(title: str, value: str, help_text: str = "") -> Dict:
        """Create metric card data"""
        return {
            'title': title,
            'value': value,
            'help': help_text
        }
    
    @staticmethod
    def format_reasoning_step(step: Dict) -> str:
        """Format reasoning step for display"""
        return f"""
        **Step {step['step_number']}: {step['title']}**
        
        {step['description']}
        
        📊 Confidence: {step.get('confidence', 'N/A')}
        
        Citations: {', '.join(step.get('citations', ['N/A']))}
        """

class ReportGenerator:
    """Generate reports and summaries"""
    
    @staticmethod
    def generate_career_health_report(health_score: Dict) -> str:
        """Generate career health report"""
        report = f"""
        # Career Health Report
        
        ## Overall Score: {health_score['overall_score']}/100 ({health_score['grade']})
        
        ### Category Breakdown:
        """
        
        for category, scores in health_score.get('category_scores', {}).items():
            report += f"\n- **{category.replace('_', ' ').title()}**: {scores['score']}/100"
        
        report += f"\n\n### Strengths:\n"
        for strength in health_score.get('strengths', []):
            report += f"- ✅ {strength}\n"
        
        report += f"\n### Areas for Improvement:\n"
        for weakness in health_score.get('weaknesses', []):
            report += f"- ⚠️ {weakness}\n"
        
        report += f"\n### Recommendations:\n"
        for rec in health_score.get('recommendations', []):
            report += f"- {rec}\n"
        
        return report
    
    @staticmethod
    def generate_shortlist_analysis_report(analysis: Dict) -> str:
        """Generate shortlist analysis report"""
        report = f"""
        # Why Am I Not Getting Shortlisted? - Analysis Report
        
        ## Shortlist Success Score: {analysis.get('shortlist_score', 0)}/100
        
        ### Main Issues Identified:
        """
        
        for issue in analysis.get('main_issues', [])[:5]:
            report += f"\n- 🔴 {issue}"
        
        report += f"\n\n### Profile Completeness: {analysis.get('profile_completeness', 0)}/100\n"
        
        report += f"\n### Critical Skill Gaps:\n"
        for gap in analysis.get('skill_gaps', [])[:5]:
            report += f"- 📚 {gap}\n"
        
        report += f"\n### Immediate Actions (Next 7 Days):\n"
        for action in analysis.get('immediate_actions', [])[:3]:
            report += f"- ✅ {action}\n"
        
        report += f"\n### Long-term Improvements (30-90 Days):\n"
        for improvement in analysis.get('long_term_improvements', [])[:3]:
            report += f"- 🎯 {improvement}\n"
        
        return report

class FileManager:
    """Manage file operations"""
    
    @staticmethod
    def save_json(data: Dict, file_path: str):
        """Save data to JSON file"""
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    @staticmethod
    def load_json(file_path: str) -> Dict:
        """Load data from JSON file"""
        if Path(file_path).exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}
    
    @staticmethod
    def create_backup(file_path: str):
        """Create backup of file"""
        import shutil
        from datetime import datetime
        
        if Path(file_path).exists():
            backup_path = f"{file_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            shutil.copy(file_path, backup_path)
            return backup_path
        return None

# Singleton instances
kb_manager = KnowledgeBaseManager()
session_manager = SessionManager()
ui_helper = UIHelper()
report_generator = ReportGenerator()
file_manager = FileManager()

"""
Career Health Engine - Calculates career readiness scores
"""
from typing import Dict, Any, Tuple, List
import json

class CareerHealthEngine:
    """Calculate comprehensive career health score"""
    
    def __init__(self):
        self.categories = {
            'technical_skills': {'weight': 0.25, 'description': 'Technical Skills'},
            'projects_portfolio': {'weight': 0.20, 'description': 'Projects & Portfolio'},
            'certifications': {'weight': 0.15, 'description': 'Certifications'},
            'experience': {'weight': 0.20, 'description': 'Experience'},
            'communication': {'weight': 0.10, 'description': 'Communication'},
            'readiness': {'weight': 0.10, 'description': 'Career Readiness'}
        }
    
    def calculate_health_score(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate overall career health score
        
        Args:
            profile: User profile with resume data
        
        Returns:
            Dictionary with health scores and breakdown
        """
        scores = {}
        total_score = 0
        
        # Calculate individual category scores
        scores['technical_skills'] = self._calculate_technical_skills_score(profile)
        scores['projects_portfolio'] = self._calculate_projects_score(profile)
        scores['certifications'] = self._calculate_certifications_score(profile)
        scores['experience'] = self._calculate_experience_score(profile)
        scores['communication'] = self._calculate_communication_score(profile)
        scores['readiness'] = self._calculate_readiness_score(profile)
        
        # Calculate weighted total
        for category, score_data in scores.items():
            weight = self.categories[category]['weight']
            total_score += score_data['score'] * weight
        
        # Determine grade
        grade = self._get_grade(total_score)
        
        return {
            'overall_score': round(total_score, 2),
            'grade': grade,
            'category_scores': scores,
            'strengths': self._identify_strengths(scores),
            'weaknesses': self._identify_weaknesses(scores),
            'recommendations': self._generate_recommendations(scores)
        }
    
    def _calculate_technical_skills_score(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate technical skills score"""
        skills = profile.get('skills', [])
        
        # Define skill tiers
        high_value_skills = [
            'Python', 'Java', 'C++', 'JavaScript', 'SQL',
            'TensorFlow', 'PyTorch', 'AWS', 'Azure', 'GCP',
            'Kubernetes', 'Docker'
        ]
        
        medium_value_skills = [
            'React', 'Node.js', 'Django', 'Flask', 'MongoDB',
            'Git', 'Linux', 'REST API'
        ]
        
        high_skill_count = sum(1 for s in skills if s in high_value_skills)
        medium_skill_count = sum(1 for s in skills if s in medium_value_skills)
        
        score = min(100, (high_skill_count * 10) + (medium_skill_count * 5))
        
        return {
            'score': score,
            'details': {
                'total_skills': len(skills),
                'high_value_skills': high_skill_count,
                'skills_list': skills
            }
        }
    
    def _calculate_projects_score(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate projects and portfolio score"""
        projects = profile.get('projects', [])
        
        # Base score for having projects
        base_score = min(100, len(projects) * 20)
        
        # Bonus for specific project types
        bonus = 0
        for project in projects:
            title = str(project.get('title', '')).lower()
            if any(keyword in title for keyword in ['ml', 'ai', 'data', 'cloud', 'full stack']):
                bonus += 10
        
        score = min(100, base_score + bonus)
        
        return {
            'score': score,
            'details': {
                'project_count': len(projects),
                'projects': projects
            }
        }
    
    def _calculate_certifications_score(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate certifications score"""
        certifications = profile.get('certifications', [])
        
        # High-value certification keywords
        premium_certs = ['AWS', 'Azure', 'Google Cloud', 'Kubernetes', 'TensorFlow']
        
        base_score = min(100, len(certifications) * 15)
        
        premium_count = sum(1 for cert in certifications 
                          if any(kw.lower() in cert.lower() for kw in premium_certs))
        bonus = premium_count * 15
        
        score = min(100, base_score + bonus)
        
        return {
            'score': score,
            'details': {
                'total_certifications': len(certifications),
                'premium_certifications': premium_count,
                'certifications': certifications
            }
        }
    
    def _calculate_experience_score(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate experience score"""
        experience = profile.get('experience', [])
        
        # Score based on experience entries
        base_score = min(100, len(experience) * 15)
        
        # Check for relevant roles
        relevant_keywords = ['Engineer', 'Developer', 'Analyst', 'Architect']
        relevant_count = sum(1 for exp in experience 
                           if any(kw.lower() in str(exp.get('title', '')).lower() for kw in relevant_keywords))
        
        bonus = relevant_count * 10
        score = min(100, base_score + bonus)
        
        return {
            'score': score,
            'details': {
                'experience_count': len(experience),
                'relevant_positions': relevant_count,
                'experience': experience
            }
        }
    
    def _calculate_communication_score(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate communication score"""
        # Check resume quality
        summary = profile.get('summary', '')
        personal_info = profile.get('personal_info', {})
        
        score = 50  # Base score
        
        # Bonus for having contacts
        if personal_info.get('linkedin'):
            score += 15
        if personal_info.get('github'):
            score += 15
        if personal_info.get('email'):
            score += 10
        
        # Bonus for having summary
        if summary and len(summary) > 50:
            score += 10
        
        score = min(100, score)
        
        return {
            'score': score,
            'details': {
                'has_summary': bool(summary),
                'contacts_provided': len(personal_info),
                'communication_indicators': {
                    'linkedin': bool(personal_info.get('linkedin')),
                    'github': bool(personal_info.get('github')),
                    'email': bool(personal_info.get('email'))
                }
            }
        }
    
    def _calculate_readiness_score(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate overall career readiness"""
        score = 50  # Base score
        
        # Add points for completeness
        if profile.get('education'):
            score += 15
        if profile.get('projects'):
            score += 15
        if profile.get('skills'):
            score += 15
        if profile.get('personal_info'):
            score += 5
        
        score = min(100, score)
        
        return {
            'score': score,
            'details': {
                'profile_completeness': {
                    'has_education': bool(profile.get('education')),
                    'has_projects': bool(profile.get('projects')),
                    'has_skills': bool(profile.get('skills')),
                    'has_experience': bool(profile.get('experience'))
                }
            }
        }
    
    def _get_grade(self, score: float) -> str:
        """Determine letter grade from score"""
        if score >= 90:
            return "A+ (Excellent)"
        elif score >= 80:
            return "A (Very Good)"
        elif score >= 70:
            return "B (Good)"
        elif score >= 60:
            return "C (Average)"
        elif score >= 50:
            return "D (Below Average)"
        else:
            return "F (Needs Improvement)"
    
    def _identify_strengths(self, scores: Dict[str, Any]) -> List[str]:
        """Identify profile strengths"""
        strengths = []
        for category, score_data in scores.items():
            if score_data['score'] >= 75:
                strengths.append(self.categories[category]['description'])
        return strengths
    
    def _identify_weaknesses(self, scores: Dict[str, Any]) -> List[str]:
        """Identify profile weaknesses"""
        weaknesses = []
        for category, score_data in scores.items():
            if score_data['score'] < 60:
                weaknesses.append(self.categories[category]['description'])
        return weaknesses
    
    def _generate_recommendations(self, scores: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        if scores['technical_skills']['score'] < 70:
            recommendations.append("📚 Improve technical skills - Learn popular frameworks and languages")
        
        if scores['projects_portfolio']['score'] < 70:
            recommendations.append("💻 Build portfolio projects - Create 2-3 substantial projects")
        
        if scores['certifications']['score'] < 70:
            recommendations.append("📜 Pursue industry certifications - Complete 1-2 recognized certs")
        
        if scores['experience']['score'] < 70:
            recommendations.append("🏢 Gain practical experience - Look for internships or freelance work")
        
        if scores['communication']['score'] < 70:
            recommendations.append("🤝 Improve communication - Update LinkedIn and create GitHub portfolio")
        
        return recommendations if recommendations else ["✅ Great profile! Keep building and learning"]

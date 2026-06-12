"""
Career Twin & Career GPS Agents
Generates future career profiles and personalized roadmaps
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta
import json

class CareerTwinAgent:
    """Generate AI Career Twin - future version of user"""
    
    def generate_career_twin(self, user_profile: Dict[str, Any], 
                           target_role: str, timeline_months: int = 12) -> Dict[str, Any]:
        """
        Create a future career profile
        
        Args:
            user_profile: Current user profile
            target_role: Target career role
            timeline_months: Timeline for reaching the twin profile
        
        Returns:
            Future career profile
        """
        
        # Define ideal profile for role
        ideal_profile = {
            "AI Engineer": {
                "skills": ["Python", "TensorFlow", "PyTorch", "Deep Learning", "NLP", "Computer Vision",
                          "Transformers", "MLOps", "Kubernetes", "AWS ML"],
                "certifications": ["TensorFlow Developer", "AWS ML Specialty", "Google Cloud ML"],
                "projects": 4,
                "experience_years": 3,
                "github_repos": 5,
                "publications": 2,
                "community_contributions": True
            },
            "Data Scientist": {
                "skills": ["Python", "SQL", "Statistics", "ML", "Data Visualization", "R", "Spark",
                          "A/B Testing", "Power BI", "Tableau"],
                "certifications": ["Google Data Analytics", "IBM Data Science", "Azure Data Scientist"],
                "projects": 3,
                "experience_years": 2,
                "github_repos": 4,
                "publications": 1,
                "blog_posts": 5
            },
            "Cloud Engineer": {
                "skills": ["AWS", "GCP", "Azure", "Kubernetes", "Docker", "Terraform", "Python",
                          "Infrastructure as Code", "DevOps", "Security"],
                "certifications": ["AWS Solutions Architect", "GCP Professional", "Kubernetes CKA"],
                "projects": 4,
                "experience_years": 3,
                "github_repos": 5,
                "certifications_count": 3
            }
        }
        
        ideal = ideal_profile.get(target_role, ideal_profile["Software Engineer"])
        
        # Calculate gaps
        current_skills = set(user_profile.get('skills', []))
        ideal_skills = set(ideal['skills'])
        missing_skills = ideal_skills - current_skills
        
        # Generate twin profile
        twin_profile = {
            "current_role": user_profile.get('current_role', 'Student/Fresher'),
            "target_role": target_role,
            "timeline_months": timeline_months,
            "target_date": (datetime.now() + timedelta(days=timeline_months * 30)).strftime("%Y-%m-%d"),
            
            "ideal_future_state": {
                "skills": ideal['skills'],
                "certifications": ideal.get('certifications', []),
                "projects": ideal.get('projects', 3),
                "experience_years": ideal.get('experience_years', 2),
                "github_presence": True,
                "portfolio_strength": "Strong",
                "salary_expectation": self._estimate_salary(target_role, ideal.get('experience_years', 2))
            },
            
            "skill_progression": self._generate_skill_progression(
                current_skills, ideal_skills, timeline_months
            ),
            
            "missing_elements": {
                "skills": list(missing_skills),
                "certifications": list(set(ideal.get('certifications', [])) - set(user_profile.get('certifications', []))),
                "projects": ideal.get('projects', 3) - len(user_profile.get('projects', [])),
                "experience_gap": ideal.get('experience_years', 2) - len(user_profile.get('experience', [])) // 12
            },
            
            "milestone_checkpoints": self._generate_milestones(timeline_months, target_role),
            
            "monthly_targets": self._generate_monthly_targets(timeline_months, missing_skills),
            
            "estimated_success_rate": self._calculate_success_probability(user_profile, target_role)
        }
        
        return twin_profile
    
    def _generate_skill_progression(self, current: set, ideal: set, months: int) -> List[Dict]:
        """Generate skill progression timeline"""
        missing = list(ideal - current)
        progression = []
        
        # Distribute skills across timeline
        skills_per_month = max(1, len(missing) // (months // 3))
        
        for i, skill in enumerate(missing):
            month = (i // skills_per_month) + 1
            if month <= months:
                progression.append({
                    'skill': skill,
                    'target_month': min(month, months),
                    'proficiency_level': 'Intermediate' if month <= months // 2 else 'Advanced'
                })
        
        return progression
    
    def _generate_milestones(self, months: int, role: str) -> List[Dict]:
        """Generate milestone checkpoints"""
        return [
            {
                'month': 3,
                'milestone': f'Complete foundation skills for {role}',
                'deliverables': ['Learn 3-4 core skills', 'Build 1 portfolio project']
            },
            {
                'month': 6,
                'milestone': 'Acquire industry certifications',
                'deliverables': ['Earn 1-2 relevant certifications', 'Build 2nd project']
            },
            {
                'month': 9,
                'milestone': 'Advanced skills and networking',
                'deliverables': ['Master advanced topics', 'Contribute to open source', 'Network with professionals']
            },
            {
                'month': 12,
                'milestone': 'Job-ready profile',
                'deliverables': ['Complete portfolio', 'Mock interviews', 'Start applying to roles']
            }
        ]
    
    def _generate_monthly_targets(self, months: int, missing_skills: set) -> List[Dict]:
        """Generate monthly action targets"""
        targets = []
        skills_list = list(missing_skills)
        
        for month in range(1, min(months + 1, 4)):  # First 3 months detailed
            targets.append({
                'month': month,
                'skill_focus': skills_list[month - 1] if month - 1 < len(skills_list) else None,
                'actions': [
                    f'Learn and practice {skills_list[month - 1]}' if month - 1 < len(skills_list) else 'Continue learning',
                    'Complete 1 online course module',
                    'Build a mini-project',
                    'Daily coding practice (1-2 hours)',
                    'Join community/hackathon'
                ]
            })
        
        return targets
    
    def _estimate_salary(self, role: str, experience_years: int) -> str:
        """Estimate salary range"""
        salary_ranges = {
            "AI Engineer": {"entry": "100k-130k", "mid": "150k-200k", "senior": "250k+"},
            "Data Scientist": {"entry": "90k-120k", "mid": "140k-180k", "senior": "220k+"},
            "Cloud Engineer": {"entry": "100k-140k", "mid": "160k-210k", "senior": "260k+"}
        }
        
        ranges = salary_ranges.get(role, {"entry": "80k-100k", "mid": "120k-160k", "senior": "200k+"})
        
        if experience_years < 2:
            return ranges['entry']
        elif experience_years < 5:
            return ranges['mid']
        else:
            return ranges['senior']
    
    def _calculate_success_probability(self, profile: Dict, role: str) -> float:
        """Calculate probability of reaching career twin in timeline"""
        score = 50.0
        
        if profile.get('skills'):
            score += min(20, len(profile['skills']) * 2)
        if profile.get('projects'):
            score += min(15, len(profile['projects']) * 5)
        if profile.get('certifications'):
            score += min(10, len(profile['certifications']) * 5)
        
        return min(100, score)

class CareerGPSAgent:
    """Career GPS - Generate personalized roadmaps"""
    
    def generate_career_roadmap(self, user_profile: Dict[str, Any], 
                               target_role: str, duration_days: int) -> Dict[str, Any]:
        """
        Generate personalized career roadmap
        
        Args:
            user_profile: Current user profile
            target_role: Target career role
            duration_days: 30, 60, or 90
        
        Returns:
            Detailed roadmap with milestones and learning paths
        """
        
        duration_type = f"{duration_days}_day"
        
        roadmap = {
            "duration_days": duration_days,
            "target_role": target_role,
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": (datetime.now() + timedelta(days=duration_days)).strftime("%Y-%m-%d"),
            
            "learning_path": self._generate_learning_path(target_role, duration_days),
            "weekly_milestones": self._generate_weekly_milestones(duration_days, target_role),
            "action_items": self._generate_action_items(duration_days, user_profile, target_role),
            "project_roadmap": self._generate_project_timeline(duration_days),
            "skill_development": self._generate_skill_schedule(duration_days, target_role),
            
            "success_metrics": self._define_success_metrics(duration_days),
            "resources": self._curate_resources(target_role),
            "community_involvement": self._generate_community_tasks(duration_days)
        }
        
        return roadmap
    
    def _generate_learning_path(self, role: str, days: int) -> List[Dict]:
        """Generate structured learning path"""
        weeks = days // 7
        
        return [
            {
                'week': 1,
                'focus': 'Fundamentals',
                'topics': ['Core concepts', 'Environment setup', 'Basic practice'],
                'hours_per_week': 15
            },
            {
                'week': 2,
                'focus': 'Intermediate skills',
                'topics': ['Advanced concepts', 'Project setup', 'Real-world scenarios'],
                'hours_per_week': 18
            },
            {
                'week': 3,
                'focus': 'Advanced implementation',
                'topics': ['System design', 'Best practices', 'Performance optimization'],
                'hours_per_week': 20
            }
        ][:weeks]
    
    def _generate_weekly_milestones(self, days: int, role: str) -> List[Dict]:
        """Generate weekly milestones"""
        weeks = days // 7
        milestones = []
        
        for week in range(1, min(weeks + 1, 14)):
            milestones.append({
                'week': week,
                'milestone': f'Week {week}: Complete {role} milestone {week}',
                'deliverables': ['Code submission', 'Documentation', 'Project checkpoint'],
                'review_date': (datetime.now() + timedelta(weeks=week)).strftime("%Y-%m-%d")
            })
        
        return milestones
    
    def _generate_action_items(self, days: int, profile: Dict, role: str) -> Dict:
        """Generate categorized action items"""
        return {
            'immediate': [
                '✅ Set up development environment',
                '✅ Join learning communities',
                '✅ Create GitHub portfolio',
                '✅ Define measurable goals'
            ],
            'weekly': [
                '📚 Complete 1 course module',
                '💻 Build feature/component',
                '🔍 Code review & optimization',
                '📝 Document learnings',
                '🤝 Join community standup'
            ],
            'monthly': [
                '🎯 Complete mini-project',
                '📊 Progress assessment',
                '🔗 Network with professionals',
                '💬 Share knowledge (blog/video)'
            ]
        }
    
    def _generate_project_timeline(self, days: int) -> List[Dict]:
        """Generate project milestones"""
        return [
            {
                'project_num': 1,
                'name': 'Beginner Project',
                'duration_weeks': 2,
                'difficulty': 'Beginner',
                'start_week': 1,
                'description': 'Fundamental concept implementation'
            },
            {
                'project_num': 2,
                'name': 'Intermediate Project',
                'duration_weeks': 3,
                'difficulty': 'Intermediate',
                'start_week': 3,
                'description': 'Real-world application'
            },
            {
                'project_num': 3,
                'name': 'Capstone Project',
                'duration_weeks': 4,
                'difficulty': 'Advanced',
                'start_week': 7,
                'description': 'Portfolio-worthy end-to-end project'
            }
        ]
    
    def _generate_skill_schedule(self, days: int, role: str) -> List[Dict]:
        """Generate skills to focus on each week"""
        return [
            {'week': 1, 'skills': ['Fundamentals', 'Setup']},
            {'week': 2, 'skills': ['Core concepts', 'Implementation']},
            {'week': 3, 'skills': ['Advanced techniques', 'Optimization']}
        ]
    
    def _define_success_metrics(self, days: int) -> List[str]:
        """Define success criteria"""
        return [
            f'✅ Complete all {days}-day milestones',
            f'✅ Build 1-2 portfolio projects',
            f'✅ Learn 3-5 critical skills',
            f'✅ Achieve 80%+ understanding of core concepts',
            f'✅ Get feedback from community',
            f'✅ Document entire learning journey'
        ]
    
    def _curate_resources(self, role: str) -> Dict:
        """Curate learning resources"""
        return {
            'courses': ['Udemy', 'Coursera', 'DataCamp', 'Pluralsight'],
            'platforms': ['LeetCode', 'HackerRank', 'Kaggle'],
            'communities': ['Reddit', 'Discord', 'Slack', 'GitHub'],
            'tools': ['VS Code', 'Jupyter', 'Google Colab', 'Git/GitHub']
        }
    
    def _generate_community_tasks(self, days: int) -> List[str]:
        """Generate community engagement tasks"""
        return [
            'Join relevant Slack/Discord communities',
            'Follow industry experts on social media',
            'Participate in weekly discussions',
            'Share your progress on Twitter/LinkedIn',
            'Attend online meetups/webinars',
            'Contribute to open source projects',
            'Mentor someone else'
        ]

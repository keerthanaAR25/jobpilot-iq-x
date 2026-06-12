"""
Interview Arena - Generate and evaluate interview questions
"""
from typing import Dict, Any, List
import json

class InterviewArena:
    """Generate interview questions and evaluate responses"""
    
    def generate_interview_questions(self, user_profile: Dict[str, Any], 
                                    target_role: str, 
                                    interview_type: str = "technical") -> Dict[str, Any]:
        """
        Generate interview questions for target role
        
        Args:
            user_profile: User's profile
            target_role: Target role
            interview_type: "technical", "behavioral", or "role_specific"
        
        Returns:
            Interview questions with difficulty levels
        """
        
        questions = {
            "technical": self._generate_technical_questions(target_role),
            "behavioral": self._generate_behavioral_questions(target_role),
            "role_specific": self._generate_role_questions(target_role),
            "company_specific": self._generate_company_questions(user_profile.get('target_companies', []))
        }
        
        return {
            "target_role": target_role,
            "interview_type": interview_type,
            "questions": questions.get(interview_type, questions["technical"]),
            "preparation_tips": self._get_preparation_tips(target_role, interview_type),
            "resources": self._get_interview_resources(target_role)
        }
    
    def _generate_technical_questions(self, role: str) -> List[Dict]:
        """Generate technical interview questions"""
        
        role_questions = {
            "AI Engineer": [
                {
                    "id": 1,
                    "question": "Explain the concept of backpropagation and how it's used in training neural networks.",
                    "difficulty": "Intermediate",
                    "topics": ["Deep Learning", "Neural Networks"],
                    "expected_duration_minutes": 5,
                    "key_points": [
                        "Gradient computation",
                        "Chain rule application",
                        "Weight updates",
                        "Common pitfalls"
                    ]
                },
                {
                    "id": 2,
                    "question": "What are transformers and how do they differ from RNNs?",
                    "difficulty": "Advanced",
                    "topics": ["NLP", "Architecture"],
                    "expected_duration_minutes": 7,
                    "key_points": [
                        "Attention mechanism",
                        "Positional encoding",
                        "Parallel processing",
                        "Use cases"
                    ]
                },
                {
                    "id": 3,
                    "question": "Design an ML pipeline from raw data to model deployment.",
                    "difficulty": "Advanced",
                    "topics": ["MLOps", "System Design"],
                    "expected_duration_minutes": 15,
                    "key_points": [
                        "Data preprocessing",
                        "Feature engineering",
                        "Model selection",
                        "Evaluation metrics",
                        "Deployment strategy"
                    ]
                }
            ],
            "Data Scientist": [
                {
                    "id": 1,
                    "question": "How do you handle imbalanced datasets?",
                    "difficulty": "Intermediate",
                    "topics": ["ML", "Data Handling"],
                    "expected_duration_minutes": 5,
                    "key_points": [
                        "Oversampling",
                        "Undersampling",
                        "SMOTE",
                        "Class weights"
                    ]
                },
                {
                    "id": 2,
                    "question": "Design an A/B testing experiment for a feature launch.",
                    "difficulty": "Intermediate",
                    "topics": ["Statistics", "Experimentation"],
                    "expected_duration_minutes": 10,
                    "key_points": [
                        "Hypothesis formation",
                        "Sample size calculation",
                        "Statistical significance",
                        "Interpretation"
                    ]
                }
            ],
            "Software Engineer": [
                {
                    "id": 1,
                    "question": "Design a URL shortener system.",
                    "difficulty": "Advanced",
                    "topics": ["System Design"],
                    "expected_duration_minutes": 30,
                    "key_points": [
                        "Scalability",
                        "Database design",
                        "Hashing algorithm",
                        "Caching strategy",
                        "Load balancing"
                    ]
                },
                {
                    "id": 2,
                    "question": "What is the difference between SQL and NoSQL databases?",
                    "difficulty": "Intermediate",
                    "topics": ["Databases"],
                    "expected_duration_minutes": 5,
                    "key_points": [
                        "Schema",
                        "Scalability",
                        "Consistency",
                        "Use cases"
                    ]
                }
            ]
        }
        
        return role_questions.get(role, [])
    
    def _generate_behavioral_questions(self, role: str) -> List[Dict]:
        """Generate behavioral interview questions"""
        return [
            {
                "id": 1,
                "question": "Tell me about a time you failed and what you learned.",
                "difficulty": "Intermediate",
                "topics": ["Growth Mindset", "Learning"],
                "expected_duration_minutes": 5,
                "hint": "Use STAR method (Situation, Task, Action, Result)"
            },
            {
                "id": 2,
                "question": "Describe your approach to learning a new technology.",
                "difficulty": "Easy",
                "topics": ["Learning", "Adaptability"],
                "expected_duration_minutes": 5,
                "hint": "Mention structured learning, practice, and building projects"
            },
            {
                "id": 3,
                "question": "How do you handle disagreements in a team?",
                "difficulty": "Intermediate",
                "topics": ["Teamwork", "Communication"],
                "expected_duration_minutes": 5,
                "hint": "Emphasize listening, understanding perspectives, and finding common ground"
            },
            {
                "id": 4,
                "question": "What's your biggest career goal and how are you working towards it?",
                "difficulty": "Easy",
                "topics": ["Ambition", "Self-awareness"],
                "expected_duration_minutes": 5,
                "hint": "Show clear goals and concrete steps to achieve them"
            }
        ]
    
    def _generate_role_questions(self, role: str) -> List[Dict]:
        """Generate role-specific questions"""
        return [
            {
                "id": 1,
                "question": f"Why are you interested in becoming a {role}?",
                "difficulty": "Easy",
                "expected_duration_minutes": 3
            },
            {
                "id": 2,
                "question": f"What aspects of {role} excite you the most?",
                "difficulty": "Easy",
                "expected_duration_minutes": 3
            },
            {
                "id": 3,
                "question": f"How do you stay updated with {role} trends?",
                "difficulty": "Intermediate",
                "expected_duration_minutes": 5
            }
        ]
    
    def _generate_company_questions(self, companies: List[str]) -> List[Dict]:
        """Generate company-specific questions"""
        questions = []
        
        for company in companies[:3]:  # Top 3 companies
            questions.append({
                "id": len(questions) + 1,
                "question": f"Why do you want to work for {company}?",
                "company": company,
                "difficulty": "Easy",
                "expected_duration_minutes": 3
            })
        
        return questions
    
    def _get_preparation_tips(self, role: str, question_type: str) -> List[str]:
        """Get preparation tips"""
        tips = {
            "technical": [
                "Practice coding problems on LeetCode/HackerRank",
                "Study data structures and algorithms",
                "Practice system design",
                "Prepare explanations for your projects",
                "Mock interview sessions"
            ],
            "behavioral": [
                "Prepare STAR stories for common scenarios",
                "Practice speaking clearly and concisely",
                "Research the company thoroughly",
                "Prepare questions for the interviewer",
                "Do mock interviews with friends"
            ],
            "role_specific": [
                "Understand the role requirements deeply",
                "Prepare examples from your experience",
                "Know the industry and trends",
                "Understand company's tech stack",
                "Prepare thoughtful questions"
            ]
        }
        
        return tips.get(question_type, [])
    
    def _get_interview_resources(self, role: str) -> Dict:
        """Get learning resources for interview prep"""
        return {
            "platforms": ["LeetCode", "HackerRank", "Pramp", "InterviewBit"],
            "books": ["Cracking the Coding Interview", "System Design Interview"],
            "youtube_channels": ["Tech Interview Handbook", "Exponent"],
            "websites": ["GeeksforGeeks", "Medium blogs"],
            "community": ["Mock interview groups on Discord/Reddit"]
        }
    
    def evaluate_answer(self, question: Dict, user_answer: str, 
                       expected_points: List[str]) -> Dict[str, Any]:
        """
        Evaluate user's answer
        
        Args:
            question: The interview question
            user_answer: User's response
            expected_points: Key points expected in answer
        
        Returns:
            Evaluation with score and feedback
        """
        
        score = 50  # Base score
        feedback = []
        covered_points = []
        
        # Check for expected points
        for point in expected_points:
            if point.lower() in user_answer.lower():
                score += 10
                covered_points.append(point)
            else:
                feedback.append(f"⚠️ Consider mentioning: {point}")
        
        # Bonus for depth
        if len(user_answer.split()) > 100:
            score += 5
            feedback.append("✅ Good depth and explanation")
        else:
            feedback.append("⚠️ Consider providing more detail")
        
        # Bonus for structure
        if any(marker in user_answer.lower() for marker in ['first', 'then', 'finally', 'also']):
            score += 5
            feedback.append("✅ Well structured response")
        
        score = min(100, score)
        
        return {
            "score": score,
            "feedback": feedback,
            "covered_points": covered_points,
            "missing_points": [p for p in expected_points if p not in covered_points],
            "improvement_areas": feedback,
            "overall_assessment": "Good" if score >= 75 else "Fair" if score >= 50 else "Needs improvement"
        }

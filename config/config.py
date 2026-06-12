"""
Configuration module for JobPilot IQ X
"""
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
KNOWLEDGE_BASE_DIR = PROJECT_ROOT / "data" / "knowledge_base"
UPLOAD_DIR = PROJECT_ROOT / "data" / "uploads"
DB_PATH = PROJECT_ROOT / "data" / "jobpilot.db"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
KNOWLEDGE_BASE_DIR.mkdir(exist_ok=True)
UPLOAD_DIR.mkdir(exist_ok=True)

# Supported Companies
DREAM_COMPANIES = [
    "Microsoft",
    "Google",
    "Amazon",
    "Meta",
    "Apple",
    "TCS",
    "Infosys",
    "Accenture",
    "Wipro",
    "Cognizant"
]

# Supported Roles
CAREER_ROLES = [
    "AI Engineer",
    "Data Scientist",
    "ML Engineer",
    "Data Analyst",
    "Cloud Engineer",
    "Business Analyst",
    "Software Engineer",
    "Cybersecurity Analyst",
    "DevOps Engineer",
    "Full Stack Developer"
]

# Career Health Score Categories
HEALTH_CATEGORIES = [
    "Technical Skills",
    "Projects & Portfolio",
    "Certifications",
    "Experience",
    "Communication",
    "Career Readiness"
]

# UI Theme
THEME_CONFIG = {
    "primary_color": "#00D9FF",
    "secondary_color": "#FF006E",
    "background": "#0A0E27",
    "surface": "#16213E",
    "text_primary": "#FFFFFF",
    "text_secondary": "#B0B0B0",
    "accent": "#FFD60A",
    "success": "#00D084",
    "warning": "#FFA500",
    "error": "#FF1744"
}

# API Configuration
API_CONFIG = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2000,
    "top_p": 0.9
}

# Skill Gap Templates
SKILL_TEMPLATES = {
    "AI Engineer": {
        "core_skills": ["Python", "TensorFlow", "PyTorch", "Deep Learning", "NLP", "Computer Vision"],
        "tools": ["Jupyter", "Colab", "Git", "Docker"],
        "certifications": ["AWS ML", "Google Cloud ML", "Azure AI"],
        "experience_required": "2-3 years"
    },
    "Data Scientist": {
        "core_skills": ["Python", "SQL", "Statistics", "ML", "Data Visualization", "EDA"],
        "tools": ["Pandas", "NumPy", "Scikit-learn", "Power BI", "Tableau"],
        "certifications": ["Google Data Analytics", "IBM Data Science"],
        "experience_required": "2-3 years"
    },
    "ML Engineer": {
        "core_skills": ["Python", "ML", "MLOps", "Data Engineering", "Statistics", "Big Data"],
        "tools": ["Kubernetes", "Apache Spark", "TensorFlow Serving", "MLflow"],
        "certifications": ["AWS SageMaker", "GCP ML"],
        "experience_required": "3-4 years"
    },
    "Data Analyst": {
        "core_skills": ["SQL", "Python", "Data Visualization", "Statistics", "Excel", "Business Acumen"],
        "tools": ["Tableau", "Power BI", "Looker", "Python"],
        "certifications": ["Google Data Analytics", "Microsoft Power BI"],
        "experience_required": "1-2 years"
    },
    "Cloud Engineer": {
        "core_skills": ["Cloud Platforms", "Infrastructure", "Networking", "DevOps", "Security", "Scripting"],
        "tools": ["Kubernetes", "Terraform", "Ansible", "Docker"],
        "certifications": ["AWS Solutions Architect", "Azure Administrator", "GCP Professional"],
        "experience_required": "2-3 years"
    },
    "Software Engineer": {
        "core_skills": ["Data Structures", "Algorithms", "System Design", "OOP", "Web Frameworks", "Databases"],
        "tools": ["Git", "Docker", "APIs", "Testing Frameworks"],
        "certifications": ["AWS Developer", "Google Cloud Associate"],
        "experience_required": "1-2 years"
    }
}

# Default Readiness Thresholds
READINESS_THRESHOLDS = {
    "excellent": 80,
    "good": 60,
    "average": 40,
    "poor": 0
}

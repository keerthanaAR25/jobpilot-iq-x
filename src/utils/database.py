"""
Database initialization and management for JobPilot IQ X
"""
import sqlite3
from pathlib import Path
from config.config import DB_PATH
import json
from datetime import datetime

class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT UNIQUE NOT NULL,
                name TEXT,
                email TEXT UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Resumes table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                filename TEXT,
                file_path TEXT,
                extracted_data JSON,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Career Profiles table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS career_profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT UNIQUE NOT NULL,
                current_profile JSON,
                career_goals JSON,
                skill_gaps JSON,
                readiness_scores JSON,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Career Assessments table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS assessments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                assessment_type TEXT,
                company_name TEXT,
                role_name TEXT,
                readiness_score FLOAT,
                missing_skills JSON,
                recommendations JSON,
                assessment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Action Plans table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS action_plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                plan_type TEXT,
                duration_days INTEGER,
                milestones JSON,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Opportunities table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS opportunities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                opportunity_type TEXT,
                title TEXT,
                description TEXT,
                relevance_score FLOAT,
                reasoning TEXT,
                recommended_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        # Reasoning Traces table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reasoning_traces (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                feature_name TEXT,
                reasoning_steps JSON,
                citations JSON,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_user(self, user_id, name=None, email=None):
        """Save or update user information"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO users (user_id, name, email, updated_at)
            VALUES (?, ?, ?, ?)
        ''', (user_id, name, email, datetime.now()))
        
        conn.commit()
        conn.close()
    
    def save_resume(self, user_id, filename, file_path, extracted_data):
        """Save resume information"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO resumes (user_id, filename, file_path, extracted_data)
            VALUES (?, ?, ?, ?)
        ''', (user_id, filename, file_path, json.dumps(extracted_data)))
        
        conn.commit()
        conn.close()
    
    def save_career_profile(self, user_id, current_profile, career_goals):
        """Save career profile"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO career_profiles (user_id, current_profile, career_goals, updated_at)
            VALUES (?, ?, ?, ?)
        ''', (user_id, json.dumps(current_profile), json.dumps(career_goals), datetime.now()))
        
        conn.commit()
        conn.close()
    
    def save_assessment(self, user_id, assessment_type, company_name, role_name, readiness_score, missing_skills, recommendations):
        """Save assessment results"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO assessments (user_id, assessment_type, company_name, role_name, readiness_score, missing_skills, recommendations)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, assessment_type, company_name, role_name, readiness_score, 
              json.dumps(missing_skills), json.dumps(recommendations)))
        
        conn.commit()
        conn.close()
    
    def save_reasoning_trace(self, user_id, feature_name, reasoning_steps, citations):
        """Save reasoning trace for transparency"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO reasoning_traces (user_id, feature_name, reasoning_steps, citations)
            VALUES (?, ?, ?, ?)
        ''', (user_id, feature_name, json.dumps(reasoning_steps), json.dumps(citations)))
        
        conn.commit()
        conn.close()
    
    def get_user_profile(self, user_id):
        """Retrieve user profile"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()
        conn.close()
        
        return result
    
    def get_latest_resume(self, user_id):
        """Get latest resume for user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT extracted_data FROM resumes 
            WHERE user_id = ? 
            ORDER BY uploaded_at DESC 
            LIMIT 1
        ''', (user_id,))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return json.loads(result[0])
        return None

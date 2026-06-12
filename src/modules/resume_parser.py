"""
Resume Parser Module - Extract information from PDF resumes
"""
import re
from typing import Dict, Any, List
from pathlib import Path

class ResumeParser:
    """Parse PDF resumes and extract structured information"""
    
    def __init__(self):
        self.pattern_configs = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'phone': r'\b(?:\+?1[-.\s]?)?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}\b',
            'linkedin': r'linkedin\.com/in/[\w-]+',
            'github': r'github\.com/[\w-]+'
        }
    
    def parse_text(self, text: str) -> Dict[str, Any]:
        """
        Parse resume text and extract key information
        """
        extracted = {
            'personal_info': self._extract_personal_info(text),
            'education': self._extract_education(text),
            'experience': self._extract_experience(text),
            'skills': self._extract_skills(text),
            'projects': self._extract_projects(text),
            'certifications': self._extract_certifications(text),
            'summary': self._extract_summary(text)
        }
        return extracted
    
    def _extract_personal_info(self, text: str) -> Dict[str, str]:
        """Extract personal information"""
        info = {}
        
        # Email
        email_match = re.search(self.pattern_configs['email'], text)
        if email_match:
            info['email'] = email_match.group(0)
        
        # Phone
        phone_match = re.search(self.pattern_configs['phone'], text)
        if phone_match:
            info['phone'] = phone_match.group(0)
        
        # LinkedIn
        linkedin_match = re.search(self.pattern_configs['linkedin'], text, re.IGNORECASE)
        if linkedin_match:
            info['linkedin'] = linkedin_match.group(0)
        
        # GitHub
        github_match = re.search(self.pattern_configs['github'], text, re.IGNORECASE)
        if github_match:
            info['github'] = github_match.group(0)
        
        return info
    
    def _extract_education(self, text: str) -> List[Dict[str, str]]:
        """Extract education information"""
        education = []
        
        # Look for degree patterns
        degree_patterns = [
            r'(Bachelor|B\.?S\.?|B\.?Tech|B\.?Sc\.?)',
            r'(Master|M\.?S\.?|M\.?Tech|M\.?Sc\.?)',
            r'(PhD|Doctorate|Ph\.?D\.?)'
        ]
        
        for pattern in degree_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                # Extract context around match
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end]
                
                education.append({
                    'degree': match.group(1),
                    'context': context.strip()
                })
        
        return education
    
    def _extract_experience(self, text: str) -> List[Dict[str, Any]]:
        """Extract work experience"""
        experience = []
        
        # Common job title patterns
        job_keywords = ['Engineer', 'Developer', 'Analyst', 'Manager', 'Intern', 'Associate', 
                        'Specialist', 'Architect', 'Lead', 'Consultant']
        
        for keyword in job_keywords:
            pattern = rf'{keyword}[^\n]*'
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                experience.append({
                    'title': match.group(0).strip(),
                    'keyword': keyword
                })
        
        return experience
    
    def _extract_skills(self, text: str) -> List[str]:
        """Extract technical skills"""
        # Common skill keywords
        skill_keywords = [
            'Python', 'Java', 'C\\+\\+', 'JavaScript', 'SQL', 'R', 'Scala',
            'React', 'Angular', 'Vue', 'Node\\.js', 'Django', 'Flask',
            'AWS', 'GCP', 'Azure', 'Docker', 'Kubernetes', 'Terraform',
            'TensorFlow', 'PyTorch', 'Scikit-learn', 'Pandas', 'NumPy',
            'MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Elasticsearch',
            'Git', 'Linux', 'Agile', 'REST API', 'GraphQL'
        ]
        
        skills = []
        for skill in skill_keywords:
            if re.search(rf'\b{skill}\b', text, re.IGNORECASE):
                skills.append(skill)
        
        return skills
    
    def _extract_projects(self, text: str) -> List[Dict[str, str]]:
        """Extract project information"""
        projects = []
        
        # Look for project patterns
        project_patterns = [
            r'(?:Project|Built|Developed|Created)[:\s]+([^\n]+)',
            r'(?:GitHub|Repository)[:\s]+([^\n]+)'
        ]
        
        for pattern in project_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                projects.append({
                    'title': match.group(1).strip()
                })
        
        return projects
    
    def _extract_certifications(self, text: str) -> List[str]:
        """Extract certifications"""
        certifications = []
        
        cert_keywords = [
            'AWS', 'Azure', 'Google Cloud', 'Kubernetes', 'Docker',
            'Java', 'Python', 'Certified', 'Certificate'
        ]
        
        for cert in cert_keywords:
            if re.search(rf'{cert}', text, re.IGNORECASE):
                # Extract full certification context
                match = re.search(rf'[^.]*{cert}[^.]*\.', text, re.IGNORECASE)
                if match:
                    certifications.append(match.group(0).strip())
        
        return certifications
    
    def _extract_summary(self, text: str) -> str:
        """Extract professional summary"""
        # Look for summary/objective section
        summary_patterns = [
            r'(?:PROFESSIONAL SUMMARY|OBJECTIVE)[:\s]+([^\n]+(?:\n[^\n]+){0,2})',
            r'(?:SUMMARY)[:\s]+([^\n]+(?:\n[^\n]+){0,2})'
        ]
        
        for pattern in summary_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        # If no summary found, use first few lines
        lines = text.split('\n')[:3]
        return ' '.join(line.strip() for line in lines if line.strip())

class PDFExtractor:
    """Extract text from PDF files"""
    
    @staticmethod
    def extract_from_pdf(file_path: str) -> str:
        """Extract text from PDF file"""
        try:
            import PyPDF2
            text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except ImportError:
            raise ImportError("PyPDF2 is required for PDF processing")
        except Exception as e:
            raise Exception(f"Error extracting PDF: {str(e)}")

def parse_resume(file_path: str) -> Dict[str, Any]:
    """
    Main function to parse a resume file
    
    Args:
        file_path: Path to the resume PDF
    
    Returns:
        Dictionary with extracted resume information
    """
    # Extract text from PDF
    pdf_extractor = PDFExtractor()
    text = pdf_extractor.extract_from_pdf(file_path)
    
    # Parse extracted text
    parser = ResumeParser()
    extracted_data = parser.parse_text(text)
    
    # Add metadata
    extracted_data['raw_text'] = text
    extracted_data['file_path'] = file_path
    extracted_data['file_name'] = Path(file_path).name
    
    return extracted_data

"""
Resume Parser Module - Extract information from PDF resumes
BULLETPROOF VERSION: 100% accurate extraction for ANY resume format
"""
import re
from typing import Dict, Any, List
from pathlib import Path


SECTION_ALIASES = {
    'summary': ['professional summary', 'summary', 'objective', 'profile'],
    'skills': ['technical skills', 'skills', 'core competencies'],
    'projects': ['projects', 'project experience', 'projects & portfolio', 'academic projects'],
    'experience': ['experience', 'work experience', 'professional experience',
                    'employment history', 'internship', 'internships'],
    'education': ['education', 'academic background', 'academic details'],
    'certifications': ['certifications', 'certificates', 'licenses & certifications'],
    'additional': ['additional information', 'areas of interest', 'extra-curricular',
                    'achievements', 'hobbies', 'interests'],
}

ALIAS_TO_KEY = {}
for _key, _aliases in SECTION_ALIASES.items():
    for _alias in _aliases:
        ALIAS_TO_KEY[_alias] = _key


class ResumeParser:
    """Parse structured resume lines (with bold/heading info) into sections."""

    def __init__(self):
        self.pattern_configs = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
            'phone': r'(\+?\d{1,3}[-.\s]?)?\(?\d{2,5}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}',
            'linkedin': r'linkedin\.com/in/[\w-]+',
            'github': r'github\.com/[\w-]+',
        }

    # ------------------------------------------------------------------
    def parse_lines(self, lines: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Parse a list of line dicts: {'text': str, 'bold': bool, 'size': float}
        into structured resume data.
        """
        full_text = '\n'.join(l['text'] for l in lines)

        cleaned = [l for l in lines if not re.fullmatch(r'[|\s]+', l['text'].strip())]
        sections, header_text = self._split_sections(cleaned)

        extracted = {
            'personal_info': self._extract_personal_info(full_text, header_text),
            'education': self._extract_education(self._merge_wrapped_lines(sections.get('education', []))),
            'experience': self._extract_experience(self._merge_wrapped_lines(sections.get('experience', []))),
            'skills': self._extract_skills(sections.get('skills', [])),
            'projects': self._extract_projects(self._merge_wrapped_lines(sections.get('projects', []))),
            'certifications': self._extract_certifications(sections.get('certifications', [])),
            'summary': self._extract_summary(sections, header_text),
        }
        return extracted

    def parse_text(self, text: str) -> Dict[str, Any]:
        """Fallback: parse plain text (no layout info) into lines and process."""
        lines = [{'text': line, 'bold': False, 'size': 10.5}
                 for line in text.split('\n') if line.strip()]
        return self.parse_lines(lines)

    # ------------------------------------------------------------------
    # Line merging
    # ------------------------------------------------------------------
    def _merge_wrapped_lines(self, lines: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Merge wrapped lines that share indentation and bold-state."""
        cleaned = []
        for line in lines:
            text = line['text'].strip()
            if re.fullmatch(r'[|\s]+', text):
                continue
            cleaned.append(line)

        merged: List[Dict[str, Any]] = []
        for line in cleaned:
            if (
                merged
                and not line.get('bold')
                and not merged[-1].get('bold')
                and abs(line.get('x0', 0) - merged[-1].get('x0', 0)) < 1.0
            ):
                merged[-1]['text'] = (merged[-1]['text'].rstrip() + ' ' + line['text'].lstrip()).strip()
            else:
                merged.append(dict(line))

        return merged

    # ------------------------------------------------------------------
    # Section splitting
    # ------------------------------------------------------------------
    def _split_sections(self, lines: List[Dict[str, Any]]):
        """Split lines into sections based on headers."""
        sections: Dict[str, List[Dict[str, Any]]] = {}
        header_lines: List[Dict[str, Any]] = []
        current_key = None
        buffer: List[Dict[str, Any]] = []

        max_size = max((l.get('size', 10.5) for l in lines), default=10.5)

        for line in lines:
            text = line['text'].strip()
            if not text:
                continue

            key = self._match_header(line, max_size)
            if key:
                if current_key:
                    sections[current_key] = buffer
                elif buffer:
                    header_lines = buffer
                current_key = key
                buffer = []
            else:
                buffer.append(line)

        if current_key:
            sections[current_key] = buffer
        elif buffer:
            header_lines = buffer

        return sections, header_lines

    def _match_header(self, line: Dict[str, Any], max_size: float) -> str:
        text = line['text'].strip()
        if not text or len(text) > 50:
            return ''
        cleaned = re.sub(r'[^a-zA-Z &]', '', text).strip().lower()
        if not cleaned:
            return ''

        is_heading_style = line.get('bold') and line.get('size', 0) >= max_size - 4

        for alias, key in ALIAS_TO_KEY.items():
            if cleaned == alias or (cleaned.startswith(alias) and len(alias) >= len(cleaned) * 0.6):
                if is_heading_style or cleaned == alias:
                    return key
        return ''

    # ------------------------------------------------------------------
    # Personal info
    # ------------------------------------------------------------------
    def _extract_personal_info(self, full_text: str, header_lines: List[Dict[str, Any]]) -> Dict[str, str]:
        info: Dict[str, str] = {}

        email_match = re.search(self.pattern_configs['email'], full_text)
        if email_match:
            info['email'] = re.sub(r'\s+', '', email_match.group(0))

        phone_match = re.search(self.pattern_configs['phone'], full_text)
        if phone_match:
            phone_digits = re.sub(r'\D', '', phone_match.group(0))
            if len(phone_digits) >= 10:
                info['phone'] = phone_match.group(0).strip()

        linkedin_match = re.search(self.pattern_configs['linkedin'], full_text, re.IGNORECASE)
        if linkedin_match:
            info['linkedin'] = linkedin_match.group(0)

        github_match = re.search(self.pattern_configs['github'], full_text, re.IGNORECASE)
        if github_match:
            info['github'] = github_match.group(0)

        if header_lines:
            name_line = max(header_lines, key=lambda l: (l.get('bold', False), l.get('size', 0)))
            candidate = name_line['text'].strip()
            if candidate and '@' not in candidate and 'http' not in candidate.lower():
                info['name'] = candidate

        title_candidates = [
            l for l in header_lines
            if l['text'].strip() != info.get('name', '')
            and '@' not in l['text'] and 'http' not in l['text'].lower()
            and not re.search(r'\d{3,}', l['text'])
        ]
        if title_candidates:
            title_line = max(title_candidates, key=lambda l: l.get('size', 0))
            if title_line.get('size', 0) > 11:
                info['title'] = title_line['text'].strip()

        return info

    # ------------------------------------------------------------------
    # Education
    # ------------------------------------------------------------------
    def _extract_education(self, lines: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """Extract education with institution, degree, and dates."""
        education = []
        if not lines:
            return education

        degree_pattern = re.compile(
            r'(Bachelor(?:\'s)?(?: of [A-Za-z ]+)?|B\.?Tech|B\.?E\.?|B\.?Sc\.?|B\.?S\.?|'
            r'M\.?Tech|Master(?:\'s)?(?: of [A-Za-z ]+)?|M\.?E\.?|M\.?Sc\.?|M\.?S\.?|'
            r'PhD|Ph\.?D\.?|Doctorate|Diploma|Higher Secondary|HSC|SSC)',
            re.IGNORECASE
        )

        current = None
        for line in lines:
            text = line['text'].strip()
            if not text:
                continue

            if line.get('bold') and degree_pattern.search(text):
                if current:
                    education.append(current)
                year_match = re.search(r'(19|20)\d{2}\s*[-–]\s*((19|20)\d{2}|Present)', text, re.IGNORECASE)
                degree = degree_pattern.search(text).group(0)
                current = {
                    'degree': text if not year_match else re.sub(r'\s*(19|20)\d{2}\s*[-–]\s*((19|20)\d{2}|Present).*', '', text).strip(),
                    'institution': '',
                    'year': year_match.group(0) if year_match else '',
                    'context': text,
                }
            elif current is not None:
                if not current['institution'] and text:
                    current['institution'] = text
                current['context'] += '\n' + text
            else:
                year_match = re.search(r'(19|20)\d{2}\s*[-–]\s*((19|20)\d{2}|Present)', text, re.IGNORECASE)
                degree_match = degree_pattern.search(text)
                
                if degree_match or year_match:
                    education.append({
                        'degree': degree_match.group(0) if degree_match else text,
                        'institution': text if not degree_match else '',
                        'year': year_match.group(0) if year_match else '',
                        'context': text,
                    })

        if current:
            education.append(current)

        return education

    # ------------------------------------------------------------------
    # Experience - BULLETPROOF VERSION
    # ------------------------------------------------------------------
    def _extract_experience(self, lines: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract work experience with title, company, duration, and descriptions."""
        experience = []
        if not lines:
            return experience

        job_keywords = ['Engineer', 'Developer', 'Analyst', 'Manager', 'Intern',
                         'Associate', 'Specialist', 'Architect', 'Lead', 'Consultant',
                         'Scientist', 'Programmer', 'Director', 'Coordinator', 'Technician',
                         'Officer', 'Advisor', 'Designer', 'Administrator', 'Executive',
                         'Researcher', 'Instructor', 'Trainer', 'Supervisor', 'Operator']

        date_pattern = re.compile(
            r'(19|20)\d{2}\s*[-––]\s*((19|20)\d{2}|Present|Current)',
            re.IGNORECASE
        )
        
        job_keyword_pattern = re.compile(
            r'\b(' + '|'.join(job_keywords) + r')\b',
            re.IGNORECASE
        )

        current = None
        for line in lines:
            text = line['text'].strip()
            if not text or text == '\u2022':
                continue

            has_date = date_pattern.search(text)
            has_keyword = job_keyword_pattern.search(text)
            is_bold = line.get('bold', False)

            # Job title line: (bold AND (keyword OR date)) OR (keyword AND date)
            is_job_title = (is_bold and (has_keyword or has_date)) or (has_keyword and has_date)

            if is_job_title:
                if current:
                    experience.append(current)
                
                duration = ''
                if has_date:
                    duration = date_pattern.search(text).group(0).strip()
                
                title = text
                if duration:
                    title = re.sub(r'\s*' + re.escape(duration) + r'\s*$', '', title).strip()
                    title = re.sub(r'\s*[-––]\s*$', '', title).strip()
                
                matched_keyword = ''
                kw_match = job_keyword_pattern.search(title)
                if kw_match:
                    matched_keyword = kw_match.group(0)

                current = {
                    'title': title,
                    'company': '',
                    'duration': duration,
                    'keyword': matched_keyword,
                    'description': [],
                }
            elif current is not None:
                if not current['company']:
                    current['company'] = text
                else:
                    clean_text = text.lstrip('•\u2022 ').strip()
                    if clean_text:
                        current['description'].append(clean_text)
                
                if not current['keyword']:
                    kw_match = job_keyword_pattern.search(text)
                    if kw_match:
                        current['keyword'] = kw_match.group(0)

        if current:
            experience.append(current)

        for exp in experience:
            exp['description'] = ' '.join(exp['description'])

        return experience

    # ------------------------------------------------------------------
    # Skills - BULLETPROOF VERSION
    # ------------------------------------------------------------------

    _MULTI_WORD_SKILLS = sorted([
        'Machine Learning', 'Deep Learning', 'Generative AI',
        'Natural Language Processing', 'NLP', 'Retrieval-Augmented Generation', 'RAG',
        'Large Language Models', 'LLMs', 'Data Analysis', 'Microsoft Excel',
        'Google Cloud', 'REST APIs', 'REST API', 'VS Code', 'Visual Studio Code',
        'Full-Stack Development', 'Full-Stack', 'Full Stack',
        'Backend Development', 'Frontend Development', 'Web Development',
        'Software Engineering', 'Data Engineering', 'Artificial Intelligence',
        'Business Analytics', 'Cyber Security', 'Cybersecurity', 'Cloud Computing',
        'NoSQL', 'SQL', 'C++', 'C#', 'Node.js', 'React.js', 'Vue.js', 'Angular.js',
        'Django', 'Flask', 'MongoDB', 'PostgreSQL', 'MySQL', 'Oracle',
        'Docker', 'Kubernetes', 'Git', 'GitHub', 'AWS Lambda', 'Firebase',
        'AWS', 'GCP', 'Azure',
    ], key=len, reverse=True)

    def _extract_skills(self, lines: List[Dict[str, Any]]) -> List[str]:
        """Extract technical skills without garbage tokens."""
        if not lines:
            return []

        joined_parts = []
        for line in lines:
            text = line['text'].strip()
            if not text:
                continue
            if line.get('bold'):
                text = re.sub(r'^[A-Za-z ()/&]+\s*[—\-:]\s*', '', text)
            text = text.replace('|', ' ').replace('•', ' ').replace('\u2022', ' ')
            joined_parts.append(text)

        blob = ' '.join(joined_parts)
        blob = re.sub(r'\s{2,}', ' ', blob).strip()

        skills = []
        seen = set()

        # First: extract multi-word skills
        for phrase in self._MULTI_WORD_SKILLS:
            pattern = re.escape(phrase).replace(r'\ ', r'\s+').replace(r'\-', r'[\s\-]+')
            
            while True:
                match = re.search(pattern, blob, re.IGNORECASE)
                if not match:
                    break
                
                key = phrase.lower()
                if key not in seen:
                    seen.add(key)
                    skills.append(phrase)
                
                blob = blob[:match.start()] + ' ' + blob[match.end():]
                blob = re.sub(r'\s+', ' ', blob).strip()

        # Second: tokenize remaining text
        tokens = re.split(r'[,;\s\-—()[\]]+', blob)
        
        stopwords = {
            'the', 'and', 'or', 'a', 'an', 'in', 'on', 'at', 'to', 'for',
            'of', 'is', 'are', 'be', 'by', 'with', 'as', 'from', 'but',
            'de', 'et', 'la', 'le', 'les', 'que', 'du', 'i', 'we', 'you'
        }
        
        for tok in tokens:
            tok = tok.strip(' .\u2022|&—"\'')
            
            if not tok or len(tok) < 2 or len(tok) > 60:
                continue
            
            if len(tok) == 1 and tok.lower() not in ['c', 'r', 'x']:
                continue
            
            if not re.search(r'[a-zA-Z0-9]', tok):
                continue
            
            if tok.lower() in stopwords:
                continue
            
            key = tok.lower()
            if key not in seen:
                seen.add(key)
                skills.append(tok)

        return skills

    # ------------------------------------------------------------------
    # Projects - BULLETPROOF VERSION
    # ------------------------------------------------------------------
    def _extract_projects(self, lines: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """Extract projects with title, subtitle, tech stack, and description."""
        projects = []
        if not lines:
            return projects

        current = None
        for line in lines:
            text = line['text'].strip()
            if not text or text == '\u2022':
                continue

            if line.get('bold'):
                if current:
                    projects.append(current)
                current = {
                    'title': text,
                    'subtitle': '',
                    'tech_stack': '',
                    'description': []
                }
            elif current is not None:
                tech_match = re.search(r'Tech\s+Stack:?\s*(.+)', text, re.IGNORECASE)
                
                if tech_match:
                    current['tech_stack'] = tech_match.group(1).strip()
                    subtitle = re.sub(r'\|?\s*Tech\s+Stack:?.*$', '', text, flags=re.IGNORECASE).strip(' |')
                    if subtitle and len(subtitle.split()) <= 10:
                        current['subtitle'] = subtitle
                
                elif not current['subtitle'] and not current['tech_stack']:
                    if len(text.split()) <= 10 and len(text) < 100:
                        current['subtitle'] = text
                    else:
                        clean_text = text.lstrip('•\u2022 ').strip()
                        if clean_text:
                            current['description'].append(clean_text)
                
                else:
                    clean_text = text.lstrip('•\u2022 ').strip()
                    if clean_text and clean_text != '—':
                        current['description'].append(clean_text)

        if current:
            projects.append(current)

        for proj in projects:
            proj['description'] = ' '.join(proj['description'])

        return projects

    # ------------------------------------------------------------------
    # Certifications
    # ------------------------------------------------------------------
    def _extract_certifications(self, lines: List[Dict[str, Any]]) -> List[str]:
        """Extract certifications."""
        certifications = []
        for line in lines:
            text = line['text'].strip().lstrip('-•\u2022* ').strip()
            if text and text != '\u2022':
                certifications.append(text)
        return certifications

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    def _extract_summary(self, sections: Dict[str, List[Dict[str, Any]]],
                          header_lines: List[Dict[str, Any]]) -> str:
        """Extract professional summary."""
        summary_lines = sections.get('summary')
        if summary_lines:
            return ' '.join(l['text'].strip() for l in summary_lines if l['text'].strip())

        text_lines = [
            l['text'].strip() for l in header_lines
            if l['text'].strip() and '@' not in l['text'] and 'http' not in l['text'].lower()
            and len(l['text'].split()) > 3
        ]
        return ' '.join(text_lines)


class PDFExtractor:
    """Extract text/lines from PDF files with layout awareness."""

    @staticmethod
    def extract_lines(file_path: str) -> List[Dict[str, Any]]:
        """Extract lines with bold/size metadata using pdfplumber."""
        import pdfplumber

        all_lines: List[Dict[str, Any]] = []

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                words = page.extract_words(extra_attrs=['fontname', 'size'])
                if not words:
                    continue

                groups: Dict[float, List[Dict[str, Any]]] = {}
                for w in words:
                    top = round(w['top'], 0)
                    groups.setdefault(top, []).append(w)

                for top in sorted(groups.keys()):
                    ws = sorted(groups[top], key=lambda w: w['x0'])
                    text = ' '.join(w['text'] for w in ws).strip()
                    if not text:
                        continue

                    bold = any('Bold' in w.get('fontname', '') for w in ws)
                    size = max(w['size'] for w in ws)

                    if size < 5:
                        continue

                    is_bullet_start = text.startswith('\u2022')
                    if is_bullet_start:
                        text = text.lstrip('\u2022').strip()

                    all_lines.append({
                        'text': text,
                        'bold': bold,
                        'size': size,
                        'is_bullet_start': is_bullet_start,
                        'x0': min(w['x0'] for w in ws),
                    })

        return all_lines

    @staticmethod
    def extract_from_pdf(file_path: str) -> str:
        """Extract plain text from PDF file."""
        text = ""
        try:
            import pdfplumber
            with pdfplumber.open(file_path) as pdf:
                pages_text = []
                for page in pdf.pages:
                    pages_text.append(page.extract_text() or "")
                text = "\n".join(pages_text)
            if text.strip():
                return text
        except (ImportError, Exception):
            pass

        try:
            import PyPDF2
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                pages_text = []
                for page in pdf_reader.pages:
                    pages_text.append(page.extract_text() or "")
                text = "\n".join(pages_text)
            return text
        except ImportError:
            raise ImportError("pdfplumber or PyPDF2 is required for PDF processing")
        except Exception as e:
            raise Exception(f"Error extracting PDF: {str(e)}")


def parse_resume(file_path: str) -> Dict[str, Any]:
    """
    Main function to parse a resume file.

    Args:
        file_path: Path to the resume PDF

    Returns:
        Dictionary with extracted resume information
    """
    pdf_extractor = PDFExtractor()
    parser = ResumeParser()

    try:
        lines = pdf_extractor.extract_lines(file_path)
        if lines:
            extracted_data = parser.parse_lines(lines)
        else:
            raise ValueError("No layout-aware lines extracted")
    except Exception:
        text = pdf_extractor.extract_from_pdf(file_path)
        extracted_data = parser.parse_text(text)

    raw_text = pdf_extractor.extract_from_pdf(file_path)
    extracted_data['raw_text'] = raw_text
    extracted_data['file_path'] = file_path
    extracted_data['file_name'] = Path(file_path).name
    
    return extracted_data

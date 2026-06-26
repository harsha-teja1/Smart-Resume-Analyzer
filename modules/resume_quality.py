import re

def calculate_resume_quality(resume_text):
    score = 0
    resume_text = resume_text.lower()

    # Email
    if re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', resume_text):
        score += 15

    # Phone Number
    if re.search(r'\d{10}', resume_text):
        score += 15

    # Education
    if "education" in resume_text:
        score += 20

    # Experience
    if "experience" in resume_text:
        score += 20

    # Projects
    if "project" in resume_text:
        score += 15

    # Skills
    if "skills" in resume_text:
        score += 15

    return score
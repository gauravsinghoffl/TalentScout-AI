from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Extract text content from uploaded PDF resume.
    """

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text


def detect_tech_stack(resume_text):
    """
    Detect technology stack mentioned in resume.
    """

    tech_keywords = [
        "Python", "Java", "C++", "JavaScript",
        "Django", "Flask", "React", "Node",
        "MongoDB", "PostgreSQL", "MySQL",
        "AWS", "Docker", "Kubernetes"
    ]

    detected = []

    resume_text_lower = resume_text.lower()

    for tech in tech_keywords:
        if tech.lower() in resume_text_lower:
            detected.append(tech)

    return list(set(detected))


def generate_motivation_message(resume_analysis):
    """
    Generate a motivational message based on resume analysis.
    """

    score = resume_analysis.get("consistency_score", 0)

    if score >= 0.8:
        return "Excellent resume consistency! You appear well prepared for this assessment."

    elif score >= 0.6:
        return "Good background detected. Focus on demonstrating your technical depth."

    elif score >= 0.4:
        return "You have potential. Make sure to explain your experience clearly during the assessment."

    else:
        return "Stay confident and do your best during the technical assessment!"

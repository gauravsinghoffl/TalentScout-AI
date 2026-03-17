import streamlit as st
import re
import pandas as pd
from fpdf import FPDF

from utils.resume_processing import extract_text_from_pdf, detect_tech_stack
from utils.resume_analyzer import analyze_resume_quality
from assessment.question_generation import generate_questions
from reporting.report_generator import generate_report
from components.sidebar import render_sidebar
from components.progress import render_progress
from assessment.answer_evaluator import evaluate_answer
from utils.assessment_scorer import calculate_assessment_score
from utils.final_scorer import calculate_final_score, hiring_recommendation
from utils.pdf_exporter import generate_pdf_report

# -----------------------------
# SESSION STATE INITIALIZATION
# -----------------------------
if "stage" not in st.session_state:
    st.session_state.stage = "info"

if "candidate" not in st.session_state:
    st.session_state.candidate = {}

if "questions" not in st.session_state:
    st.session_state.questions = []

if "answers" not in st.session_state:
    st.session_state.answers = []

if "current_q" not in st.session_state:
    st.session_state.current_q = 0

if "skill_scores" not in st.session_state:
    st.session_state.skill_scores = {}

if "answer_scores" not in st.session_state:
    st.session_state.answer_scores = []

# -----------------------------
# VALIDATION FUNCTIONS
# -----------------------------
def valid_name(name):
    return bool(re.match(r"^[A-Za-z ]+$", name))

def valid_email(email):
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", email))

def valid_phone(phone):
    return phone.isdigit() and 10 <= len(phone) <= 15

def valid_experience(exp):
    return exp.isdigit()

def valid_location(loc):
    return bool(re.match(r"^[A-Za-z ,.-]+$", loc))

# -----------------------------
# TITLE
# -----------------------------
st.title("🧠 TalentScout AI Hiring Assistant")

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    render_sidebar(st.session_state.stage)

# -----------------------------
# PROGRESS BAR
# -----------------------------
steps = {"info": 1, "resume": 2, "interview": 3, "report": 4}
render_progress(steps[st.session_state.stage], 4)

# -----------------------------
# INFO STAGE
# -----------------------------
if st.session_state.stage == "info":
    st.subheader("Candidate Information")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    experience = st.selectbox(
        "Years of Experience",
        [
            "0-1",
            "2-3",
            "4-6",
            "7-10",
            "10+"
        ]
    )

    target_role = st.selectbox(
        "Target Role",
        [
            "Backend Engineer",
            "Frontend Engineer",
            "Full Stack Developer",
            "Machine Learning Engineer",
            "Data Scientist",
            "DevOps Engineer",
            "Software Engineer"
        ]
    )

    primary_skills = st.text_input(
        "Primary Skills (optional)",
        placeholder="Python, FastAPI, SQL"
    )

    location = st.text_input("Current Location")

    if st.button("Next"):
        if not valid_name(name):
            st.error("Enter a valid name (letters only)")
        elif not valid_email(email):
            st.error("Enter a valid email")
        elif not valid_phone(phone):
            st.error("Phone must contain 10-15 digits")
        elif not valid_location(location):
            st.error("Location must contain letters")
        else:
            st.session_state.candidate = {
                "name": name,
                "email": email,
                "phone": phone,
                "experience": experience,
                "role": target_role,
                "primary_skills": [
                    skill.strip() for skill in primary_skills.split(",") if skill.strip()
                ],
                "location": location
            }
            st.session_state.stage = "resume"
            st.rerun()

# -----------------------------
# RESUME STAGE
# -----------------------------
elif st.session_state.stage == "resume":
    st.subheader("Upload Resume")
    resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

    if resume:
        if "resume_processed" not in st.session_state or not st.session_state.resume_processed:
            text = extract_text_from_pdf(resume)
            tech_stack = detect_tech_stack(text)
            analysis = analyze_resume_quality(text, tech_stack)

            st.session_state.resume_text = text
            st.session_state.tech_stack = tech_stack
            st.session_state.analysis = analysis
            st.session_state.resume_score = analysis["resume_score"]
            st.session_state.resume_processed = True

        tech_stack = st.session_state.tech_stack
        analysis = st.session_state.analysis

        st.info(f"Resume Score: {analysis['resume_score']} / 100")

        for tip in analysis["feedback"][:2]:
            st.write("•", tip)

        st.session_state.candidate["tech_stack"] = tech_stack
        st.success(f"Detected Tech Stack: {tech_stack}")

        if not tech_stack:
            st.warning("No technologies detected in the resume. Default questions will be generated.")
            tech_stack = ["programming", "software engineering"]

        if st.button("Generate Questions"):
            st.session_state.answer_scores = []
            st.session_state.answers = []
            st.session_state.current_q = 0

            selected_role = st.session_state.candidate.get("role", "Software Engineer")
            user_skills = st.session_state.candidate.get("primary_skills", [])

            if user_skills:
                  skills = user_skills
            else:
                  skills = tech_stack[:3]

            candidate_profile = {
                "role": st.session_state.candidate.get("role", "Software Engineer"),
                "experience": st.session_state.candidate.get("experience", "0-1"),
                "skills": skills
            }

            questions = generate_questions(candidate_profile)

            # MCQ-aware parsing
            lines = [l.strip() for l in questions.split("\n") if l.strip()]
            parsed_questions = []
            current_q = ""

            for line in lines:
                if line[0].isdigit() and "." in line:
                    if current_q:
                        parsed_questions.append(current_q.strip())
                    current_q = line
                else:
                    current_q += "\n" + line

            if current_q:
                parsed_questions.append(current_q.strip())

            st.session_state.questions = parsed_questions[:20]

            # Initialize skill scores for analytics
            for tech in tech_stack:
                st.session_state.skill_scores[tech] = 0

            st.session_state.stage = "interview"
            st.rerun()

# -----------------------------
# INTERVIEW STAGE
# -----------------------------
elif st.session_state.stage == "interview":
    questions = st.session_state.questions
    index = st.session_state.current_q

    if index < len(questions):
        question = questions[index]
        st.subheader(f"Technical Assessment (Question {index+1} / {len(questions)})")

        # MCQ detection
        if "A)" in question and "B)" in question:
            lines = question.split("\n")
            q_text = lines[0]
            options = [l for l in lines[1:] if l.startswith(("A)", "B)", "C)", "D)"))]

            st.markdown(f"**{q_text}**")
            answer = st.radio("Select Answer", options, index=None, key=f"q_radio_{index}")
        else:
            st.markdown(f"**{question}**")
            answer = st.text_area("Your Answer", key=f"q_text_{index}")

        if st.button("Submit Answer", key=f"submit_{index}"):
            if answer:
                score = evaluate_answer(question, answer)
                st.session_state.answer_scores.append(score)
                st.session_state.answers.append(answer)
                st.session_state.current_q += 1
                st.rerun()
            else:
                st.warning("Please provide an answer")
    else:
        st.session_state.stage = "report"
        st.rerun()

# -----------------------------
# REPORT STAGE
# -----------------------------
elif st.session_state.stage == "report":
    st.subheader("Candidate Evaluation Report")

    resume_score = st.session_state.get("resume_score", 50)

    assessment_score = calculate_assessment_score(
        st.session_state.answer_scores
    )

    skill_count = len(st.session_state.candidate.get("tech_stack", []))

    final_score = calculate_final_score(
        resume_score,
        assessment_score,
        skill_count
    )

    decision = hiring_recommendation(final_score)

    st.write(f"Resume Score: {resume_score} / 100")
    st.write(f"Technical Assessment Score: {assessment_score} / 100")
    st.write(f"Final Candidate Score: {round(final_score, 2)}")

    if decision == "Strong Hire":
        st.success(f"Hiring Recommendation: {decision}")
    elif decision == "Hire":
        st.info(f"Hiring Recommendation: {decision}")
    elif decision == "Borderline":
        st.warning(f"Hiring Recommendation: {decision}")
    else:
        st.error(f"Hiring Recommendation: {decision}")

    # -----------------------------
    # EXPORT REPORT
    # -----------------------------
    st.subheader("Export Report")
    pdf_path = generate_pdf_report(
        st.session_state.candidate,
        resume_score,
        assessment_score,
        final_score,
        decision
    )

    with open(pdf_path, "rb") as f:
        st.download_button(
            label="Download Candidate Report",
            data=f,
            file_name="candidate_report.pdf",
            mime="application/pdf"
        )
from models.llm_manager import ask_llm


def analyze_resume_quality(resume_text, tech_stack):
    """
    AI-based resume scoring using LLM.
    """

    prompt = f"""
You are a technical hiring expert.

Analyze the following resume text and evaluate the candidate.

Score the resume from 0 to 100 based on:

1. Technical skills relevance
2. Project experience
3. Professional experience
4. Resume clarity and structure
5. Overall technical strength

Detected tech stack:
{tech_stack}

Resume text:
{resume_text[:3000]}

Return your answer exactly in this format:

Score: <number>

Feedback:
- point 1
- point 2
- point 3
"""

    result = ask_llm(prompt)

    score = 50
    feedback = []

    lines = result.split("\n")

    for line in lines:
        if "Score" in line:
            try:
                score = int(line.split(":")[1].strip())
            except:
                score = 50

        if line.strip().startswith("-"):
            feedback.append(line.replace("-", "").strip())

    if not feedback:
        feedback = ["AI analysis completed"]

    return {
        "resume_score": score,
        "feedback": feedback
    }

from models.llm_manager import ask_llm
import re


def evaluate_answer(question, answer):
    """
    Evaluates both descriptive and MCQ answers.
    Returns a score from 0 to 10.
    """

    is_mcq = "A)" in question and "B)" in question

    if is_mcq:
        prompt = f"""
You are a senior technical interviewer.

The following is a multiple-choice question.

Question:
{question}

Candidate Selected Answer:
{answer}

Check whether the selected answer is correct.

Scoring Rules:
- Correct answer -> Score: 10
- Incorrect answer -> Score: 0

Return exactly in this format:
Score: <number>
"""
    else:
        prompt = f"""
You are a senior technical interviewer.

Evaluate the candidate's answer.

Question:
{question}

Candidate Answer:
{answer}

Score the answer from 0 to 10 based on:
- correctness
- clarity
- technical depth

Return exactly in this format:
Score: <number>
"""

    result = ask_llm(prompt)

    score = 5  # default fallback

    for line in result.split("\n"):
        if "score" in line.lower():
            match = re.search(r"\d+", line)
            if match:
                try:
                    score = int(match.group())
                except:
                    score = 5

    score = max(0, min(score, 10))

    return score
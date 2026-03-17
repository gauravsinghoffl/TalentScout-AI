def calculate_final_score(resume_score, interview_score, skill_count):

    skill_score = min(skill_count * 10, 100)

    final_score = (
        resume_score * 0.4 +
        interview_score * 0.4 +
        skill_score * 0.2
    )

    return round(final_score, 2)


def hiring_recommendation(final_score):

    if final_score >= 85:
        return "Strong Hire"

    elif final_score >= 70:
        return "Hire"

    elif final_score >= 55:
        return "Borderline"

    else:
        return "Reject"

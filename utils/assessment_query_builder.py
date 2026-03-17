def build_assessment_query(candidate_profile):

    role = candidate_profile.get("role", "Software Engineer")
    experience = candidate_profile.get("experience", "0-1")
    skills = ", ".join(candidate_profile.get("skills", []))

    difficulty_map = {
        "0-1": "easy",
        "2-3": "easy to medium",
        "4-6": "medium",
        "7-10": "medium to hard",
        "10+": "hard"
    }

    difficulty = difficulty_map.get(experience, "medium")

    return f"""
Technical assessment questions for {role}.
Skills: {skills}.
Experience: {experience} years.
Difficulty: {difficulty}.
"""
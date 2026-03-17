def calculate_assessment_score(answer_scores):
    """
    Calculates overall technical assessment score.
    """

    if not answer_scores:
        return 0

    total = sum(answer_scores)

    max_score = len(answer_scores) * 10

    percentage = (total / max_score) * 100

    return round(percentage, 2)

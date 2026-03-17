import json

def generate_report(candidate_data, questions, answers):

    report = {
        "candidate": candidate_data,
        "questions": questions,
        "answers": answers
    }

    return report


def save_report(report):

    with open("data/candidates.json", "a") as f:
        json.dump(report, f)
        f.write("\n")

def hiring_decision(score):

    if score > 85:
        return "Strong Hire"

    elif score > 70:
        return "Hire"

    elif score > 50:
        return "Maybe"

    else:
        return "Reject"

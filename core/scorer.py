from core.matcher import match_keywords


def score_email(subject, body, rules):
    text = subject + " " + body
    scores = {}

    for label, keywords in rules.items():
        score = match_keywords(text, keywords)
        scores[label] = score

    return scores


if __name__ == "__main__":
    from core.rules import rules

    subject = "Online Assessment — Round 2"
    body = "We would like to invite you for a coding round"

    scores = score_email(subject, body, rules)
    print(scores)

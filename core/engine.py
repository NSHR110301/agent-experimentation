from core.scorer import score_email


def classify_email(subject, body, rules):
    scores = score_email(subject, body, rules)

    # pick label with highest score
    best_label = max(scores, key=scores.get)
    best_score = scores[best_label]

    # handle no match case
    if best_score == 0:
        return "Uncategorized"

    return best_label


if __name__ == "__main__":
    from core.rules import rules

    subject = "Submit documents by Friday"
    body = "Please submit before the deadline"

    label = classify_email(subject, body, rules)
    print(label)

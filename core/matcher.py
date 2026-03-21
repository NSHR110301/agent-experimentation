def match_keywords(text, keywords):
    text = text.lower()
    score = 0

    for keyword in keywords:
        keyword = keyword.lower()

        if keyword in text:
            score += 1

    return score


if __name__ == "__main__":
    text = "We would like to invite you for an interview"
    keywords = ["interview", "deadline"]

    print(match_keywords(text, keywords))  # expect 1

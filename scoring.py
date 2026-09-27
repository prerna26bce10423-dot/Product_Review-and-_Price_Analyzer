def calculate_score(review, rating):

    score = 0

    suspicious_words = [
        "best",
        "perfect",
        "amazing",
        "excellent",
        "must buy",
        "highly recommended",
        "awesome",
        "incredible"
    ]

    review_lower = review.lower()

    # Suspicious words
    for word in suspicious_words:
        if word in review_lower:
            score += 1

    # Too many exclamation marks
    if review.count("!") >= 3:
        score += 1

    # Very short review
    if len(review.split()) < 5:
        score += 1

    # Very high rating with suspicious patterns
    if rating == 5 and score >= 2:
        score += 1

    return score
from text_preprocessor import clean_text


def analyze_review(review, rating):
    cleaned_review = clean_text(review)

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

    score = 0

    # Check suspicious promotional words
    for word in suspicious_words:
        if word in cleaned_review:
            score += 1

    # Check repeated exclamation marks
    if review.count("!") >= 3:
        score += 1

    # Check very short review
    if len(cleaned_review.split()) < 5:
        score += 1

    # Rating + exaggerated review
    if rating == 5 and score >= 2:
        score += 1

    # Final result
    if score <= 1:
        result = "🟢 REVIEW LOOKS RELATIVELY TRUSTWORTHY"
    elif score <= 3:
        result = "🟡 REVIEW NEEDS A CLOSER LOOK"
    else:
        result = "🔴 REVIEW IS POTENTIALLY SUSPICIOUS"

    return {
        "score": score,
        "result": result
    }
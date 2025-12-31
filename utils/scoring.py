def final_score(
    intent_score: float = 0,
    emotion_score: float = 0,
    cta_score: float = 0,
    text_quality_score: float = 0,
    similarity_score: float = None
) -> int:
    """
    Compute final Ad Performance Score (0-100)
    Scores are expected between 0 and 1 (or 0-100 if already scaled)
    similarity_score is optional (0-100)
    """

    # Scale 0-1 inputs to 0-100
    intent_score = intent_score * 100 if intent_score <= 1 else intent_score
    emotion_score = emotion_score * 100 if emotion_score <= 1 else emotion_score
    cta_score = cta_score * 100 if cta_score <= 1 else cta_score
    text_quality_score = text_quality_score * 100 if text_quality_score <= 1 else text_quality_score

    # Weighted scoring (adjustable)
    weights = {
        "intent": 0.3,
        "emotion": 0.25,
        "cta": 0.2,
        "text_quality": 0.15,
        "similarity": 0.1
    }

    total_score = (
        intent_score * weights["intent"] +
        emotion_score * weights["emotion"] +
        cta_score * weights["cta"] +
        text_quality_score * weights["text_quality"]
    )

    # Include similarity if available
    if similarity_score is not None:
        total_score += similarity_score * weights["similarity"]

    # Clamp between 0-100
    total_score = max(min(total_score, 100), 0)

    return round(total_score)

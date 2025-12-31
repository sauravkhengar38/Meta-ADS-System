def optimize_copy(ad_text: str):
    """
    Provides actionable suggestions to improve ad captions.
    Rule-based, no training required.
    """

    if not ad_text or len(ad_text.strip()) == 0:
        return ["Ad text is empty, please provide text."]

    suggestions = []

    # Suggest shortening long captions
    word_count = len(ad_text.split())
    if word_count > 20:
        suggestions.append("Consider shortening the caption (under 20 words).")

    # Add urgency if missing
    urgency_words = ["now", "today", "limited", "hurry", "exclusive", "offer"]
    if not any(word in ad_text.lower() for word in urgency_words):
        suggestions.append("Add urgency words like 'now', 'limited', 'exclusive'.")

    # Check for punctuation / excitement
    if "!" not in ad_text:
        suggestions.append("Add punctuation or exclamation marks for excitement.")

    # Suggest including a CTA if missing
    cta_words = ["buy", "shop", "order", "download", "register", "sign up"]
    if not any(word in ad_text.lower() for word in cta_words):
        suggestions.append("Include a clear call-to-action (CTA) in your caption.")

    # Suggest adding emotional trigger words
    emotional_words = ["amazing", "best", "incredible", "free", "surprise"]
    if not any(word in ad_text.lower() for word in emotional_words):
        suggestions.append("Consider adding emotional trigger words to attract attention.")

    # If no suggestions, compliment the copy
    if len(suggestions) == 0:
        suggestions.append("Your caption follows best practices!")

    return suggestions

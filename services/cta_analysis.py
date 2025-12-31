import re

# High-performing CTA keywords (marketing proven)
STRONG_CTA = [
    "buy now", "shop now", "order now", "get started",
    "sign up", "register", "download now", "limited offer",
    "claim now", "book now", "subscribe", "grab now"
]

MEDIUM_CTA = [
    "learn more", "discover", "find out", "see more",
    "explore", "know more", "view details"
]

WEAK_CTA = [
    "click here", "visit us", "check this",
    "read more", "watch now"
]

def analyze_cta(ad_text: str):
    """
    Analyze CTA strength inside ad copy
    Returns CTA score and insights
    """

    if not ad_text or len(ad_text.strip()) == 0:
        return {"error": "Empty ad text"}

    text = ad_text.lower()

    found_strong = [cta for cta in STRONG_CTA if cta in text]
    found_medium = [cta for cta in MEDIUM_CTA if cta in text]
    found_weak = [cta for cta in WEAK_CTA if cta in text]

    score = 0

    # Scoring logic
    score += len(found_strong) * 10
    score += len(found_medium) * 5
    score += len(found_weak) * 2

    # Penalty if no CTA
    if not (found_strong or found_medium or found_weak):
        score -= 10

    score = max(min(score, 100), 0)

    return {
        "cta_score": score,
        "found_strong_cta": found_strong,
        "found_medium_cta": found_medium,
        "found_weak_cta": found_weak,
        "has_cta": score > 0
    }

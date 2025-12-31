from transformers import pipeline

# Load pretrained Zero-Shot Classification model
# This model is already trained — NO custom data required
classifier = pipeline(
    task="zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# Marketing / Ads-specific labels
DEFAULT_LABELS = [
    "Brand Awareness",
    "Lead Generation",
    "Sales Promotion",
    "Product Launch",
    "Discount Offer",
    "Emotional Appeal",
    "Urgency Driven",
    "Trust Building",
    "Social Proof",
    "Call To Action Focused"
]

def analyze_ad_intent(ad_text: str, labels: list = DEFAULT_LABELS):
    """
    Analyze ad caption text using Zero-Shot Learning
    Returns intent labels with confidence scores
    """

    if not ad_text or len(ad_text.strip()) == 0:
        return {"error": "Empty ad text"}

    result = classifier(
        sequences=ad_text,
        candidate_labels=labels,
        multi_label=True
    )

    response = []
    for label, score in zip(result["labels"], result["scores"]):
        response.append({
            "label": label,
            "confidence": round(score, 3)
        })

    return {
        "ad_text": ad_text,
        "analysis": response
    }

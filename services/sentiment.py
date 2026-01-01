from transformers import pipeline

# Pretrained emotion detection model
# No training required
emotion_classifier = pipeline(
    task="text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def analyze_emotion(ad_text: str):
    """
    Analyze emotional tone of an ad caption
    Returns emotion scores
    """

    if not ad_text or len(ad_text.strip()) == 0:
        return {"error": "Empty ad text"}

    result = emotion_classifier(ad_text)[0]

    emotions = []
    for item in result:
        emotions.append({
            "emotion": item["label"],
            "confidence": round(item["score"], 3)
        })
def detect_emotion(text: str):
    return sentiment_pipeline(text)
from transformers import pipeline

sentiment_pipeline = pipeline(
    "text-classification",
    model="cardiffnlp/twitter-roberta-base-emotion",
    top_k=None
)

def detect_emotion(text: str):
    """
    Returns emotion scores for input text
    """
    return sentiment_pipeline(text)


    # Sort by highest confidence
    emotions = sorted(emotions, key=lambda x: x["confidence"], reverse=True)

    return {
        "ad_text": ad_text,
        "emotions": emotions
    }

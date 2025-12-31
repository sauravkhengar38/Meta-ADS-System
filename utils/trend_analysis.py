from collections import Counter
import re

def extract_keywords(texts):
    words = []
    for t in texts:
        clean = re.sub(r"[^a-zA-Z ]", "", t.lower())
        words.extend(clean.split())
    return Counter(words)

def market_trends(ads):
    texts = [ad["ad_creative_body"] for ad in ads]

    keyword_freq = extract_keywords(texts)

    top_keywords = [
        word for word, count in keyword_freq.items()
        if count > 2 and len(word) > 3
    ][:10]

    return {
        "total_ads": len(ads),
        "top_keywords": top_keywords
    }

from sentence_transformers import SentenceTransformer, util

# Pretrained embedding model (NO training needed)
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity(base_ad: str, competitor_ads: list):
    """
    Compare one ad caption with multiple competitor ads
    Returns similarity scores
    """

    if not base_ad or not competitor_ads:
        return {"error": "Base ad or competitor ads missing"}

    # Encode base ad
    base_embedding = model.encode(base_ad, convert_to_tensor=True)

    results = []

    for ad in competitor_ads:
        competitor_embedding = model.encode(ad, convert_to_tensor=True)

        score = util.cos_sim(base_embedding, competitor_embedding).item()

        results.append({
            "competitor_ad": ad,
            "similarity_score": round(score * 100, 2)  # percentage
        })

    # Sort highest similarity first
    results = sorted(results, key=lambda x: x["similarity_score"], reverse=True)

    return {
        "base_ad": base_ad,
        "comparisons": results
    }

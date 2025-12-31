import requests
import os

META_ADS_TOKEN = os.getenv("EAAVtBlZBaes0BQZAfPSf7ZBO7Yv0WjULDVn3zZAwvgbdvCtU24x9MNG8rxGArSXDg4GFZBB3GBJOs5qblEU6BKCNx9GypIZAcneDRnuZBfkLYEWDZAMnzqblUUVNtPSjul792ZBuorTN36XHgqZCsOlFox4rsyYnw9Kjl2u244lfWsGZC4oCNIEwjslyljVryVXOY5W1LRiZAbnZCrMQ6GLdkkmKqJTkuLKKjrQxnPcnl7xCopI44nF1Moa3wtP1e61TQAoXc1UvdkEvllaJg7ircBzwYpILl")
BASE_URL = "https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=IN&is_targeted_country=false&media_type=all"

def fetch_live_ads(keyword, country="IN", limit=20):
    if not META_ADS_TOKEN:
        raise ValueError("META_ADS_TOKEN not set")

    params = {
        "search_terms": keyword,
        "ad_reached_countries": country,
        "ad_type": "ALL",
        "fields": (
            "page_name,"
            "ad_creative_body,"
            "ad_creative_link_title,"
            "ad_delivery_start_time"
        ),
        "limit": limit,
        "access_token": META_ADS_TOKEN
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    ads = response.json().get("data", [])
    return [ad for ad in ads if ad.get("ad_creative_body")]

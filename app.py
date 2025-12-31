import streamlit as st
import os
import warnings
from warnings import filterwarnings

# ---------- Services ----------
from services.zero_shot import classify_intent
from services.sentiment import detect_emotion
from services.similarity import text_quality_score
from services.cta_analysis import cta_strength
from services.copy_optimizer import optimize_copy
from services.meta_ads_api import fetch_live_ads

# ---------- Utils ----------
from utils.scoring import final_score
from utils.trend_analysis import market_trends


# ---------- Page Config ----------
st.set_page_config(
    page_title="Meta AI Ads Intelligence Tool",
    page_icon="📢",
    layout="wide"
)

st.title("📢 Meta AI Ads Intelligence Tool")
st.caption("Live Meta Ads • Market Trends • AI Creative Analysis")


# ---------- Sidebar ----------
menu = st.sidebar.radio(
    "Navigation",
    [
        "📊 Overview",
        "🎯 Analyze My Ad",
        "🧠 Live Competitor Ads",
        "⚠️ Ad Fatigue Checker",
        "✍️ Copy Optimizer",
        "ℹ️ About"
    ]
)


# =========================================================
# 📊 OVERVIEW
# =========================================================
if menu == "📊 Overview":
    st.subheader("What does this tool do?")

    st.write(
        """
        This platform combines **Meta Ads Library live data** with **pretrained AI models**
        to analyze ad creatives, market trends, and competitor messaging — without using
        any historical performance data.
        """
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Live Meta Ads", "Yes")
    col2.metric("Model Training", "Not Required")
    col3.metric("Analysis Type", "Real-Time")

    st.info("🔒 No ads are stored. All analysis runs on demand.")


# =========================================================
# 🎯 ANALYZE USER AD
# =========================================================
elif menu == "🎯 Analyze My Ad":
    st.subheader("Analyze Your Ad Creative")

    col1, col2 = st.columns(2)

    with col1:
        caption = st.text_area("Ad Caption / Primary Text", height=150)
        cta = st.selectbox(
            "Call To Action",
            ["Buy Now", "Shop Now", "Learn More", "DM Us", "Sign Up", "Check It Out"]
        )
        analyze = st.button("Analyze Ad")

    with col2:
        if analyze and caption.strip():
            with st.spinner("Running AI analysis..."):
                intent = classify_intent(caption)
                emotion = detect_emotion(caption)
                quality = text_quality_score(caption)
                cta_score = cta_strength(cta)

                score = final_score(
                    intent["score"],
                    emotion["score"],
                    cta_score,
                    quality
                )

            st.metric("Performance Score", f"{score}/100")

            if score >= 75:
                st.success("🟢 Low Risk – Ready to Run")
            elif score >= 50:
                st.warning("🟡 Medium Risk – Needs Optimization")
            else:
                st.error("🔴 High Risk – Likely Budget Waste")

            st.progress(score / 100)

            st.markdown("### 🔍 AI Insights")
            st.write(f"**Intent:** {intent['label']}")
            st.write(f"**Emotion:** {emotion['emotion']}")
            st.write(f"**CTA Strength:** {round(cta_score * 100)}%")
            st.write(f"**Text Quality:** {round(quality * 100)}%")


# =========================================================
# 🧠 LIVE COMPETITOR ADS (META ADS LIBRARY)
# =========================================================
elif menu == "🧠 Live Competitor Ads":
    st.subheader("Live Competitor Ads (Meta Ads Library)")

    keyword = st.text_input("Search Keyword / Brand / Product")
    country = st.selectbox("Country", ["IN", "US", "UK", "AE"])

    if st.button("Fetch Live Ads"):
        try:
            with st.spinner("Fetching live ads from Meta Ads Library..."):
                ads = fetch_live_ads(keyword, country)

            if not ads:
                st.warning("No ads found for this keyword.")
            else:
                st.success(f"Fetched {len(ads)} live ads")

                # ---------- Market Trends ----------
                trends = market_trends(ads)

                st.markdown("### 📊 Market Trend Analysis")
                st.write("**Total Live Ads:**", trends["total_ads"])
                st.write("**Trending Keywords:**", ", ".join(trends["top_keywords"]))

                st.divider()

                # ---------- Show Ads + AI Analysis ----------
                for ad in ads[:5]:
                    st.markdown(f"### 🏷️ {ad['page_name']}")
                    st.write(ad["ad_creative_body"])

                    intent = classify_intent(ad["ad_creative_body"])
                    emotion = detect_emotion(ad["ad_creative_body"])

                    st.caption(
                        f"Intent: {intent['label']} | "
                        f"Emotion: {emotion['emotion']}"
                    )

                    st.divider()

        except Exception as e:
            st.error(f"Error fetching ads: {e}")


# =========================================================
# ⚠️ AD FATIGUE CHECKER
# =========================================================
elif menu == "⚠️ Ad Fatigue Checker":
    st.subheader("Ad Fatigue Risk Estimator")

    caption = st.text_area("Ad Caption", height=120)
    days = st.slider("Planned Run Duration (Days)", 1, 30, 7)
    frequency = st.slider("Estimated Frequency", 1.0, 5.0, 2.0)

    if st.button("Check Fatigue"):
        fatigue_risk = min((days * frequency) / 30, 1.0)

        st.metric("Fatigue Risk", f"{round(fatigue_risk * 100)}%")
        st.progress(fatigue_risk)

        if fatigue_risk > 0.7:
            st.error("High Fatigue Risk – Refresh Creative")
        elif fatigue_risk > 0.4:
            st.warning("Medium Risk – Monitor Performance")
        else:
            st.success("Low Risk – Safe to Run")


# =========================================================
# ✍️ COPY OPTIMIZER
# =========================================================
elif menu == "✍️ Copy Optimizer":
    st.subheader("AI Copy Optimization")

    caption = st.text_area("Original Caption", height=150)

    if st.button("Get Suggestions") and caption.strip():
        tips = optimize_copy(caption)

        if tips:
            st.markdown("### ✨ Optimization Suggestions")
            for tip in tips:
                st.write("•", tip)
        else:
            st.success("Your caption already follows best practices!")


# =========================================================
# ℹ️ ABOUT
# =========================================================
elif menu == "ℹ️ About":
    st.subheader("About This Project")

    st.write(
        """
        **Meta AI Ads Intelligence Tool** is a real-time marketing intelligence platform.

        ### Key Capabilities
        - Live Meta Ads Library integration
        - Market trend analysis
        - Zero-shot intent classification
        - Emotion detection
        - No model training or historical data

        ### Tech Stack
        - Python
        - Streamlit
        - HuggingFace Transformers
        - Meta Ads Library API
        """
    )

from src.state import InvestmentState


# ============================================================
# FINAL INVESTMENT ANALYST
# ============================================================

def final_analyst(state: InvestmentState) -> InvestmentState:

    print("\n")
    print("=" * 60)
    print("FINAL INVESTMENT ANALYST")
    print("=" * 60)

    # ========================================================
    # GET DATA
    # ========================================================

    ticker = state.get("ticker", "UNKNOWN")

    market_data = state.get(
        "market_data",
        {}
    )

    news_data = state.get(
        "news_data",
        []
    )

    research_data = state.get(
        "research_data",
        []
    )

    technical_analysis = state.get(
        "technical_analysis",
        {}
    )

    risk_analysis = state.get(
        "risk_analysis",
        {}
    )

    # ========================================================
    # MARKET DATA
    # ========================================================

    company_name = market_data.get(
        "company_name",
        ticker
    )

    price = market_data.get(
        "price"
    )

    market_cap = market_data.get(
        "market_cap"
    )

    pe_ratio = market_data.get(
        "pe_ratio"
    )

    volume = market_data.get(
        "volume"
    )

    # ========================================================
    # TECHNICAL DATA
    # ========================================================

    technical_trend = technical_analysis.get(
        "trend",
        "Unknown"
    )

    current_price = technical_analysis.get(
        "current_price",
        price
    )

    sma_20 = technical_analysis.get(
        "sma_20"
    )

    sma_50 = technical_analysis.get(
        "sma_50"
    )

    sma_200 = technical_analysis.get(
        "sma_200"
    )

    six_month_high = technical_analysis.get(
        "six_month_high"
    )

    six_month_low = technical_analysis.get(
        "six_month_low"
    )

    # ========================================================
    # RISK DATA
    # ========================================================

    risk_level = risk_analysis.get(
        "risk_level",
        "Unknown"
    )

    risks = risk_analysis.get(
        "risks",
        []
    )

    # ========================================================
    # SCORING SYSTEM
    # ========================================================

    score = 0

    max_score = 10

    score_reasons = []

    # ========================================================
    # VALUATION
    # ========================================================

    if pe_ratio is not None:

        try:

            pe = float(pe_ratio)

            if pe < 20:

                score += 3

                score_reasons.append(
                    "Valuation is attractive based on P/E."
                )

            elif pe < 30:

                score += 2

                score_reasons.append(
                    "Valuation appears reasonable."
                )

            elif pe < 40:

                score += 1

                score_reasons.append(
                    "Valuation is relatively expensive."
                )

            else:

                score -= 1

                score_reasons.append(
                    "Valuation is expensive."
                )

        except (
            TypeError,
            ValueError
        ):

            score_reasons.append(
                "P/E ratio could not be evaluated."
            )

    else:

        score_reasons.append(
            "P/E ratio unavailable."
        )

    # ========================================================
    # TECHNICAL ANALYSIS
    # ========================================================

    if technical_trend == "Bullish":

        score += 3

        score_reasons.append(
            "Technical trend is bullish."
        )

    elif technical_trend == "Mixed":

        score += 1

        score_reasons.append(
            "Technical trend is mixed."
        )

    elif technical_trend == "Bearish":

        score -= 2

        score_reasons.append(
            "Technical trend is bearish."
        )

    else:

        score_reasons.append(
            "Technical trend unavailable."
        )

    # ========================================================
    # RISK ANALYSIS
    # ========================================================

    if risk_level == "Low":

        score += 2

        score_reasons.append(
            "Risk level is low."
        )

    elif risk_level == "Low to Moderate":

        score += 1

        score_reasons.append(
            "Risk level is low to moderate."
        )

    elif risk_level == "Moderate":

        score += 0

        score_reasons.append(
            "Risk level is moderate."
        )

    elif risk_level == "High":

        score -= 2

        score_reasons.append(
            "Risk level is high."
        )

    else:

        score_reasons.append(
            "Risk level unavailable."
        )

    # ========================================================
    # NEWS RESEARCH
    # ========================================================

    news_count = len(news_data)

    if news_count >= 5:

        score += 1

        score_reasons.append(
            "Multiple recent news sources were analyzed."
        )

    elif news_count > 0:

        score += 0

        score_reasons.append(
            "Some recent news was available."
        )

    else:

        score_reasons.append(
            "No recent news was available."
        )

    # ========================================================
    # FUNDAMENTAL RESEARCH
    # ========================================================

    fundamental_count = len(research_data)

    if fundamental_count > 0:

        score += 1

        score_reasons.append(
            "Fundamental research data was available."
        )

    else:

        score_reasons.append(
            "Fundamental research was unavailable."
        )

    # ========================================================
    # VERDICT
    # ========================================================

    if score >= 7:

        verdict = "BUY"

    elif score >= 4:

        verdict = "HOLD"

    elif score >= 1:

        verdict = "CAUTIOUS HOLD"

    else:

        verdict = "AVOID / WAIT"

    # ========================================================
    # CONFIDENCE
    # ========================================================

    research_sources = 0

    if market_data:
        research_sources += 1

    if news_data:
        research_sources += 1

    if research_data:
        research_sources += 1

    if technical_analysis:
        research_sources += 1

    if risk_analysis:
        research_sources += 1

    confidence = 50 + (
        research_sources * 8
    )

    # Keep confidence between 50 and 90
    confidence = min(
        90,
        max(
            50,
            confidence
        )
    )

    # ========================================================
    # MARKET CAP FORMAT
    # ========================================================

    if market_cap is not None:

        market_cap_text = (
            f"${float(market_cap) / 1_000_000_000_000:.2f} trillion"
        )

    else:

        market_cap_text = "Unavailable"

    # ========================================================
    # PRICE FORMAT
    # ========================================================

    if price is not None:

        price_text = (
            f"${float(price):.2f}"
        )

    else:

        price_text = "Unavailable"

    # ========================================================
    # P/E FORMAT
    # ========================================================

    if pe_ratio is not None:

        pe_text = (
            f"{float(pe_ratio):.2f}"
        )

    else:

        pe_text = "Unavailable"

    # ========================================================
    # TECHNICAL SUMMARY
    # ========================================================

    technical_summary = ""

    if sma_20 is not None:

        technical_summary += (
            f"- 20-day SMA: ${float(sma_20):.2f}\n"
        )

    if sma_50 is not None:

        technical_summary += (
            f"- 50-day SMA: ${float(sma_50):.2f}\n"
        )

    if sma_200 is not None:

        technical_summary += (
            f"- 200-day SMA: ${float(sma_200):.2f}\n"
        )

    if six_month_high is not None:

        technical_summary += (
            f"- 6-month high: ${float(six_month_high):.2f}\n"
        )

    if six_month_low is not None:

        technical_summary += (
            f"- 6-month low: ${float(six_month_low):.2f}\n"
        )

    if not technical_summary:

        technical_summary = (
            "Technical indicators unavailable.\n"
        )

    # ========================================================
    # RISK SUMMARY
    # ========================================================

    risk_summary = ""

    if risks:

        for risk in risks:

            risk_summary += (
                f"- {risk}\n"
            )

    else:

        risk_summary = (
            "- No specific risks returned.\n"
        )

    # ========================================================
    # NEWS SUMMARY
    # ========================================================

    news_summary = ""

    for index, article in enumerate(
        news_data[:5],
        start=1
    ):

        title = article.get(
            "title",
            "Untitled"
        )

        published = article.get(
            "published_date",
            ""
        )

        news_summary += (
            f"{index}. {title}"
        )

        if published:

            news_summary += (
                f" ({published})"
            )

        news_summary += "\n"

    if not news_summary:

        news_summary = (
            "No recent news articles available.\n"
        )

    # ========================================================
    # POSITIVE FACTORS
    # ========================================================

    positive_factors = """
- Large and established company ecosystem.
- Strong brand recognition and customer base.
- Hardware, software, and services diversification.
- Significant financial resources.
- Large market capitalization and established business operations.
"""

    # ========================================================
    # FINAL REPORT
    # ========================================================

    report = f"""
# INVESTMENT RESEARCH REPORT

## Asset

{company_name} ({ticker})

## Current Price

{price_text}

## Investment Verdict

### {verdict}

## Confidence

{confidence}%

## Overall Score

{score}/{max_score + 3}

---

## Valuation

P/E Ratio: {pe_text}

Market Capitalization: {market_cap_text}

Volume: {volume if volume is not None else "Unavailable"}

---

## Technical Analysis

Trend: **{technical_trend}**

Current Price:
{f"${float(current_price):.2f}" if current_price is not None else "Unavailable"}

{technical_summary}

---

## Risk Analysis

Risk Level: **{risk_level}**

{risk_summary}

---

## News Research

Number of News Articles Analyzed:

{len(news_data)}

### Recent Articles

{news_summary}

---

## Fundamental Research

Fundamental research records collected:

{len(research_data)}

---

## Investment Considerations

### Positive Factors

{positive_factors}

### Risk Factors

- Valuation may be expensive relative to earnings growth.
- Technology-sector declines could affect the stock.
- Competition may pressure future growth.
- Product cycles can affect revenue.
- Regulatory and supply-chain risks remain important.
- Future returns depend on continued earnings and revenue growth.

---

## Automated Scoring

"""

    for reason in score_reasons:

        report += (
            f"- {reason}\n"
        )

    report += f"""

---

## Conclusion

Based on the available market data, news,
fundamental research, technical analysis,
and risk analysis, the automated assessment is:

# {verdict}

The system assigns a confidence level of
{confidence}% to this assessment.

This is an automated research assessment and
should not be considered personalized financial advice.

---

## Data Summary

### Market Data

{market_data}

### Technical Analysis

{technical_analysis}

### Risk Analysis

{risk_analysis}

### News Articles

{len(news_data)}

### Fundamental Research

{research_data}
"""

    # ========================================================
    # PRINT REPORT
    # ========================================================

    print(report)

    print("\n")
    print("=" * 60)
    print("FINAL ANALYSIS COMPLETE")
    print("=" * 60)

    # ========================================================
    # RETURN STATE
    # ========================================================

    return {
        **state,
        "final_analysis": report
    }
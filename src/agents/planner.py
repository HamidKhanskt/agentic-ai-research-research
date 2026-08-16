import os
import re

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from src.state import InvestmentState


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()


# ============================================================
# GROQ MODEL
# ============================================================

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# ============================================================
# PLANNER AGENT
# ============================================================

def planner_agent(state: InvestmentState) -> InvestmentState:

    question = state.get("question", "").strip()

    print("\n")
    print("=" * 60)
    print("PLANNER AGENT")
    print("=" * 60)

    print("\nUser question:")
    print(question)

    # ========================================================
    # PLANNER PROMPT
    # ========================================================

    prompt = f"""
You are an investment research planning agent.

The user asked:

{question}

Your job is to identify the company or asset and decide
which research agents are required.

Available research agents:

1. MARKET_DATA
   Current price, volume, market cap, P/E ratio.

2. NEWS
   Recent financial news and events.

3. FUNDAMENTAL_RESEARCH
   Company financial health, business quality,
   revenue, earnings, valuation and growth.

4. TECHNICAL_ANALYSIS
   Price trends, moving averages and historical price levels.

5. RISK_ANALYSIS
   Investment risks and downside factors.

For a stock investment question, normally request ALL
five research categories.

Return your response using exactly this structure:

ASSET:
<company name and ticker if known>

RESEARCH_REQUIRED:
- MARKET_DATA
- NEWS
- FUNDAMENTAL_RESEARCH
- TECHNICAL_ANALYSIS
- RISK_ANALYSIS

REASON:
<short explanation>

Do not provide an investment recommendation.
Only create the research plan.
"""

    # ========================================================
    # CALL GROQ
    # ========================================================

    response = llm.invoke(prompt)

    plan = response.content

    print("\nPlanner decision:")
    print(plan)

    # ========================================================
    # EXTRACT TICKER
    # ========================================================

    ticker = extract_ticker(plan, question)

    print("\nExtracted ticker:")
    print(ticker)

    # ========================================================
    # RESEARCH REQUIREMENTS
    # ========================================================

    research_required = [
        "MARKET_DATA",
        "NEWS",
        "FUNDAMENTAL_RESEARCH",
        "TECHNICAL_ANALYSIS",
        "RISK_ANALYSIS"
    ]

    print("\nResearch agents required:")

    for agent in research_required:
        print(f"→ {agent}")

    # ========================================================
    # RETURN UPDATED STATE
    # ========================================================

    return {
        **state,
        "plan": plan,
        "ticker": ticker,
        "research_required": research_required
    }


# ============================================================
# TICKER EXTRACTION
# ============================================================

def extract_ticker(plan: str, question: str) -> str:

    text = f"{plan} {question}".lower()

    # --------------------------------------------------------
    # Known companies
    # --------------------------------------------------------

    company_map = {
        "apple": "AAPL",
        "microsoft": "MSFT",
        "google": "GOOGL",
        "alphabet": "GOOGL",
        "amazon": "AMZN",
        "tesla": "TSLA",
        "nvidia": "NVDA",
        "meta": "META",
        "facebook": "META",
        "netflix": "NFLX",
        "amd": "AMD",
        "intel": "INTC",
        "palantir": "PLTR",
        "coinbase": "COIN",
        "berkshire": "BRK-B",
        "walmart": "WMT",
        "disney": "DIS",
        "nike": "NKE",
        "jpmorgan": "JPM",
        "visa": "V",
        "mastercard": "MA",
    }

    for company, ticker in company_map.items():

        if company in text:
            return ticker

    # --------------------------------------------------------
    # Look for ticker written in parentheses
    # Example: Apple (AAPL)
    # --------------------------------------------------------

    match = re.search(
        r"\(([A-Z]{1,5}(?:-[A-Z])?)\)",
        plan
    )

    if match:
        return match.group(1)

    # --------------------------------------------------------
    # Look for uppercase ticker
    # --------------------------------------------------------

    match = re.search(
        r"\b[A-Z]{2,5}(?:-[A-Z])?\b",
        plan
    )

    if match:
        return match.group(0)

    # --------------------------------------------------------
    # Unknown
    # --------------------------------------------------------

    return "UNKNOWN"
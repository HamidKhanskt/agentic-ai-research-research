from src.state import InvestmentState


def risk_analysis_agent(state: InvestmentState) -> InvestmentState:

    print("\n")
    print("=" * 60)
    print("RISK ANALYSIS AGENT")
    print("=" * 60)

    ticker = state.get("ticker", "UNKNOWN")

    # ============================================================
    # RISK ANALYSIS
    # ============================================================

    risk_analysis = {
        "ticker": ticker,
        "risk_level": "Low to Moderate",
        "risks": [
            "Fundamental risk: future returns depend on continued earnings and revenue growth.",
            "Market risk: a broader market or technology-sector decline could negatively affect the stock.",
            "Company-specific risk: competition, product cycles, regulation, tariffs, and supply-chain issues may affect results.",
        ],
    }

    print("\nRISK ANALYSIS:")
    print(risk_analysis)

    # ============================================================
    # RETURN UPDATED STATE
    # ============================================================

    return {
        **state,
        "risk_analysis": risk_analysis,
    }
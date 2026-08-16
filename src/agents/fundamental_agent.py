from src.state import InvestmentState


# ============================================================
# FUNDAMENTAL RESEARCH AGENT
# ============================================================

def fundamental_agent(state: InvestmentState) -> InvestmentState:

    ticker = state.get(
        "ticker",
        "UNKNOWN"
    )

    market_data = state.get(
        "market_data",
        {}
    )

    print("\n")
    print("=" * 60)
    print("FUNDAMENTAL RESEARCH AGENT")
    print("=" * 60)

    print(
        f"\nAnalyzing fundamentals for: {ticker}"
    )

    # ========================================================
    # GET MARKET DATA FROM STATE
    # ========================================================

    company_name = market_data.get(
        "company_name"
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

    currency = market_data.get(
        "currency",
        "USD"
    )

    # ========================================================
    # FALLBACK COMPANY NAME
    # ========================================================

    if not company_name:

        company_name = ticker

    # ========================================================
    # FUNDAMENTAL RESEARCH RECORD
    # ========================================================

    fundamental = {
        "type": "fundamental",
        "ticker": ticker,
        "company_name": company_name,
        "price": price,
        "market_cap": market_cap,
        "pe_ratio": pe_ratio,
        "currency": currency,
    }

    # ========================================================
    # INTERPRETATION
    # ========================================================

    observations = []

    # --------------------------------------------------------
    # P/E ANALYSIS
    # --------------------------------------------------------

    if pe_ratio is not None:

        try:

            pe = float(pe_ratio)

            if pe < 20:

                observations.append(
                    "The P/E ratio is relatively low "
                    "compared with many growth-oriented "
                    "technology companies."
                )

            elif pe < 30:

                observations.append(
                    "The P/E ratio indicates a moderate "
                    "valuation."
                )

            elif pe < 40:

                observations.append(
                    "The P/E ratio indicates a relatively "
                    "premium valuation."
                )

            else:

                observations.append(
                    "The P/E ratio indicates a high "
                    "valuation and significant growth "
                    "expectations."
                )

        except (
            TypeError,
            ValueError
        ):

            observations.append(
                "P/E ratio could not be interpreted."
            )

    else:

        observations.append(
            "P/E ratio is unavailable."
        )

    # --------------------------------------------------------
    # MARKET CAP ANALYSIS
    # --------------------------------------------------------

    if market_cap is not None:

        try:

            market_cap_value = float(
                market_cap
            )

            if market_cap_value >= 1_000_000_000_000:

                observations.append(
                    "The company has a very large "
                    "market capitalization."
                )

            elif market_cap_value >= 100_000_000_000:

                observations.append(
                    "The company has a large "
                    "market capitalization."
                )

        except (
            TypeError,
            ValueError
        ):

            pass

    # --------------------------------------------------------
    # PRICE
    # --------------------------------------------------------

    if price is not None:

        observations.append(
            f"The latest observed share price is "
            f"{currency} {float(price):.2f}."
        )

    # ========================================================
    # SAVE OBSERVATIONS
    # ========================================================

    fundamental["observations"] = observations

    # ========================================================
    # PRINT RESULTS
    # ========================================================

    print("\nFUNDAMENTAL RESEARCH:")

    print(
        f"Company: {company_name}"
    )

    print(
        f"Price: {price}"
    )

    print(
        f"Market Cap: {market_cap}"
    )

    print(
        f"P/E Ratio: {pe_ratio}"
    )

    if observations:

        print("\nObservations:")

        for observation in observations:

            print(
                f"- {observation}"
            )

    # ========================================================
    # GET EXISTING RESEARCH
    # ========================================================

    existing_research = state.get(
        "research_data",
        []
    )

    # ========================================================
    # ADD FUNDAMENTAL RESEARCH
    # ========================================================

    updated_research = [
        *existing_research,
        fundamental
    ]

    # ========================================================
    # RETURN UPDATED STATE
    # ========================================================

    return {
        **state,
        "research_data": updated_research
    }
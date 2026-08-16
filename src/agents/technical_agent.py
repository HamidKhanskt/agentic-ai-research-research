import yfinance as yf

from src.state import InvestmentState


# ============================================================
# TECHNICAL ANALYSIS AGENT
# ============================================================

def technical_agent(state: InvestmentState) -> InvestmentState:

    ticker = state.get(
        "ticker",
        ""
    ).strip().upper()

    print("\n")
    print("=" * 60)
    print("TECHNICAL ANALYSIS AGENT")
    print("=" * 60)

    print(
        f"\nRunning technical analysis for: {ticker}"
    )

    # ========================================================
    # VALIDATE TICKER
    # ========================================================

    if not ticker or ticker == "UNKNOWN":

        print(
            "ERROR: No valid ticker found."
        )

        return {
            **state,
            "technical_analysis": {}
        }

    # ========================================================
    # DOWNLOAD HISTORICAL DATA
    # ========================================================

    try:

        stock = yf.Ticker(ticker)

        history = stock.history(
            period="1y",
            interval="1d"
        )

        if history.empty:

            print(
                f"No historical data found for {ticker}"
            )

            return {
                **state,
                "technical_analysis": {}
            }

        # ====================================================
        # CLOSE PRICES
        # ====================================================

        close = history["Close"]

        # ====================================================
        # CURRENT PRICE
        # ====================================================

        current_price = float(
            close.iloc[-1]
        )

        # ====================================================
        # MOVING AVERAGES
        # ====================================================

        sma_20 = None
        sma_50 = None
        sma_200 = None

        if len(close) >= 20:

            sma_20 = float(
                close.tail(20).mean()
            )

        if len(close) >= 50:

            sma_50 = float(
                close.tail(50).mean()
            )

        if len(close) >= 200:

            sma_200 = float(
                close.tail(200).mean()
            )

        # ====================================================
        # SIX MONTH DATA
        # ====================================================

        six_month_data = history.tail(
            126
        )

        six_month_high = float(
            six_month_data["High"].max()
        )

        six_month_low = float(
            six_month_data["Low"].min()
        )

        # ====================================================
        # TREND LOGIC
        # ====================================================

        trend = "Neutral"

        if (
            sma_20 is not None
            and sma_50 is not None
            and sma_200 is not None
        ):

            if (
                current_price > sma_20
                and sma_20 > sma_50
                and sma_50 > sma_200
            ):

                trend = "Bullish"

            elif (
                current_price < sma_20
                and sma_20 < sma_50
            ):

                trend = "Bearish"

            else:

                trend = "Mixed"

        # ====================================================
        # TECHNICAL RESULT
        # ====================================================

        technical_analysis = {
            "ticker": ticker,
            "current_price": current_price,
            "sma_20": sma_20,
            "sma_50": sma_50,
            "sma_200": sma_200,
            "six_month_high": six_month_high,
            "six_month_low": six_month_low,
            "trend": trend
        }

        # ====================================================
        # PRINT RESULTS
        # ====================================================

        print("\nTECHNICAL ANALYSIS:")

        print(
            technical_analysis
        )

        # ====================================================
        # RETURN UPDATED STATE
        # ====================================================

        return {
            **state,
            "technical_analysis": technical_analysis
        }

    except Exception as e:

        print(
            f"\nTechnical analysis error: {e}"
        )

        return {
            **state,
            "technical_analysis": {}
        }
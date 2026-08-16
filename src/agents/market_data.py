import yfinance as yf

from src.state import InvestmentState


# ============================================================
# MARKET DATA AGENT
# ============================================================

def market_data_agent(state: InvestmentState) -> InvestmentState:

    ticker = state.get("ticker", "").strip().upper()

    print("\n")
    print("=" * 60)
    print("MARKET DATA AGENT")
    print("=" * 60)

    print(f"\nRequesting live market data for: {ticker}")

    # ========================================================
    # VALIDATE TICKER
    # ========================================================

    if not ticker or ticker == "UNKNOWN":

        print("ERROR: No valid ticker was found.")

        return {
            **state,
            "market_data": {}
        }

    # ========================================================
    # DOWNLOAD MARKET DATA
    # ========================================================

    try:

        stock = yf.Ticker(ticker)

        history = stock.history(
            period="5d",
            interval="1d"
        )

        if history.empty:

            print(f"No market data found for {ticker}")

            return {
                **state,
                "market_data": {}
            }

        # ====================================================
        # CURRENT PRICE
        # ====================================================

        latest = history.iloc[-1]

        price = float(latest["Close"])

        open_price = float(latest["Open"])

        high_price = float(latest["High"])

        low_price = float(latest["Low"])

        volume = int(latest["Volume"])

        # ====================================================
        # COMPANY INFORMATION
        # ====================================================

        info = {}

        try:
            info = stock.info
        except Exception:
            info = {}

        company_name = info.get(
            "longName",
            ticker
        )

        currency = info.get(
            "currency",
            "USD"
        )

        market_cap = info.get(
            "marketCap"
        )

        pe_ratio = info.get(
            "trailingPE"
        )

        # ====================================================
        # FALLBACK P/E
        # ====================================================

        if pe_ratio is None:

            pe_ratio = info.get(
                "forwardPE"
            )

        # ====================================================
        # MARKET DATA OBJECT
        # ====================================================

        market_data = {
            "ticker": ticker,
            "price": price,
            "open": open_price,
            "high": high_price,
            "low": low_price,
            "volume": volume,
            "currency": currency,
            "company_name": company_name,
            "market_cap": market_cap,
            "pe_ratio": pe_ratio
        }

        # ====================================================
        # PRINT RESULTS
        # ====================================================

        print("\nLIVE MARKET DATA:")

        print(market_data)

        # ====================================================
        # RETURN UPDATED STATE
        # ====================================================

        return {
            **state,
            "market_data": market_data
        }

    except Exception as e:

        print(
            f"\nMarket data error for {ticker}: {e}"
        )

        return {
            **state,
            "market_data": {}
        }
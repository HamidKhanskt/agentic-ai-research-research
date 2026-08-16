import feedparser
from urllib.parse import quote

from src.state import InvestmentState


# ============================================================
# NEWS AGENT
# ============================================================

def news_agent(state: InvestmentState) -> InvestmentState:

    ticker = state.get("ticker", "").strip().upper()

    print("\n")
    print("=" * 60)
    print("NEWS AGENT")
    print("=" * 60)

    print(f"\nSearching live financial news for: {ticker}")

    # ========================================================
    # VALIDATE TICKER
    # ========================================================

    if not ticker or ticker == "UNKNOWN":

        print("ERROR: No valid ticker found.")

        return {
            **state,
            "news_data": []
        }

    # ========================================================
    # GOOGLE NEWS RSS
    # ========================================================

    query = quote(
        f"{ticker} stock"
    )

    rss_url = (
        "https://news.google.com/rss/search?"
        f"q={query}&"
        "hl=en-US&"
        "gl=US&"
        "ceid=US:en"
    )

    # ========================================================
    # FETCH NEWS
    # ========================================================

    try:

        feed = feedparser.parse(
            rss_url
        )

        articles = []

        # ----------------------------------------------------
        # GET UP TO 5 ARTICLES
        # ----------------------------------------------------

        for entry in feed.entries[:5]:

            title = entry.get(
                "title",
                "Untitled"
            )

            link = entry.get(
                "link",
                ""
            )

            published = entry.get(
                "published",
                ""
            )

            summary = entry.get(
                "summary",
                ""
            )

            article = {
                "title": title,
                "url": link,
                "content": summary,
                "published_date": published
            }

            articles.append(
                article
            )

        # ====================================================
        # PRINT RESULTS
        # ====================================================

        print(
            f"\nFound {len(articles)} news articles."
        )

        for index, article in enumerate(
            articles,
            start=1
        ):

            print(
                f"\n{index}. "
                f"{article['title']}"
            )

        # ====================================================
        # RETURN UPDATED STATE
        # ====================================================

        return {
            **state,
            "news_data": articles
        }

    except Exception as e:

        print(
            f"\nNews agent error: {e}"
        )

        return {
            **state,
            "news_data": []
        }
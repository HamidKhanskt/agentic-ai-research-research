from src.graph import investment_graph


# ============================================================
# TEST INVESTMENT GRAPH
# ============================================================

def main():

    print("\n")
    print("=" * 60)
    print("AGENTIC AI INVESTMENT RESEARCH ASSISTANT")
    print("=" * 60)

    question = input(
        "\nAsk the investment research system: "
    )

    if not question.strip():

        print("\nNo question entered.")
        return

    # ========================================================
    # INITIAL STATE
    # ========================================================

    initial_state = {
        "question": question
    }

    # ========================================================
    # RUN GRAPH
    # ========================================================

    try:

        final_state = investment_graph.invoke(
            initial_state
        )

    except Exception as e:

        print("\n")
        print("=" * 60)
        print("GRAPH ERROR")
        print("=" * 60)

        print(f"\n{type(e).__name__}: {e}")

        return

    # ========================================================
    # FINAL RESULT
    # ========================================================

    print("\n")
    print("=" * 60)
    print("INVESTMENT RESEARCH COMPLETE")
    print("=" * 60)

    final_analysis = final_state.get(
        "final_analysis"
    )

    if final_analysis:

        print("\n")
        print(final_analysis)

    else:

        print("\nNo final analysis was returned.")

    # ========================================================
    # DEBUG SUMMARY
    # ========================================================

    print("\n")
    print("=" * 60)
    print("RESEARCH SUMMARY")
    print("=" * 60)

    print(
        "\nTicker:",
        final_state.get("ticker", "Unknown")
    )

    print(
        "Market data:",
        "YES" if final_state.get("market_data") else "NO"
    )

    print(
        "News articles:",
        len(final_state.get("news_data", []))
    )

    print(
        "Fundamental research:",
        len(final_state.get("research_data", []))
    )

    print(
        "Technical analysis:",
        "YES"
        if final_state.get("technical_analysis")
        else "NO"
    )

    print(
        "Risk analysis:",
        "YES"
        if final_state.get("risk_analysis")
        else "NO"
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    main()
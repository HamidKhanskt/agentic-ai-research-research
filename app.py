import streamlit as st

from src.graph import investment_graph


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Agentic AI Investment Research",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# NEON STYLE
# ============================================================

st.markdown(
    """
    <style>

    /* MAIN BACKGROUND */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 15%,
                rgba(0, 255, 200, 0.08),
                transparent 28%
            ),
            radial-gradient(
                circle at 85% 20%,
                rgba(130, 50, 255, 0.08),
                transparent 30%
            ),
            #060a10;
    }


    /* CONTENT WIDTH */

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* TITLE */

    .neon-title {
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1px;

        background: linear-gradient(
            90deg,
            #00ffc8,
            #00d9ff,
            #9b5cff
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-bottom: 5px;
    }


    .neon-subtitle {
        color: #9aaaba;
        font-size: 17px;
        line-height: 1.6;
        margin-bottom: 28px;
    }


    /* ONLINE STATUS */

    .online {
        color: #00ffc8;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin-bottom: 12px;
    }


    /* INPUT */

    div[data-baseweb="input"] {
        background-color: #0b111a;
        border: 1px solid rgba(0, 255, 200, 0.25);
        border-radius: 12px;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #00ffc8;
        box-shadow: 0 0 18px rgba(0, 255, 200, 0.15);
    }


    /* BUTTON */

    .stButton > button {
        min-height: 48px;

        border-radius: 12px;

        border: 1px solid rgba(0, 255, 200, 0.45);

        background:
            linear-gradient(
                90deg,
                rgba(0, 255, 200, 0.12),
                rgba(100, 50, 255, 0.12)
            );

        color: #00ffc8;

        font-weight: 800;

        box-shadow:
            0 0 18px rgba(0, 255, 200, 0.08);
    }


    .stButton > button:hover {
        border-color: #00ffc8;
        color: white;

        box-shadow:
            0 0 25px rgba(0, 255, 200, 0.2);
    }


    /* METRICS */

    div[data-testid="stMetric"] {
        background: #0b111a;

        border: 1px solid rgba(0, 255, 200, 0.16);

        border-radius: 15px;

        padding: 18px;

        box-shadow:
            0 0 20px rgba(0, 255, 200, 0.04);
    }


    div[data-testid="stMetricLabel"] {
        color: #8292a4 !important;
    }


    div[data-testid="stMetricValue"] {
        color: #00ffc8 !important;
        font-weight: 800;
    }


    /* EXPANDERS */

    div[data-testid="stExpander"] {
        background: #0a1018;

        border: 1px solid rgba(0, 255, 200, 0.14);

        border-radius: 14px;

        margin-bottom: 12px;
    }


    div[data-testid="stExpander"]:hover {
        border-color: rgba(0, 255, 200, 0.35);
    }


    /* DOWNLOAD BUTTON */

    div[data-testid="stDownloadButton"] button {
        border-radius: 12px;

        border: 1px solid rgba(0, 255, 200, 0.35);

        background: rgba(0, 255, 200, 0.06);

        color: #00ffc8;

        font-weight: 700;
    }


    div[data-testid="stDownloadButton"] button:hover {
        border-color: #00ffc8;

        box-shadow:
            0 0 20px rgba(0, 255, 200, 0.15);
    }


    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background: #070c13;

        border-right: 1px solid rgba(0, 255, 200, 0.12);
    }


    /* SECTION HEADINGS */

    h2,
    h3 {
        color: #00ffc8 !important;
    }


    /* DIVIDER */

    hr {
        border-color: rgba(0, 255, 200, 0.12);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## ⚡ AI RESEARCH SYSTEM"
    )

    st.caption(
        "Multi-agent investment research platform"
    )

    st.divider()

    st.markdown(
        "**Architecture**"
    )

    st.write(
        "LangGraph Multi-Agent System"
    )

    st.markdown(
        "**LLM**"
    )

    st.write(
        "Groq"
    )

    st.markdown(
        "**Market Data**"
    )

    st.write(
        "Yahoo Finance"
    )

    st.markdown(
        "**News**"
    )

    st.write(
        "Google News RSS"
    )

    st.divider()

    st.markdown(
        "**Agents**"
    )

    st.write(
        """
        🧠 Planner Agent

        📊 Market Data Agent

        📰 News Agent

        💰 Fundamental Agent

        📈 Technical Agent

        ⚠️ Risk Agent

        🤖 Final Investment Analyst
        """
    )

    st.divider()

    st.caption(
        "Automated research only. Not financial advice."
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="online">● SYSTEM ONLINE</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="neon-title">📈 Agentic AI Investment Research</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="neon-subtitle">'
    "Autonomous investment research using LangGraph, "
    "LangChain, Groq, live market data, financial news, "
    "technical analysis, fundamentals, and risk analysis."
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# QUESTION
# ============================================================

st.subheader(
    "🔎 Investment Research Query"
)

question = st.text_input(
    "Investment question",
    placeholder="Example: Should I invest in Apple now?",
    label_visibility="collapsed",
)


# ============================================================
# RUN BUTTON
# ============================================================

run_research = st.button(
    "🚀 RUN INVESTMENT RESEARCH",
    type="primary",
    use_container_width=True,
)


# ============================================================
# RUN GRAPH
# ============================================================

if run_research:

    if not question.strip():

        st.warning(
            "Please enter an investment research question."
        )

        st.stop()

    initial_state = {
        "question": question.strip()
    }

    with st.spinner(
        "🤖 Agentic system is researching..."
    ):

        try:

            result = investment_graph.invoke(
                initial_state
            )

            st.session_state[
                "research_result"
            ] = result

        except Exception as e:

            st.error(
                f"Research system error: {e}"
            )

            st.stop()

    st.success(
        "✅ Research completed successfully."
    )


# ============================================================
# RESULTS
# ============================================================

if "research_result" in st.session_state:

    result = st.session_state[
        "research_result"
    ]

    ticker = result.get(
        "ticker",
        "UNKNOWN",
    )

    market_data = result.get(
        "market_data",
        {},
    )

    news_data = result.get(
        "news_data",
        [],
    )

    technical_analysis = result.get(
        "technical_analysis",
        {},
    )

    risk_analysis = result.get(
        "risk_analysis",
        {},
    )

    final_analysis = result.get(
        "final_analysis",
        "No final analysis was generated.",
    )


    # ========================================================
    # OVERVIEW
    # ========================================================

    st.divider()

    st.subheader(
        "📊 Research Overview"
    )

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "TICKER",
            ticker,
        )


    with col2:

        price = market_data.get(
            "price"
        )

        if price is not None:

            st.metric(
                "CURRENT PRICE",
                f"${float(price):.2f}",
            )

        else:

            st.metric(
                "CURRENT PRICE",
                "N/A",
            )


    with col3:

        st.metric(
            "NEWS ARTICLES",
            len(news_data),
        )


    with col4:

        trend = technical_analysis.get(
            "trend",
            "N/A",
        )

        st.metric(
            "TECHNICAL TREND",
            trend,
        )


    # ========================================================
    # MARKET DATA
    # ========================================================

    with st.expander(
        "📊 LIVE MARKET DATA",
        expanded=True,
    ):

        if market_data:

            st.json(
                market_data
            )

        else:

            st.info(
                "No market data available."
            )


    # ========================================================
    # TECHNICAL ANALYSIS
    # ========================================================

    with st.expander(
        "📈 TECHNICAL ANALYSIS",
        expanded=True,
    ):

        if technical_analysis:

            st.json(
                technical_analysis
            )

        else:

            st.info(
                "No technical analysis available."
            )


    # ========================================================
    # RISK ANALYSIS
    # ========================================================

    with st.expander(
        "⚠️ RISK ANALYSIS"
    ):

        if risk_analysis:

            st.json(
                risk_analysis
            )

        else:

            st.info(
                "No risk analysis available."
            )


    # ========================================================
    # NEWS
    # ========================================================

    with st.expander(
        "📰 FINANCIAL NEWS"
    ):

        if news_data:

            for index, article in enumerate(
                news_data,
                start=1,
            ):

                title = article.get(
                    "title",
                    "Untitled",
                )

                url = article.get(
                    "url",
                    "",
                )

                published = article.get(
                    "published_date",
                    "",
                )

                st.markdown(
                    f"**{index}. {title}**"
                )

                if published:

                    st.caption(
                        published
                    )

                if url:

                    st.markdown(
                        f"[🔗 Read article]({url})"
                    )

                st.divider()

        else:

            st.info(
                "No financial news found."
            )


    # ========================================================
    # FINAL REPORT
    # ========================================================

    st.subheader(
        "🤖 Final Investment Research Report"
    )

    st.markdown(
        final_analysis
    )


    # ========================================================
    # DOWNLOAD
    # ========================================================

    st.divider()

    st.subheader(
        "📥 Download Research"
    )

    col1, col2 = st.columns(2)


    with col1:

        st.download_button(
            label="📄 Download Markdown Report",
            data=final_analysis,
            file_name=f"{ticker}_investment_research.md",
            mime="text/markdown",
            use_container_width=True,
        )


    with col2:

        st.download_button(
            label="📝 Download TXT Report",
            data=final_analysis,
            file_name=f"{ticker}_investment_research.txt",
            mime="text/plain",
            use_container_width=True,
        )


    # ========================================================
    # AGENT STATUS
    # ========================================================

    st.divider()

    st.subheader(
        "⚡ Agent Status"
    )

    col1, col2, col3 = st.columns(3)


    with col1:

        if market_data:

            st.success(
                "✅ Market Data Agent"
            )

        else:

            st.warning(
                "⚠️ Market Data Agent"
            )


    with col2:

        if news_data:

            st.success(
                f"✅ News Agent — {len(news_data)} articles"
            )

        else:

            st.warning(
                "⚠️ News Agent"
            )


    with col3:

        if technical_analysis:

            st.success(
                "✅ Technical Agent"
            )

        else:

            st.warning(
                "⚠️ Technical Agent"
            )


    st.caption(
        "⚠️ This system provides automated investment research "
        "and is not personalized financial advice."
    )
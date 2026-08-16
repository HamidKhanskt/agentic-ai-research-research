from langgraph.graph import StateGraph, START, END

from src.state import InvestmentState

from src.agents.planner import planner_agent
from src.agents.market_data import market_data_agent
from src.agents.news_agent import news_agent
from src.agents.fundamental_agent import fundamental_agent
from src.agents.technical_agent import technical_agent
from src.agents.risk_agent import risk_analysis_agent
from src.agents.final_analyst import final_analyst


# ============================================================
# BUILD INVESTMENT RESEARCH GRAPH
# ============================================================

def build_graph():

    graph = StateGraph(InvestmentState)

    # ========================================================
    # ADD ALL AGENTS
    # ========================================================

    graph.add_node(
        "planner",
        planner_agent
    )

    graph.add_node(
        "market_data",
        market_data_agent
    )

    graph.add_node(
        "news",
        news_agent
    )

    graph.add_node(
        "fundamental",
        fundamental_agent
    )

    graph.add_node(
        "technical",
        technical_agent
    )

    graph.add_node(
        "risk",
        risk_analysis_agent
    )

    graph.add_node(
        "final_analyst",
        final_analyst
    )

    # ========================================================
    # START
    # ========================================================

    graph.add_edge(
        START,
        "planner"
    )

    # ========================================================
    # PLANNER → MARKET DATA
    # ========================================================

    graph.add_edge(
        "planner",
        "market_data"
    )

    # ========================================================
    # MARKET DATA → NEWS
    # ========================================================

    graph.add_edge(
        "market_data",
        "news"
    )

    # ========================================================
    # NEWS → FUNDAMENTAL
    # ========================================================

    graph.add_edge(
        "news",
        "fundamental"
    )

    # ========================================================
    # FUNDAMENTAL → TECHNICAL
    # ========================================================

    graph.add_edge(
        "fundamental",
        "technical"
    )

    # ========================================================
    # TECHNICAL → RISK
    # ========================================================

    graph.add_edge(
        "technical",
        "risk"
    )

    # ========================================================
    # RISK → FINAL ANALYST
    # ========================================================

    graph.add_edge(
        "risk",
        "final_analyst"
    )

    # ========================================================
    # FINAL ANALYST → END
    # ========================================================

    graph.add_edge(
        "final_analyst",
        END
    )

    # ========================================================
    # COMPILE GRAPH
    # ========================================================

    return graph.compile()


# ============================================================
# APPLICATION GRAPH
# ============================================================

investment_graph = build_graph()
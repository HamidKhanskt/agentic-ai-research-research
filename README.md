#    
<img width="1405" height="621" alt="Screenshot 2026-08-16 at 4 07 22 PM" src="https://github.com/user-attachments/assets/a0833846-b98a-4ee1-bec9-775edb73e9e6" />




<img width="1247" height="638" alt="Screenshot 2026-08-16 at 4 07 42 PM" src="https://github.com/user-attachments/assets/d6ea26ef-dcca-44da-a385-1ca03ab97e52" />


<img width="1324" height="376" alt="Screenshot 2026-08-16 at 4 07 51 PM" src="https://github.com/user-attachments/assets/c77f0a3c-9880-4a58-84f5-26682be2c9aa" />

<img width="1355" height="335" alt="Screenshot 2026-08-16 at 4 07 58 PM" src="https://github.com/user-attachments/assets/940d1179-943c-49e7-afb7-2f45a7262902" />



<img width="1372" height="763" alt="Screenshot 2026-08-16 at 4 08 07 PM" src="https://github.com/user-attachments/assets/02f8a029-8c0a-4ebe-a22b-10a2c3d720b5" />


<img width="677" height="772" alt="Screenshot 2026-08-16 at 4 08 16 PM" src="https://github.com/user-attachments/assets/5d1a206e-2d76-4cfa-a199-0b6f3367c446" />




<img width="612" height="589" alt="Screenshot 2026-08-16 at 4 08 23 PM" src="https://github.com/user-attachments/assets/cc38b3e3-68f0-4692-9efe-c1fde5697d36" />



<img width="1113" height="632" alt="Screenshot 2026-08-16 at 4 08 29 PM" src="https://github.com/user-attachments/assets/0e7f8294-3c76-4ed5-90ef-c2d29bf81d09" />



<img width="827" height="752" alt="Screenshot 2026-08-16 at 4 08 36 PM" src="https://github.com/user-attachments/assets/bb8f8b72-70a9-4eff-909e-07a8a55b25f5" />



<img width="943" height="591" alt="Screenshot 2026-08-16 at 4 08 45 PM" src="https://github.com/user-attachments/assets/bcc18f28-bb67-4c39-8214-eddf1719efd2" />


<img width="1325" height="699" alt="Screenshot 2026-08-16 at 4 08 55 PM" src="https://github.com/user-attachments/assets/22c084f6-0b77-4afd-9638-bb572db7ef55" />


<img width="1383" height="179" alt="Screenshot 2026-08-16 at 4 09 02 PM" src="https://github.com/user-attachments/assets/61d5793a-0de0-46a5-9407-bab965fd2616" />

Agentic AI Investment Research Assistant

> 🤖 An autonomous multi-agent AI system that researches stocks using **LangGraph, LangChain, Groq, live market data, financial news, technical analysis, fundamental analysis, and risk analysis**.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-FF6B35?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 🚀 Overview

The **Agentic AI Investment Research Assistant** is a multi-agent investment research platform designed to automatically investigate a stock and produce a structured research report.

Instead of relying on a single LLM response, the system uses an **agentic workflow** where a Planner Agent determines what research is required and specialized agents independently collect and analyze different types of information.

The system can analyze:

* 📊 Live market data
* 📰 Financial news
* 💰 Fundamental information
* 📈 Technical indicators
* ⚠️ Investment risks
* 🤖 Overall investment assessment

The final results are synthesized by a **Final Investment Analyst Agent**.

---

# 🧠 Agentic AI Architecture

```text
                         👤 USER
                           │
                           ▼
                  ┌─────────────────┐
                  │  🧠 PLANNER     │
                  │     AGENT       │
                  └────────┬────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
      ┌────────────┐ ┌────────────┐ ┌──────────────┐
      │ 📊 MARKET  │ │ 📰 NEWS    │ │ 💰 FUNDAMENTAL│
      │    DATA    │ │   AGENT    │ │    AGENT     │
      └─────┬──────┘ └─────┬──────┘ └──────┬───────┘
            │              │               │
            └──────────────┼───────────────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
      ┌──────────────┐          ┌──────────────┐
      │ 📈 TECHNICAL │          │ ⚠️ RISK       │
      │    AGENT     │          │    AGENT      │
      └──────┬───────┘          └──────┬───────┘
             │                         │
             └────────────┬────────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ 🤖 FINAL ANALYST │
                 └────────┬─────────┘
                          │
                          ▼
                 📄 INVESTMENT REPORT
```

---

# ⚡ How It Works

### 1️⃣ User asks a question

Example:

```text
Should I invest in Apple now?
```

### 2️⃣ Planner Agent

The Planner Agent analyzes the question and extracts the stock ticker.

For example:

```text
AAPL
```

It then decides which research agents are required.

```text
MARKET_DATA
NEWS
FUNDAMENTAL_RESEARCH
TECHNICAL_ANALYSIS
RISK_ANALYSIS
```

---

### 3️⃣ Specialized Research Agents

The selected agents perform their individual tasks.

| Agent                | Responsibility                                |
| -------------------- | --------------------------------------------- |
| 🧠 Planner Agent     | Determines research strategy                  |
| 📊 Market Data Agent | Retrieves current market information          |
| 📰 News Agent        | Finds recent financial news                   |
| 💰 Fundamental Agent | Evaluates fundamental information             |
| 📈 Technical Agent   | Calculates technical indicators               |
| ⚠️ Risk Agent        | Identifies investment risks                   |
| 🤖 Final Analyst     | Combines all research into a final assessment |

---

### 4️⃣ Final Investment Analyst

The final analyst receives the collected research and generates a structured report containing:

* 💵 Current price
* 📊 Market capitalization
* 📈 Technical indicators
* 📰 Recent news
* 💰 Fundamental observations
* ⚠️ Risk factors
* 🎯 Investment assessment
* 📋 Overall score
* 🔎 Research summary

---

# 📊 Example Technical Analysis

The system calculates indicators such as:

```text
Current Price       $305.93
20-Day SMA          $318.22
50-Day SMA          $308.95
200-Day SMA         $279.99

6-Month High        $344.27
6-Month Low         $245.07

Trend               Mixed
```

This allows the Final Analyst to consider both short-term and long-term price behavior.

---

# 📰 Financial News Analysis

The News Agent retrieves recent financial articles and provides them to the research workflow.

Example:

```text
📰 Recent Financial News

1. Does Apple Stock Still Have Room to Run?
2. Apple Reportedly Eyes Foldable iPhone
3. Apple Stock Looks Pricey On Cash Flow
4. Apple Stock Opinions on Recent Earnings
5. Can Apple Intelligence Spark a New iPhone Cycle?
```

The final analyst uses this information alongside the other research signals.

---

# ⚠️ Risk Analysis

The Risk Agent identifies potential risks including:

```text
⚠️ Fundamental Risk
Future returns depend on continued earnings and revenue growth.

⚠️ Market Risk
A broader market or technology-sector decline could negatively
affect the stock.

⚠️ Company-Specific Risk
Competition, product cycles, regulation, tariffs, and supply
chain issues may affect results.
```

---

# 🖥️ Streamlit Dashboard

The project includes a modern **neon-style Streamlit interface**.

The dashboard provides:

### 🔎 Research Query

Users can enter questions such as:

```text
Should I invest in Apple now?
```

### 📊 Research Overview

Displays:

* Ticker
* Current price
* Number of news articles
* Technical trend

### 📈 Technical Analysis

Displays technical indicators collected by the Technical Agent.

### ⚠️ Risk Analysis

Displays identified investment risks.

### 📰 Financial News

Displays recent financial articles with links.

### 🤖 Final Research Report

Displays the complete AI-generated investment research report.

---

# 🧩 Technology Stack

### 🐍 Python

Core programming language.

### 🔗 LangChain

Used for LLM orchestration and agent components.

### 🕸️ LangGraph

Used to build the stateful multi-agent workflow.

### ⚡ Groq

Used as the LLM provider for fast AI inference.

### 📊 Yahoo Finance

Used for market data and financial information.

### 📰 Google News RSS

Used for financial news discovery.

### 🎨 Streamlit

Used to build the interactive web interface.

---

# 📁 Project Structure

```text
agentic-investment-ai/
│
├── 📄 app.py
├── 📄 test_graph.py
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
│
└── 📁 src/
    │
    ├── 📄 __init__.py
    ├── 📄 graph.py
    ├── 📄 state.py
    │
    └── 📁 agents/
        │
        ├── 📄 __init__.py
        ├── 🧠 planner.py
        ├── 📊 market_data.py
        ├── 📰 news_agent.py
        ├── 💰 fundamental_agent.py
        ├── 📈 technical_agent.py
        ├── ⚠️ risk_agent.py
        └── 🤖 final_analyst.py
```

---

# 🔄 LangGraph Workflow

The workflow is implemented using LangGraph.

```text
START
  │
  ▼
Planner
  │
  ├──────────────► Market Data
  │
  ├──────────────► News
  │
  ├──────────────► Fundamentals
  │
  ├──────────────► Technical Analysis
  │
  └──────────────► Risk Analysis
                         │
                         ▼
                  Final Analyst
                         │
                         ▼
                        END
```

The Planner dynamically determines which research agents should run.

This makes the application **agentic rather than a simple sequential chatbot**.

---

# 💻 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/agentic-investment-ai.git
```

Enter the project:

```bash
cd agentic-investment-ai
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file locally.

```env
GROQ_API_KEY=your_groq_api_key
```

⚠️ **Never upload your `.env` file or API keys to GitHub.**

The `.gitignore` file should contain:

```text
.venv/
__pycache__/
*.pyc
.env
.DS_Store
.streamlit/secrets.toml
```

---

# ▶️ Run the Agentic System

To test the LangGraph workflow:

```bash
python test_graph.py
```

You should see the agents execute:

```text
🧠 PLANNER AGENT

📊 MARKET DATA AGENT

📰 NEWS AGENT

💰 FUNDAMENTAL RESEARCH AGENT

📈 TECHNICAL ANALYSIS AGENT

⚠️ RISK ANALYSIS AGENT

🤖 FINAL INVESTMENT ANALYST
```

---

# 🌐 Run the Streamlit Application

Start the web application:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal.

---

# 📄 Research Reports

The Streamlit application allows users to download generated research.

Available formats include:

```text
📄 Markdown Research Report
📝 TXT Research Report
```

The reports contain the information collected by the multi-agent research system.

---

# 📈 Example Workflow

```text
User:
"Should I invest in Apple now?"

             ↓

Planner Agent
             ↓

Extract ticker: AAPL
             ↓

Research Planning
             ↓

┌───────────────────────────────┐
│ Market Data                   │
│ Financial News                │
│ Fundamental Research          │
│ Technical Analysis            │
│ Risk Analysis                 │
└───────────────────────────────┘
             ↓

Final Investment Analyst
             ↓

┌───────────────────────────────┐
│ Investment Verdict            │
│ Confidence                    │
│ Overall Score                 │
│ Valuation                     │
│ Technical Analysis            │
│ Risk Analysis                 │
│ News Research                 │
│ Fundamental Research          │
└───────────────────────────────┘
             ↓

📄 Downloadable Research Report
```

---

# 🎯 Why This Project Is Agentic AI

This project demonstrates several important agentic AI concepts:

### 🧠 Autonomous Planning

The Planner Agent determines what research is needed.

### 🔀 Dynamic Routing

LangGraph routes the workflow to the appropriate research agents.

### 👥 Multi-Agent Architecture

Different agents specialize in different research tasks.

### 🛠️ Tool-Based Research

Agents interact with external financial and news data sources.

### 🔄 State Management

LangGraph maintains shared research state between agents.

### 🤖 AI Synthesis

The Final Analyst combines information from multiple agents into one report.

---

# 💼 Resume Project Description

You can describe this project on your resume as:

> **Agentic AI Investment Research Assistant** — Built a multi-agent investment research system using LangGraph and LangChain that autonomously plans and routes stock research across market data, financial news, fundamental, technical, and risk-analysis agents; integrated Groq LLM inference, live financial data, and Streamlit to generate interactive, citation-ready investment research reports.

---

# 🚀 Future Improvements

Possible future additions include:

* 📄 PDF report generation
* 📊 Interactive stock charts
* 📉 Candlestick charts
* 🧠 RAG over SEC filings and annual reports
* 🔍 Financial statement analysis
* 📰 News sentiment analysis
* 🏦 Portfolio analysis
* 📈 Stock comparison
* 💾 Persistent research history
* 🗃️ Vector database integration
* 🔄 Agent reflection and fact-checking
* ☁️ Cloud deployment

---

<img width="1405" height="621" alt="Screenshot 2026-08-16 at 4 07 22 PM" src="https://github.com/user-attachments/assets/7f3fad17-fdd1-4097-9b20-e76e55f10508" />


---

# ⭐ Project Highlights

<p align="center">

🧠 **Agentic AI**

🔗 **LangChain**

🕸️ **LangGraph**

⚡ **Groq**

📊 **Live Market Data**

📰 **Financial News**

📈 **Technical Analysis**

💰 **Fundamental Analysis**

⚠️ **Risk Analysis**

🎨 **Streamlit Dashboard**

📄 **Downloadable Reports**

</p>

---

## 👨‍💻 Built With

**Python • LangChain • LangGraph • Groq • Streamlit • Yahoo Finance • Financial News APIs**

---

⭐ If you find this project useful, consider giving the repository a star!

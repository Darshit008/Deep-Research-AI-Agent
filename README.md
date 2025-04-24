# 🧠 Deep Research AI Agentic System

## 📌 Overview
This project is a **Deep Research AI Agentic System** designed to automate complex research tasks using a multi-agent setup. It leverages:

- **Tavily API** for intelligent web crawling and data collection.
- **LangChain** for building modular, interactive agents.
- **LangGraph** for structuring agent workflows as stateful graphs.
- **Gemini API** (Google Generative AI) for drafting high-quality answers.

This system is built to reflect how future enterprise-grade AI agents can autonomously conduct research, organize data, and generate polished outputs.

---

## 🧠 Architecture

```
User Input
   │
   ▼
[Research Agent] ←──── Tavily API
   │         (Web search + summarization)
   ▼
[Drafting Agent] ←──── Gemini API
   │         (Refines into final answer)
   ▼
Final Drafted Answer
```

- **Research Agent**: Responsible for querying Tavily with user input, retrieving relevant information from the web, and summarizing key points.
- **Drafting Agent**: Takes the summarized research and transforms it into a well-written, human-readable final answer using Gemini's generative capabilities.

LangGraph connects these agents in a **sequential state graph**, where the output of one agent becomes the input to the next.

---

## 🧠 Agent Collaboration

### 🔍 Research Agent
- Accepts a query from the user.
- Calls **Tavily** to perform live web searches.
- Extracts, summarizes, and filters out noise.
- Returns structured data as a context document.

### ✍️ Drafting Agent
- Accepts context from the Research Agent.
- Uses **Gemini API** (Google Generative AI) to:
  - Understand the summarized data.
  - Generate a professional, accurate, and coherent answer.

---

## 🔧 Technologies Used
- `Python 3.9`
- `LangChain`
- `LangGraph`
- `Google Generative AI (Gemini)`
- `Tavily`
- `dotenv` for environment config

---

## 🚀 How to Run
1. Clone the repo:
```bash
git clone https://github.com/Darshit008/deep-research-agent.git
cd deep-research-agent
```

2. Set up environment variables:
Create a `.env` file:
```
TAVILY_API_KEY=your_tavily_key
GOOGLE_API_KEY=your_gemini_api_key
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the main app:
```bash
python main.py
```

---

## 🧪 Example Flow
```
Enter your research query: "2025 AI agents"

✅ Final Drafted Answer:
[Structured response generated from web + Gemini]
```

---

## 📁 Project Structure
```
.
├── main.py                   # Entrypoint
├── agents/
│   ├── research_agent.py     # Tavily-based Research Agent
│   └── drafting_agent.py     # Gemini-based Drafting Agent
├── graph.py                  # LangGraph orchestration
├── utils/
│   └── prompts.py            # Prompt templates for agents
├── .env                      # API keys
└── README.md                 # Project documentation
```


## 👨‍💻 Author
**Darshit**
- Email: [darshitsingh08@gmail.com]
- GitHub: [Darshit008]

---

## 🏁 Final Note
This system showcases how AI agents can work collaboratively to automate sophisticated research workflows — with creativity, modularity, and reliability.




# Agentic Knowledge Base Auditor

A production-oriented, multi-agent system designed to continuously audit, monitor, and improve AI chatbot knowledge bases to reduce hallucinations and improve response accuracy.

## 🎯 Overview

The Agentic Knowledge Base Auditor improves the reliability of AI chatbot responses by focusing on the data layer - the primary cause of hallucinations and incorrect outputs in Retrieval-Augmented Generation (RAG) systems.

Instead of retraining large language models, this system continuously monitors, evaluates, and improves the underlying knowledge base through intelligent agents.

## 🏗️ System Architecture

```
User → Chatbot → Knowledge Base
                      ↑
                Auditor System
```

### Key Components

1. **Knowledge Base System** - Document ingestion, embedding, and semantic search
2. **Multi-Agent System** - Specialized agents for quality assurance
3. **Orchestration Layer** - Coordinates agent execution
4. **Remediation Engine** - Determines corrective actions
5. **Plugin System** - Easy integration with existing chatbots
6. **Dashboard** - Real-time monitoring and control

## 📦 Project Structure

```
agentic-kb-auditor/
├── README.md
├── requirements.txt
├── pyproject.toml
├── .env
├── .gitignore
│
├── configs/
│   ├── config.yaml
│   ├── logging.yaml
│   └── prompts/
│
├── data/
│   ├── kb/
│   ├── logs/
│   └── vector_store/
│
├── src/
│   ├── main.py
│   ├── plugin/
│   ├── core/
│   ├── domain/
│   ├── kb/
│   ├── processing/
│   ├── agents/
│   ├── application/
│   ├── remediation/
│   ├── infrastructure/
│   ├── observability/
│   ├── evaluation/
│   ├── interfaces/
│   └── utils/
│
├── scripts/
├── tests/
└── docs/
```

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/Ashith1234/agentic-kb-auditor.git
cd agentic-kb-auditor

# Install dependencies
pip install -r requirements.txt

# Or install as a package
pip install -e .
```

### Configuration

1. Copy `.env.example` to `.env`
2. Add your API keys (OpenAI, etc.)
3. Configure `configs/config.yaml` for your use case

### Running the System

```bash
# Run the main pipeline
python src/main.py

# Or use the CLI
python src/plugin/cli.py run

# Start the dashboard
streamlit run src/interfaces/dashboard/streamlit_app.py
```

## 🤖 Core Agents

| Agent | Function |
|-------|----------|
| **Version Agent** | Detects outdated content |
| **Duplicate Agent** | Identifies duplicates/conflicts |
| **Coverage Agent** | Finds missing topics |
| **Retrieval Agent** | Fetches verified information |
| **Scoring Agent** | Evaluates KB health |
| **Learning Agent** | Updates knowledge base |
| **Supervisor Agent** | Monitors all agents |

## ✨ Key Features

- ✅ **Multi-Agent Architecture** - Specialized agents for different quality checks
- ✅ **Versioning & Rollback** - Safe updates with automatic rollback
- ✅ **Human-in-the-Loop** - Manual review of critical decisions
- ✅ **Cross-Source Consensus** - Reduces incorrect updates
- ✅ **Security Layer** - Masks PII and protects sensitive data
- ✅ **Plugin System** - Easy integration with existing chatbots
- ✅ **Dashboard** - Real-time monitoring and analytics
- ✅ **Structured Logging** - JSON-based logs for debugging

## 📊 Development Phases

### Phase 1: Foundation
- Knowledge base pipeline
- Embedding and retrieval system

### Phase 2: Core Agents
- Version, duplicate, and coverage agents

### Phase 3: Advanced Agents
- Retrieval, learning, and supervisor agents

### Phase 4: Safety Layer
- Rollback system
- HITL queue
- Consensus checker

### Phase 5: Product Layer
- Plugin system
- CLI tools
- Dashboard UI

## 🔌 Plugin Integration

Use as a plugin in your existing chatbot:

```python
from src.plugin.rag_auditor import RAGAuditor

auditor = RAGAuditor(config_path='configs/config.yaml')
auditor.intercept_response(
    query="What is AI?",
    documents=retrieved_docs,
    response="AI is..."
)
```

## 📚 Documentation

- [Architecture Design](docs/architecture.md)
- [Agent Design Patterns](docs/agent_design.md)

## 🔒 Security

- PII masking
- API key protection
- Safe data handling
- Audit trails

## 📈 Expected Outcomes

- Reduce hallucinations
- Improve response accuracy
- Maintain up-to-date knowledge
- Enable automated KB management
- Increase trust in AI systems

## 🧠 Key Insight

*The effectiveness of AI systems depends more on the quality of their knowledge base than the complexity of the model.*

## 📝 License

MIT License

## 👤 Author

Ashith1234

## 🤝 Contributing

Contributions are welcome! Please read CONTRIBUTING.md first.

## 💬 Support

For support, please open an issue on GitHub.

---

**Status**: Under Development (Phase 1)

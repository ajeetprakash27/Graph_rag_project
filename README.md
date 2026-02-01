# GraphRAG - Graph-based Retrieval Augmented Generation

<div align="center">

![GraphRAG Logo](https://img.shields.io/badge/GraphRAG-AI%20Knowledge%20Graph-blue?style=for-the-badge&logo=neo4j)
![Python](https://img.shields.io/badge/Python-3.8%2B-green?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009485?style=flat-square&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

**An intelligent AI-powered API that combines graph databases with retrieval-augmented generation for enhanced semantic search and knowledge extraction.**

[Features](#-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [API Documentation](#-api-documentation) • [Contributing](#-contributing)

</div>

---

## 🚀 Overview

**GraphRAG** is a sophisticated Retrieval Augmented Generation (RAG) system that leverages both vector embeddings and graph-based knowledge representations to provide intelligent, context-aware responses. By combining LLM capabilities with structured knowledge graphs, it enables more accurate and traceable information retrieval.

### Key Benefits
- 📊 **Dual-Context Intelligence**: Combines semantic search (vector similarity) with structured knowledge graphs
- 🧠 **LLM-Powered Responses**: Integrates OpenAI's GPT-4 for intelligent question answering
- 🔗 **Knowledge Graphs**: Uses Neo4j for structured relationship mapping and entity extraction
- ⚡ **Fast & Scalable**: Built on FastAPI for high-performance async operations
- 📄 **Document Processing**: Supports PDF ingestion and chunking with LangChain

---

## ✨ Features

- **🤖 Intelligent Q&A**: Ask natural language questions and receive AI-powered answers with contextual awareness
- **📚 Vector Search**: Semantic similarity search across document collections using OpenAI embeddings
- **🔍 Graph Exploration**: Entity and relationship extraction with Neo4j graph database
- **🎯 Context Awareness**: Leverages both text context and graph relationships for comprehensive answers
- **🧪 Mock Mode**: Works out-of-the-box with mock data for testing and development
- **🔄 Auto-reload**: Development mode with hot-reloading for rapid iteration
- **📖 Interactive API Docs**: Auto-generated Swagger UI and ReDoc documentation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Server                        │
│  (HTTP API with auto-generated documentation)          │
└────────────┬────────────────────────────┬────────────────┘
             │                            │
      ┌──────▼──────┐           ┌────────▼──────────┐
      │ RAG Pipeline │           │  Graph Utils      │
      │ • Retrieve   │           │ • Extract Graph   │
      │ • Context    │           │ • Store Triples   │
      │   Search     │           │ • Graph Search    │
      └──────┬───────┘           └────────┬──────────┘
             │                            │
      ┌──────▼──────────────┐    ┌───────▼────────────┐
      │  Vector Store       │    │   Neo4j Database   │
      │  • Chroma VectorDB  │    │  • Knowledge Graph │
      │  • PDF Loader       │    │  • Entity Relations│
      │  • Embeddings       │    │                    │
      └─────────────────────┘    └────────────────────┘
             │                            │
      ┌──────▼──────────────┐    ┌───────▼────────────┐
      │  OpenAI API         │    │   LLM (GPT-4o)     │
      │  • Embeddings       │    │  • Entity Extract  │
      │  • Chat Models      │    │  • Answer Gen      │
      └─────────────────────┘    └────────────────────┘
```

---

## 🔧 Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | FastAPI | High-performance async web framework |
| **LLM** | OpenAI GPT-4o-mini | Language understanding & generation |
| **Vector Store** | Chroma + LangChain | Semantic search & embeddings |
| **Graph DB** | Neo4j | Knowledge graph storage & querying |
| **PDF Processing** | PyPDF + LangChain | Document ingestion |
| **Server** | Uvicorn | ASGI server for FastAPI |
| **Configuration** | python-dotenv | Environment management |

---

## 📋 Project Structure

```
graphrag-project/
├── app/
│   ├── main.py              # FastAPI application & endpoints
│   ├── config.py            # Configuration & environment variables
│   ├── rag_pipeline.py      # RAG retrieval logic
│   ├── vector_store.py      # Vector database management
│   └── graph_utils.py       # Neo4j graph operations
├── data/
│   └── data.pdf             # Input documents (add your PDFs here)
├── vectordb/                # Persisted vector embeddings
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create this)
├── test_api.py             # API testing script
└── README.md               # This file
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.8 or higher
- pip or conda
- (Optional) OpenAI API key for real responses
- (Optional) Neo4j instance for graph operations

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/graphrag-project.git
   cd graphrag-project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Create .env file
   echo OPENAI_API_KEY=your_api_key_here > .env
   ```

5. **Run the server**
   ```bash
   python -m uvicorn app.main:app --reload
   ```

6. **Access the API**
   - Main API: `http://localhost:8000`
   - Interactive Docs (Swagger): `http://localhost:8000/docs`
   - Alternative Docs (ReDoc): `http://localhost:8000/redoc`

### Quick Test

```bash
# Test the home endpoint
curl http://localhost:8000/

# Test with mock data
curl http://localhost:8000/test

# Ask a question
curl "http://localhost:8000/ask?question=What%20is%20GraphRAG?"
```

---

## 📡 API Documentation

### Endpoints

#### 1. **GET /** - Home
Returns API status and available endpoints.

**Response:**
```json
{
  "message": "✅ GraphRAG API Running",
  "status": "online",
  "endpoints": {
    "home": "GET /",
    "ask": "POST /ask?question=YOUR_QUESTION",
    "test": "GET /test"
  }
}
```

#### 2. **GET /test** - Test Endpoint
Returns mock data for testing without API keys.

**Response:**
```json
{
  "status": "✅ API is working",
  "mock_context": "GraphRAG combines graph databases with retrieval-augmented generation...",
  "mock_graph": [
    ["GraphRAG", "USES", "Graph Database"],
    ["GraphRAG", "COMBINES", "LLM Technology"]
  ],
  "message": "This is mock data. Connect your OpenAI API key for real responses."
}
```

#### 3. **POST /ask** - Ask Question
Query the knowledge base with natural language questions.

**Parameters:**
- `question` (string, required): Your question

**Response:**
```json
{
  "question": "What is GraphRAG?",
  "answer": "GraphRAG combines graph databases with retrieval-augmented generation...",
  "sources": "Real OpenAI Response"
}
```

**Example:**
```bash
curl -X POST "http://localhost:8000/ask?question=How%20does%20GraphRAG%20work?"
```

---

## 🔑 Configuration

### Environment Variables (`.env`)

```bash
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Neo4j Configuration (Optional)
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
```

### Get Your OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Create a new API key
3. Add it to your `.env` file

---

## 💻 Development

### Project Components

#### `main.py` - FastAPI Application
- Defines REST endpoints
- Handles request/response routing
- Manages OpenAI client initialization

#### `rag_pipeline.py` - RAG Logic
- `retrieve_context()`: Vector similarity search
- `retrieve_graph()`: Graph-based entity search
- `build_graph_from_docs()`: Document processing

#### `vector_store.py` - Vector Database
- Document loading (PDF support)
- Text chunking and splitting
- Embedding generation
- Chroma vector store management

#### `graph_utils.py` - Neo4j Operations
- Entity and relationship extraction
- Triple storage in Neo4j
- Graph-based knowledge search

#### `config.py` - Configuration
- Environment variable loading
- API credentials
- Database connection settings

---

## 🧪 Testing

### Run the Test Suite
```bash
python test_api.py
```

### Manual Testing
```python
import requests

# Test home endpoint
response = requests.get("http://localhost:8000/")
print(response.json())

# Ask a question
response = requests.post(
    "http://localhost:8000/ask",
    params={"question": "What is machine learning?"}
)
print(response.json())
```

---

## 📊 Usage Examples

### Example 1: Simple Question Answering
```bash
curl -X POST "http://localhost:8000/ask?question=Explain%20artificial%20intelligence"
```

### Example 2: Technical Query
```bash
curl -X POST "http://localhost:8000/ask?question=How%20do%20vector%20embeddings%20work?"
```

### Example 3: Using Python
```python
import requests
import json

url = "http://localhost:8000/ask"
params = {"question": "What is the GraphRAG architecture?"}

response = requests.post(url, params=params)
result = response.json()

print(f"Q: {result['question']}")
print(f"A: {result['answer']}")
```

---

## 🚀 Deployment

### Docker Support (Coming Soon)
```bash
docker build -t graphrag .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key graphrag
```

### Cloud Deployment Options
- **AWS**: EC2 + RDS (PostgreSQL) + Lambda
- **GCP**: Cloud Run + Firestore
- **Azure**: App Service + Cosmos DB
- **Heroku**: Simple deployment with buildpacks

---

## 📝 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `OpenAI API Error 401` | Check your API key in `.env` file |
| `Neo4j Connection Failed` | Ensure Neo4j is running or disable graph features |
| `Port 8000 already in use` | Run on different port: `uvicorn app.main:app --port 8001` |
| `PDF not found` | Add PDF to `data/` folder or use mock mode |

---

## 🔗 Integration Examples

### With LangChain
```python
from langchain.chains import RetrievalQA

qa = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)
```

### With Streamlit Frontend
```python
import streamlit as st
import requests

st.title("GraphRAG Chat")
question = st.text_input("Ask a question:")

if question:
    response = requests.post(
        "http://localhost:8000/ask",
        params={"question": question}
    )
    st.write(response.json()["answer"])
```

---

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [FastAPI Guide](https://fastapi.tiangolo.com/)
- [Neo4j Documentation](https://neo4j.com/docs/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Chroma Vector DB](https://docs.trychroma.com/)

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Install dev dependencies
pip install -r requirements.txt
pip install pytest black flake8

# Format code
black app/

# Run linter
flake8 app/
```

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name** - [@Ajeet Pandey](https://github.com/ajeetprakash27)

---

## 🌟 Star History

If you found this project useful, please consider giving it a star! ⭐

---

## 📞 Support

- 📧 Email: imajeetpandey27@gmail.com
- 💬 Issues: [GitHub Issues](https://github.com/yourusername/graphrag-project/issues)
- 📖 Discussions: [GitHub Discussions](https://github.com/yourusername/graphrag-project/discussions)

---

<div align="center">

**Made with ❤️ by [Your Name]**

[⬆ back to top](#graphrag---graph-based-retrieval-augmented-generation)

</div>

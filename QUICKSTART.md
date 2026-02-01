# Quick Start Guide

Get GraphRAG running in 5 minutes!

## ⚡ Installation (2 minutes)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/graphrag-project.git
cd graphrag-project
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment (Optional)
```bash
# Create .env file
echo OPENAI_API_KEY=your_api_key_here > .env

# On macOS/Linux:
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

### Step 5: Run the Server
```bash
python -m uvicorn app.main:app --reload
```

✅ Server is running at `http://localhost:8000`

---

## 🧪 Test It (1 minute)

### In Your Browser
1. Open `http://localhost:8000/docs`
2. Click on the test endpoint
3. Try the `/test` endpoint first
4. Then try `/ask` with a question

### Using cURL
```bash
# Test endpoint
curl http://localhost:8000/test

# Ask a question
curl "http://localhost:8000/ask?question=What%20is%20artificial%20intelligence?"
```

### Using Python
```python
import requests

response = requests.post(
    "http://localhost:8000/ask",
    params={"question": "What is machine learning?"}
)
print(response.json())
```

---

## 📚 Next Steps

### 1. Explore the API
- Visit `http://localhost:8000/docs` for interactive documentation
- Read [API.md](API.md) for detailed endpoint documentation

### 2. Add Your Own Data
```bash
# Place PDF files in the data/ folder
cp your_document.pdf data/
```

### 3. Configure OpenAI API
```bash
# Get your API key from https://platform.openai.com/api-keys
# Add to .env file:
OPENAI_API_KEY=sk-...
```

### 4. Set Up Neo4j (Optional)
```bash
# Download Neo4j: https://neo4j.com/download/
# Update .env with your Neo4j credentials:
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
```

---

## 🎯 Common Tasks

### Ask a Question with Python
```python
import requests

def ask_graphrag(question):
    response = requests.post(
        "http://localhost:8000/ask",
        params={"question": question}
    )
    result = response.json()
    print(f"Q: {result['question']}")
    print(f"A: {result['answer']}")
    return result

# Usage
ask_graphrag("Explain quantum computing")
```

### Test All Endpoints
```python
import requests
import json

BASE_URL = "http://localhost:8000"

# Test 1: Home
print("Testing /")
response = requests.get(f"{BASE_URL}/")
print(json.dumps(response.json(), indent=2))

# Test 2: Test endpoint
print("\nTesting /test")
response = requests.get(f"{BASE_URL}/test")
print(json.dumps(response.json(), indent=2))

# Test 3: Ask
print("\nTesting /ask")
response = requests.post(f"{BASE_URL}/ask", params={"question": "Hello?"})
print(json.dumps(response.json(), indent=2))
```

### Add Custom Documents
```python
from app.rag_pipeline import build_graph_from_docs

# Documents should be in data/ folder as PDFs
build_graph_from_docs()
print("Documents processed successfully!")
```

---

## 🔧 Troubleshooting

### Port Already in Use
```bash
# Use a different port
python -m uvicorn app.main:app --port 8001
```

### ModuleNotFoundError
```bash
# Make sure venv is activated and reinstall
pip install -r requirements.txt
```

### OpenAI API Errors
```bash
# Check your .env file
cat .env

# Verify API key is valid at https://platform.openai.com/account/api-keys
```

### Connection Issues
```bash
# Test if server is running
curl http://localhost:8000/

# Check logs in the terminal running uvicorn
```

---

## 📖 Documentation

- **README.md** - Project overview
- **API.md** - Complete API documentation
- **CONTRIBUTING.md** - How to contribute
- **LICENSE** - MIT License

---

## 🚀 Deployment

### Local Development
```bash
python -m uvicorn app.main:app --reload
```

### Production
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
```

### Docker (Coming Soon)
```bash
docker build -t graphrag .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key graphrag
```

---

## 💡 Tips

1. **Use the interactive docs** - `http://localhost:8000/docs` is your friend!
2. **Keep .env secure** - Never commit it to git
3. **Use mock mode** - Test without API keys using `/test` endpoint
4. **Read the logs** - Check terminal output for errors and debugging info
5. **Start simple** - Ask basic questions first, then get complex

---

## 🎓 Learning Resources

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [LangChain Docs](https://python.langchain.com/)
- [Neo4j Getting Started](https://neo4j.com/developer/)
- [OpenAI API Guide](https://platform.openai.com/docs/)

---

## ❓ FAQ

**Q: Do I need OpenAI API key to start?**
A: No! Use `/test` endpoint for mock data. Add API key later for real responses.

**Q: Can I use different LLMs?**
A: Yes! Modify `config.py` to use different providers (Azure, Hugging Face, etc.)

**Q: How do I add documents?**
A: Place PDF files in `data/` folder and call `build_graph_from_docs()`

**Q: Is it production-ready?**
A: It's feature-complete but needs proper auth/security for production.

**Q: How do I contribute?**
A: See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines!

---

## 🆘 Need Help?

1. Check [API.md](API.md) for endpoint details
2. Review example scripts in the repository
3. Check existing GitHub issues
4. Open a new issue with detailed information

---

**Happy coding! 🚀**

Questions? Open an issue: [GitHub Issues](https://github.com/yourusername/graphrag-project/issues)

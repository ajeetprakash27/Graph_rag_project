from fastapi import FastAPI, HTTPException
from openai import OpenAI
from app.rag_pipeline import retrieve_context, retrieve_graph

app = FastAPI()
client = None

def get_client():
    global client
    if client is None:
        try:
            client = OpenAI()
        except Exception as e:
            print(f"⚠️  Warning: OpenAI client initialization failed: {e}")
            client = False
    return client if client else None

@app.get("/")
def home():
    return {
        "message": "✅ GraphRAG API Running",
        "status": "online",
        "endpoints": {
            "home": "GET /",
            "ask": "POST /ask?question=YOUR_QUESTION",
            "test": "GET /test"
        }
    }

@app.get("/test")
def test():
    """Test endpoint with mock data"""
    return {
        "status": "✅ API is working",
        "mock_context": "GraphRAG combines graph databases with retrieval-augmented generation for enhanced knowledge management.",
        "mock_graph": [
            ["GraphRAG", "USES", "Graph Database"],
            ["GraphRAG", "COMBINES", "LLM Technology"]
        ],
        "message": "This is mock data. Connect your OpenAI API key for real responses."
    }

@app.post("/ask")
def ask(question: str):
    if not question or question.strip() == "":
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    try:
        context = retrieve_context(question)
        graph_data = retrieve_graph(question.split()[0] if question.split() else "")

        prompt = f"""
    Use both contexts to answer.

    Text Context:
    {context}

    Graph Context:
    {str(graph_data)}

    Question: {question}
    """

        api_client = get_client()
        
        if api_client:
            res = api_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return {
                "question": question,
                "answer": res.choices[0].message.content,
                "sources": "Real OpenAI Response"
            }
        else:
            return {
                "question": question,
                "answer": f"Mock Response: Based on the context about '{question}', GraphRAG provides intelligent retrieval-augmented generation capabilities. Configure your OpenAI API key in .env file for real responses.",
                "sources": "Mock Data (OpenAI API key not configured)",
                "note": "Set OPENAI_API_KEY in .env file for real responses"
            }
    except Exception as e:
        return {
            "question": question,
            "answer": f"Mock Response: I can help with questions about {question}. Please configure your OpenAI API key.",
            "error": str(e),
            "sources": "Error - Using Mock Data"
        }

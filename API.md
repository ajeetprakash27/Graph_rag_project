# API Documentation

## Overview

GraphRAG provides a RESTful API built with FastAPI for intelligent question-answering powered by graph-based retrieval augmented generation.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. For production deployments, add API key authentication:

```python
from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API Key")
```

## Response Format

All responses are in JSON format. Standard response structure:

```json
{
  "status": "success" | "error",
  "data": { /* response data */ },
  "error": null | "error message"
}
```

## Endpoints

### 1. GET /

**Description:** Returns API status and available endpoints

**Method:** GET

**URL:** `http://localhost:8000/`

**Parameters:** None

**Request:**
```bash
curl -X GET "http://localhost:8000/"
```

**Response:** `200 OK`
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

**Status Codes:**
- `200`: API is running normally

---

### 2. GET /test

**Description:** Test endpoint that returns mock data without requiring API keys

**Method:** GET

**URL:** `http://localhost:8000/test`

**Parameters:** None

**Request:**
```bash
curl -X GET "http://localhost:8000/test"
```

**Response:** `200 OK`
```json
{
  "status": "✅ API is working",
  "mock_context": "GraphRAG combines graph databases with retrieval-augmented generation for enhanced knowledge management.",
  "mock_graph": [
    ["GraphRAG", "USES", "Graph Database"],
    ["GraphRAG", "COMBINES", "LLM Technology"]
  ],
  "message": "This is mock data. Connect your OpenAI API key for real responses."
}
```

**Use Cases:**
- Verify API is running
- Test connectivity
- Demo without authentication

---

### 3. POST /ask

**Description:** Ask a question to the GraphRAG system. Returns AI-generated answers using context from vector search and graph relationships.

**Method:** POST

**URL:** `http://localhost:8000/ask`

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `question` | string | Yes | The question to ask the system |

**Request:**
```bash
curl -X POST "http://localhost:8000/ask?question=What%20is%20GraphRAG?"
```

**With Python:**
```python
import requests

url = "http://localhost:8000/ask"
params = {"question": "How do vector embeddings work?"}

response = requests.post(url, params=params)
print(response.json())
```

**Response:** `200 OK`
```json
{
  "question": "What is GraphRAG?",
  "answer": "GraphRAG is a system that combines graph databases with retrieval-augmented generation. It uses vector embeddings for semantic search and Neo4j for knowledge graphs to provide more accurate and traceable answers.",
  "sources": "Real OpenAI Response"
}
```

**Response with mock data (no API key):**
```json
{
  "question": "What is GraphRAG?",
  "answer": "Mock Response: I can help with questions about What is GraphRAG?. Please configure your OpenAI API key.",
  "error": "Error code: 401 - {'error': {'message': 'Incorrect API key provided'}}",
  "sources": "Error - Using Mock Data"
}
```

**Status Codes:**
- `200`: Question processed successfully
- `400`: Bad request (empty question)
- `422`: Validation error
- `500`: Internal server error

**Error Responses:**

Empty question:
```json
{
  "detail": "Question cannot be empty"
}
```

---

## Data Types

### Question Object
```json
{
  "question": "string",
  "timestamp": "2026-02-01T10:30:00Z"
}
```

### Answer Object
```json
{
  "question": "string",
  "answer": "string",
  "sources": "string",
  "error": "string | null",
  "confidence": "number (0-1)"
}
```

### Context Object
```json
{
  "id": "string",
  "content": "string",
  "score": "number (0-1)"
}
```

### Graph Entity
```json
{
  "entity": "string",
  "type": "string",
  "relationships": ["string"]
}
```

---

## Error Handling

### Common Error Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 400 | Bad Request | Check your query parameters |
| 401 | Unauthorized | Add valid API key |
| 404 | Not Found | Endpoint doesn't exist |
| 422 | Validation Error | Invalid request format |
| 500 | Server Error | Server encountered an error |

### Error Response Format
```json
{
  "detail": "Error message",
  "status_code": 400,
  "error_type": "ValidationError"
}
```

---

## Rate Limiting

Coming soon in production release:
- 100 requests per minute for unauthenticated users
- 1000 requests per minute for authenticated users

---

## Examples

### Example 1: Simple Question
```bash
curl -X POST "http://localhost:8000/ask?question=What%20is%20machine%20learning?"
```

### Example 2: Technical Question
```bash
curl -X POST "http://localhost:8000/ask?question=How%20do%20transformers%20work%20in%20NLP?"
```

### Example 3: With Python Requests
```python
import requests
import json

def ask_question(question: str):
    url = "http://localhost:8000/ask"
    response = requests.post(url, params={"question": question})
    return response.json()

# Usage
result = ask_question("What is the difference between RAG and fine-tuning?")
print(f"Question: {result['question']}")
print(f"Answer: {result['answer']}")
print(f"Source: {result['sources']}")
```

### Example 4: Batch Questions
```python
import requests

questions = [
    "What is GraphRAG?",
    "How do graph databases work?",
    "What is retrieval augmented generation?"
]

for question in questions:
    response = requests.post(
        "http://localhost:8000/ask",
        params={"question": question}
    )
    print(f"Q: {response.json()['question']}")
    print(f"A: {response.json()['answer']}\n")
```

---

## Webhook Support (Coming Soon)

```python
# Register webhook for answer completion
POST /webhooks/register
{
  "url": "https://your-domain.com/webhook",
  "events": ["answer.completed"]
}
```

---

## Pagination (Coming Soon)

For endpoints returning multiple results:

```bash
GET /search?q=query&page=1&limit=10
```

---

## Caching

Responses are cached for 1 hour by default:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_cached_response(question: str):
    # implementation
    pass
```

To disable caching:
```bash
GET /ask?question=query&nocache=true
```

---

## Versioning

Current API Version: `v1`

Future versions will use:
```
/api/v2/ask
/api/v3/ask
```

Backward compatibility maintained for 2 major versions.

---

## SDK / Libraries

### Python SDK (Coming Soon)
```python
from graphrag import GraphRAG

client = GraphRAG(api_key="your-key")
response = client.ask("What is GraphRAG?")
```

### JavaScript/TypeScript SDK (Coming Soon)
```typescript
import { GraphRAG } from 'graphrag-js';

const client = new GraphRAG({ apiKey: 'your-key' });
const response = await client.ask('What is GraphRAG?');
```

---

## Best Practices

1. **Always provide meaningful questions**
   - Good: "How do neural networks process information?"
   - Bad: "How?"

2. **Use appropriate timeouts**
   - Set timeout to 30 seconds for production
   - ```python
     requests.post(url, params=params, timeout=30)
     ```

3. **Handle errors gracefully**
   ```python
   try:
       response = requests.post(url, params=params)
       response.raise_for_status()
   except requests.exceptions.RequestException as e:
       print(f"API error: {e}")
   ```

4. **Cache results to reduce API calls**
   ```python
   cache = {}
   def ask_with_cache(question):
       if question in cache:
           return cache[question]
       result = requests.post(url, params={"question": question}).json()
       cache[question] = result
       return result
   ```

5. **Monitor API usage**
   - Track number of requests
   - Monitor response times
   - Log errors

---

## Monitoring & Analytics

### Health Check
```bash
curl -X GET "http://localhost:8000/health"
```

Response:
```json
{
  "status": "healthy",
  "uptime": 86400,
  "requests_processed": 1250,
  "avg_response_time": 245
}
```

---

## Support & Issues

- 📧 Email: support@graphrag.dev
- 💬 GitHub Issues: [Report Bug](https://github.com/yourusername/graphrag/issues)
- 📖 Documentation: [Full Docs](https://graphrag.dev/docs)

---

## Changelog

### v1.0.0 (2026-02-01)
- Initial API release
- Three endpoints: /, /test, /ask
- Mock data support
- Error handling

### v1.1.0 (Coming Soon)
- Rate limiting
- Webhook support
- Batch processing
- Caching improvements

---

Last Updated: February 1, 2026

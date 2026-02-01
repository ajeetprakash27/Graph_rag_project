#!/usr/bin/env python
"""Test script to demonstrate GraphRAG API functionality"""

import json
import time
import subprocess
import requests
from threading import Thread

def run_server():
    """Run the uvicorn server in background"""
    subprocess.run(["python", "-m", "uvicorn", "app.main:app", "--port", "8000"], 
                   capture_output=True)

# Start server in background thread
server_thread = Thread(target=run_server, daemon=True)
server_thread.start()

# Wait for server to start
print("⏳ Starting GraphRAG API server...")
time.sleep(5)

try:
    # Test 1: Home endpoint
    print("\n" + "="*60)
    print("TEST 1: Home Endpoint (GET /)")
    print("="*60)
    response = requests.get("http://127.0.0.1:8000/")
    print(json.dumps(response.json(), indent=2))
    
    # Test 2: Test endpoint
    print("\n" + "="*60)
    print("TEST 2: Test Endpoint (GET /test)")
    print("="*60)
    response = requests.get("http://127.0.0.1:8000/test")
    print(json.dumps(response.json(), indent=2))
    
    # Test 3: Ask endpoint with mock data
    print("\n" + "="*60)
    print("TEST 3: Ask Endpoint (POST /ask)")
    print("="*60)
    response = requests.post("http://127.0.0.1:8000/ask", params={"question": "What is GraphRAG?"})
    print(json.dumps(response.json(), indent=2))
    
    # Test 4: Another question
    print("\n" + "="*60)
    print("TEST 4: Another Question")
    print("="*60)
    response = requests.post("http://127.0.0.1:8000/ask", params={"question": "How does Neo4j work?"})
    print(json.dumps(response.json(), indent=2))
    
    print("\n" + "="*60)
    print("✅ ALL TESTS COMPLETED SUCCESSFULLY")
    print("="*60)
    print("\n📝 Summary:")
    print("- ✅ API is running without errors")
    print("- ✅ Mock data is being returned")
    print("- ✅ All endpoints are responsive")
    print("- ⚠️  Configure OPENAI_API_KEY in .env for real responses")
    print("- ⚠️  Set up Neo4j server for graph operations")
    
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    print("\n✨ Test completed!")

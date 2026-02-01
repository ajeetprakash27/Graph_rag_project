import os

_vectorstore = None

def create_vectorstore():
    """Lazy-load vectorstore with mock data if PDF not found."""
    global _vectorstore
    
    if _vectorstore is not None:
        return _vectorstore
    
    try:
        from langchain_community.document_loaders import PyPDFLoader
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        from langchain_openai import OpenAIEmbeddings
        from langchain_community.vectorstores import Chroma
        
        if not os.path.exists("data/data.pdf"):
            print("⚠️  Warning: data/data.pdf not found. Using mock vectorstore.")
            return MockVectorStore()
        
        loader = PyPDFLoader("data/data.pdf")
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings()

        vectorstore = Chroma.from_documents(
            chunks,
            embedding=embeddings,
            persist_directory="vectordb"
        )
        _vectorstore = vectorstore
        return vectorstore
    except Exception as e:
        print(f"⚠️  Error loading vectorstore: {e}. Using mock vectorstore.")
        return MockVectorStore()


class MockVectorStore:
    """Mock vectorstore for testing without OpenAI API key."""
    def similarity_search(self, query, k=3):
        from langchain_core.documents import Document
        mock_docs = [
            Document(page_content="GraphRAG combines graph databases with retrieval-augmented generation."),
            Document(page_content="Neo4j is a graph database management system."),
            Document(page_content="Vector embeddings enable semantic search capabilities.")
        ]
        return mock_docs[:k]

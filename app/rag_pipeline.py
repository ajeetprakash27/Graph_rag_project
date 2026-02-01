from app.vector_store import create_vectorstore
from app.graph_utils import extract_graph, store_triple, graph_search

vectorstore = None

def get_vectorstore():
    global vectorstore
    if vectorstore is None:
        vectorstore = create_vectorstore()
    return vectorstore

def build_graph_from_docs():
    vs = get_vectorstore()
    docs = vs.similarity_search(" ", k=10)
    for d in docs:
        triples = extract_graph(d.page_content).split("\n")
        for t in triples:
            if t.strip():
                try:
                    e1 = t.split("(")[1].split(")")[0]
                    rel = t.split("[")[1].split("]")[0]
                    e2 = t.split("->(")[1].split(")")[0]
                    store_triple(e1, rel, e2)
                except:
                    pass


def retrieve_context(question):
    vs = get_vectorstore()
    docs = vs.similarity_search(question, k=3)
    return "\n".join([d.page_content for d in docs])


def retrieve_graph(entity):
    return graph_search(entity)

from neo4j import GraphDatabase
from openai import OpenAI
from app.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

driver = None
client = OpenAI()

def get_driver():
    global driver
    if driver is None:
        try:
            driver = GraphDatabase.driver(
                NEO4J_URI,
                auth=(NEO4J_USER, NEO4J_PASSWORD)
            )
        except Exception as e:
            print(f"⚠️  Warning: Could not connect to Neo4j: {e}")
            driver = None
    return driver

def extract_graph(text):
    try:
        prompt = f"""
        Extract entities and relationships.
        Format strictly:
        (Entity1)-[RELATION]->(Entity2)

        Text:
        {text}
        """
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content
    except Exception as e:
        print(f"⚠️  Error extracting graph: {e}")
        return "(MockEntity1)-[RELATION]->(MockEntity2)"


def store_triple(e1, rel, e2):
    drv = get_driver()
    if drv is None:
        print(f"⚠️  Neo4j not connected. Mock storing: {e1} -[{rel}]-> {e2}")
        return
    
    try:
        with drv.session() as session:
            session.run("""
                MERGE (a:Entity {name:$e1})
                MERGE (b:Entity {name:$e2})
                MERGE (a)-[:REL {type:$rel}]->(b)
            """, e1=e1, e2=e2, rel=rel)
    except Exception as e:
        print(f"⚠️  Error storing triple: {e}")


def graph_search(name):
    drv = get_driver()
    if drv is None:
        return [
            ("MockEntity1", "RELATION", "MockEntity2"),
            ("GraphRAG", "RELATED_TO", "NLPTechnology"),
        ]
    
    try:
        query = """
        MATCH (a:Entity)-[r]->(b:Entity)
        WHERE a.name CONTAINS $name
        RETURN a.name, type(r), b.name
        LIMIT 20
        """
        with drv.session() as session:
            result = session.run(query, name=name)
            return [r.values() for r in result]
    except Exception as e:
        print(f"⚠️  Error searching graph: {e}")
        return []

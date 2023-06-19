from neo4j import GraphDatabase


uri = "bolt://localhost:7687"
user = "neo4j"
password = "Adebayo1@"
driver = GraphDatabase.driver(uri, auth=(user, password))


def read_query(query, params={}):
    with driver.session() as session:
        result = session.run(query, params)
        response = [r.values()[0] for r in result]
        return response

import os
from dotenv import load_dotenv
from neo4j import GraphDatabase


def create_driver():
    load_dotenv()

    connection_uri = os.getenv("NEO4J_URI")
    username = os.getenv("NEO4J_USERNAME")
    password = os.getenv("NEO4J_PASSWORD")

    missing = [
        key
        for key, value in {
            "NEO4J_URI": connection_uri,
            "NEO4J_USERNAME": username,
            "NEO4J_PASSWORD": password,
        }.items()
        if not value
    ]

    if missing:
        missing_keys = ", ".join(missing)
        raise ValueError(f"Missing required environment variables: {missing_keys}")

    return GraphDatabase.driver(connection_uri, auth=(username, password))


if __name__ == "__main__":
    driver = create_driver()
    driver.verify_connectivity()
    print("Neo4j connectivity verified.")
    driver.close()

from neo4j import GraphDatabase, Session
from typing import Any


class Neo4jClient:
    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config

        try:
            self.driver = GraphDatabase.driver(
                uri=f"bolt://{self.config.get("host")}:{self.config.get("port")}",
                auth=(self.config.get("username"), self.config.get("password")),
                connection_timeout=self.config.get("connection_timeout"),
                max_connection_pool_size=self.config.get("max_connection_pool_size")
            )

            self.driver.verify_connectivity()
        except Exception:
            raise
    
    def get_session(self) -> Session:
        try:
            session = self.driver.session(database=self.config.get("database"))

            return session
        except Exception:
            raise

from neo4j import GraphDatabase, Session

from configs.neo4j_config import Neo4jConfig


class Neo4jClient:
    def __init__(self, config: Neo4jConfig) -> None:
        self.config = config

        try:
            self.driver = GraphDatabase.driver(
                uri=f"bolt://{self.config.host}:{self.config.port}",
                auth=(self.config.username, self.config.password),
                connection_timeout=self.config.connection_timeout,
                max_connection_pool_size=self.config.max_connection_pool_size
            )

            self.driver.verify_connectivity()
        except Exception:
            raise
    
    def get_session(self) -> Session:
        try:
            session = self.driver.session(database=self.config.database)

            return session
        except Exception:
            raise

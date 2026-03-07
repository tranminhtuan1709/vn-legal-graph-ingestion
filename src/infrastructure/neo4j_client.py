from neo4j import GraphDatabase, Session

from src.exceptions.custom_exceptions import InfrastructureError
from src.configs.neo4j_config import Neo4jConfig


class Neo4jClient:
    def __init__(self, config: Neo4jConfig) -> None:
        self.config = config

        try:
            self.driver = GraphDatabase.driver(
                self.config.uri,
                auth=(self.config.username, self.config.password),
                connection_timeout=self.config.connection_timeout,
                max_connection_pool_size=self.config.max_connection_pool_size
            )

            self.driver.verify_connectivity()
        except Exception as e:
            raise InfrastructureError(
                message="Failed to connect to Neo4j",
                context={
                    "uri": self.config.uri,
                    "username": self.config.username,
                    "database": self.config.database,
                    "connection_timeout": self.config.connection_timeout,
                    "max_connection_pool_size": self.config.max_connection_pool_size
                }
            ) from e
    
    def get_session(self) -> Session:
        try:
            return self.driver.session(database=self.config.database)
        except Exception as e:
            raise InfrastructureError(
                message="Failed to create Neo4j session",
                context={
                    "host": self.config.host,
                    "port": self.config.port,
                    "username": self.config.username,
                    "database": self.config.database,
                    "connection_timeout": self.config.connection_timeout,
                    "max_connection_pool_size": self.config.max_connection_pool_size
                }
            ) from e

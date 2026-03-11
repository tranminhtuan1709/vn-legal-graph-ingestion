from mysql.connector import pooling
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract
from typing import Any


class MySQLClient:
    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config

        try:
            self.connection_pool = pooling.MySQLConnectionPool(
                host=self.config.get("host"),
                port=self.config.get("port"),
                username=self.config.get("username"),
                password=self.config.get("password"),
                database=self.config.get("database"),
                pool_name=self.config.get("pool_name"),
                pool_size=self.config.get("pool_size"),
                connection_timeout=self.config.get("connection_timeout")
            )
        except Exception:
            raise

    def get_connection(self) -> MySQLConnectionAbstract:
        try:
            connection = self.connection_pool.get_connection()

            return connection
        except Exception:
            raise

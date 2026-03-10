from mysql.connector import pooling
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract

from configs.mysql_config import MySQLConfig


class MySQLClient:
    def __init__(self, config: MySQLConfig) -> None:
        self.config = config

        try:
            self.connection_pool = pooling.MySQLConnectionPool(
                host=self.config.host,
                port=self.config.port,
                username=self.config.username,
                password=self.config.password,
                database=self.config.database,
                pool_name=self.config.pool_name,
                pool_size=self.config.pool_size,
                connection_timeout=self.config.connection_timeout
            )
        except Exception:
            raise

    def get_connection(self) -> MySQLConnectionAbstract:
        try:
            return self.connection_pool.get_connection()
        except Exception:
            raise
    
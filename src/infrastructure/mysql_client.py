from mysql.connector import pooling
from mysql.connector.abstracts import MySQLConnectionAbstract


class MySQLClient:
    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        database: str,
        pool_name: str,
        pool_size: int,
        connection_timeout: int
    ) -> None:

        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.pool_name = pool_name
        self.pool_size = pool_size
        self.connection_timeout = connection_timeout

        try:
            self.connection_pool = pooling.MySQLConnectionPool(
                host=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
                database=self.database,
                pool_name=self.pool_name,
                pool_size=self.pool_size,
                connection_timeout=self.connection_timeout
            )
        except Exception:
            raise

    def get_connection(self) -> MySQLConnectionAbstract:
        try:
            connection = self.connection_pool.get_connection()
            
            return connection
        except Exception:
            raise

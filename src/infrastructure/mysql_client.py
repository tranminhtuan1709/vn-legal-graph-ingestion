from mysql.connector import pooling
from mysql.connector.abstracts import MySQLConnectionAbstract, MySQLCursorAbstract

from ..exceptions.custom_exceptions import InfrastructureError
from ..configs.mysql_config import MySQLConfig


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
        except Exception as e:
            raise InfrastructureError(
                message="Failed to connect to MySQL",
                context={
                    "host": self.config.host,
                    "port": self.config.port,
                    "username": self.config.username,
                    "database": self.config.database,
                    "pool_name": self.config.pool_name,
                    "pool_size": self.config.pool_size,
                    "connection_timeout": self.config.connection_timeout
                }
            ) from e

    def get_connection(self) -> tuple[MySQLConnectionAbstract, MySQLCursorAbstract]:
        try:
            connection = self.connection_pool.get_connection()
            cursor = connection.cursor(dictionary=True)

            return connection, cursor
        except Exception as e:
            raise InfrastructureError(
                message="Failed to get a connection from the connection pool",
                context={
                    "host": self.config.host,
                    "port": self.config.port,
                    "username": self.config.username,
                    "database": self.config.database,
                    "pool_name": self.config.pool_name,
                    "pool_size": self.config.pool_size,
                    "connection_timeout": self.config.connection_timeout
                }
            ) from e

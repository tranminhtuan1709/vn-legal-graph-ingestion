class MySQLConfig:
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
    ):
        """
        Init an object of `MySQLConfig` with provided configurations.

        Args:
            host (str): Host name of the MySQL server.
            port (int): Port of the MySQL server.
            username (str): Username.
            password (str): Password.
            database (str): Default database to use.
            pool_name (str): Name of the connection pool.
            pool_size (int): Size of the connection pool.
            connection_timeout (int): Timeout for the TCP and Unix socket connections.
        """
        
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.pool_name = pool_name
        self.pool_size = pool_size
        self.connection_timeout = connection_timeout

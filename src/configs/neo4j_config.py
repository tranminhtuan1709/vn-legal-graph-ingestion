class Neo4jConfig:
    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        database: str,
        connection_timeout: int,
        max_connection_pool_size: int
    ) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.connection_timeout = connection_timeout
        self.max_connection_pool_size = max_connection_pool_size

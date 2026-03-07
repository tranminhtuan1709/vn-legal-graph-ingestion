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
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.pool_name = pool_name
        self.pool_size = pool_size
        self.connection_timeout = connection_timeout

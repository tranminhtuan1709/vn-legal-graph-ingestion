from ..infrastructure.mysql_client import MySQLClient


class DocumentRepository:
    def __init__(self, mysql_client: MySQLClient):
        self.mysql_client = mysql_client

    def fetch_data(self, document_id):
        pass

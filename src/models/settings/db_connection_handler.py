import mysql.connector
from src.models.settings.config import Config
from mysql.connector import MySQLConnection


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__conn = None
    
    def connect(self) -> None:
        conn =  mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        self.__conn = conn
    
    def get_connection(self) -> MySQLConnection:
        return self.__conn
    

db_connection_handler = DbConnectionHandler()

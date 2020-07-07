from pyodbc import Connection
import pyodbc
import pandas.io.sql
from pandas import DataFrame

def runQuery(sql: str, connection: Connection) -> DataFrame:
    """Query all the data to the DataBase Server

    Args:
        sql (str): SQL query string 
        connection (Connection): Connection Object

    Returns:
        DataFrame: Pandas dataframe with data
    """
    return pandas.io.sql.read_sql(sql, connection)

def createConnection(databaseName: str, server: str,user: str, password: str, driver: str ="ODBC Driver 17 for SQL Server") -> Connection:
    """Creates a Conection to a SQL SERVER Database

    Args:
        databaseName (str): Name of the database
        server (str): Database Server IP or hostname
        user (str): user Name
        password (str): Connection credentials
        driver (str, optional): Connection Driver. Defaults to "ODBC Driver 17 for SQL Server".

    Returns:
        Connection: a connection object
    """
    return pyodbc.connect("DRIVER={"+driver+"};SERVER="+server+";DATABASE="+databaseName+";UID="+user+";PWD="+password)
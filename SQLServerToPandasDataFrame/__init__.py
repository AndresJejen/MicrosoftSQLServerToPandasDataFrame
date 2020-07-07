from os import listdir
from os.path import isfile, isdir
from pyodbc import Connection
import pyodbc
import pandas.io.sql
from pandas import DataFrame
from .constants import BaseSQLQuery

def CreateObjectEmpresa(empresa: str, DataBase: str, Table: str) -> None:
    """[Creates a new Company Object and add it to empresas object]

    Args:
        empresa (str): [Name of company]
        DataBase (str): [Name of Database]
        Table (str): [Name of table]
    """
    empresaObject = {
        "Empresa": empresa,
        "DataBase": DataBase,
        "Table": Table
    }
    return empresaObject

def FilesToCompanyDict(path: str) -> None:
    """[Convert a list of sql files to a Dict objects]

    Args:
        path (str): [description]
    """
    empresas = {}
    files = QueryFilesNames(path)
    for file in files:
        f=open(path+file, "r")
        content = f.read()
        contents=content.split(',')
        companyName = contents[1].split(' AS ')[0].split("'")[1]
        Database = content.split('[')[1].split(']')[0]
        Table = 'Vista_Auxiliar_Movimientos_Contables'
        empresas[companyName] = CreateObjectEmpresa(companyName, Database, Table)
    return empresas

def QueryFilesNames(path: str) -> list:
    """[return an array of files names .sql]

    Args:
        path (str): [Route of directory with sql Files]

    Returns:
        list: [List with the name of the files]
    """
    return [obj for obj in listdir(path) if isfile(path + obj)]

def CreateQuery(company: dict, BaseQuery: str, test: bool = True) -> str:
    """[Create a SQL QUERY based on the company data]

    Args:
        company (dict): [Dictionay with the data]

    Returns:
        str: [SQL QUERY for ]
    """
    Empresa = company["Empresa"]
    DataBase = company["DataBase"]
    Table = company["Table"]
    limit = "TOP 10" if test == True else ""
    return BaseSQLQuery.format(limit,Empresa, DataBase, Table)

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
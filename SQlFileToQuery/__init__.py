from os import listdir
from os.path import isfile, isdir
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
    empresas = {}
    """[Convert a list of sql files to a Dict objects]

    Args:
        path (str): [description]
    """
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

def CreateQuery(company: dict) -> str:
    """[Create a SQL QUERY based on the company data]

    Args:
        company (dict): [Dictionay with the data]

    Returns:
        str: [SQL QUERY for ]
    """
    Empresa = company["Empresa"]
    DataBase = company["DataBase"]
    Table = company["Table"]
    return BaseSQLQuery.format(Empresa, DataBase, Table)
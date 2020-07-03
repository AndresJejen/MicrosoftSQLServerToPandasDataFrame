from SQlFileToQuery import FilesToCompanyDict, CreateQuery
import urllib
from sqlalchemy import create_engine, text
#import pyodbc
import pandas as pd
import pandas.io.sql

def runQuery(sql: str):
    """[Query all the data to the DataBase Server]

    Args:
        sql (str): [SQL String]

    Returns:
        [type]: [description]
    """
    result = engine.connect().execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())
    #df= pandas.io.sql.read_sql(sql, conn)
    #return df

if __name__ == "__main__":    
    empresas = FilesToCompanyDict('./DataExample/SQL/')
    empresasNames = [empresa for empresa in empresas]
    name = empresasNames[0]
    empresa = empresas[name]
    query1 = CreateQuery(empresa)
    params = urllib.parse.quote_plus(f'DRIVER={"ODBC Driver 17 for SQL Server"};SERVER=192.168.11.3\WORLDOFFICE;DATABASE={empresa["DataBase"]};UID=wo_cliente;PWD=wo_cliente')
    connQuery = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    engine = create_engine(connQuery)
    #conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.11.3\WORLDOFFICE;DATABASE=' + empresa['DataBase'] +';UID=wo_cliente;PWD=wo_cliente')
    print(runQuery(query1))

# 35617215324531349489132184383
# MicrosoftSQLServerToPandasDataFrame

## Description

This package query data from any SQL Server Database and parse it into a Pandas Dataframe
it can be useful for pipelines process and speed up your development process.

## Usage

```
from SQLServerToPandasDataFrame import CreateQuery, createConnection, runQuery

Base_Query = "select {0} {1} from {2}.dbo.{3}"
query1 = CreateQuery(empresa, Base_Query)
    
server = "HOST_DIRECTION"
user = "USER_NAME"
password = "PASSWORD"
    
conn = createConnection("MyDataBase", server, user, password)
print(runQuery(query1, conn))
```

## Settings

This package performs by default all the connections to a SQL Server using ``ODBC Driver 17 for SQL Server`` driver. if you wanna use a different driver, please replace add the driver parameter in create Connection method.

```
conn = createConnection("MyDataBase", server, user, password, driver = "DRIVER OF YOUR PREFERENCE")
```


```
conn = createConnection("MyDataBase", server, user, password, driver = "ODBC Driver 17 for SQL Server")
```

We use ``Pyodbc `` as ODBC access library, for more driver options please ckeck the documentation [PyODBC Documentation](https://github.com/mkleehammer/pyodbc).

## Collaborators

- Germán Andrés Jején Cortés [@andres_jejen on twitter](https://twitter.com/andres_jejen)
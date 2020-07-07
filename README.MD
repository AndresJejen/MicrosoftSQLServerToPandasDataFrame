# RSQLServerToPandasDataFrame

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

## Collaborators

1. Germán Andrés Jején Cortés [@andres_jejen on twitter](https://twitter.com/andres_jejen)
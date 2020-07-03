BaseSQLQuery = """
select {0}
 ROW_NUMBER() OVER (ORDER BY Fecha) as id,
 '{1}' AS Empresa,
 YEAR(Fecha) AS Año,
 MONTH(Fecha) AS Mes,
 Fecha,
 Codigo_Cuenta,
 substring("Codigo_Cuenta",1,1) as Cod_Clase,
 substring("Codigo_Cuenta",1,2) as Cod_Grupo,
 substring("Codigo_Cuenta",1,4) as Cod_Cuenta,
 Nombre_Cuenta,
 Nombre_Documento,
 Tipo_documento,
 Numero_Documento,
 Concepto_Detalle AS Concepto,
 Tercero,
 Codigo_Centro_Costos,
 Centro_de_costos,
 Débito,
 Crédito,
 SUM(Débito - Crédito) AS Valor,
 SUM((Débito - Crédito) * -1) AS Valor_Ingreso
 FROM [{2}].dbo.{3}
 GROUP BY 
 YEAR(Fecha), MONTH(Fecha), Fecha, Codigo_Cuenta, Nombre_Cuenta, Tercero,
 Codigo_Centro_Costos, Centro_de_costos, Nombre_Documento, Tipo_documento,
 Numero_Documento, Concepto_Detalle, Tercero, Débito, Crédito
 ORDER BY Fecha
""" 

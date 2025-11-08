# Databricks notebook source
from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------


dbutils.widgets.removeAll()

# COMMAND ----------

dbutils.widgets.text("storage_name", "adlsatalaya1402")
dbutils.widgets.text("container", "raw")
dbutils.widgets.text("catalogo", "project_etl")
dbutils.widgets.text("esquema", "bronze")

# COMMAND ----------

storage_name = dbutils.widgets.get("storage_name")
container = dbutils.widgets.get("container")
catalogo = dbutils.widgets.get("catalogo")
esquema = dbutils.widgets.get("esquema")

ruta = f"abfss://{container}@{storage_name}.dfs.core.windows.net/clinic_profession.csv"

# COMMAND ----------

profession_schema = StructType([
    StructField("id_profesion", IntegerType(), nullable=False),
    StructField("nombre_profesion", StringType(), nullable=True),
    StructField("departamento", StringType(), nullable=True)
])

# COMMAND ----------

df_profession = spark.read \
    .schema(profession_schema) \
    .option("header", True) \
    .option("sep", ",") \
    .csv(ruta)

# COMMAND ----------

df_profession.display()

# COMMAND ----------

df_profession.write.mode("overwrite").format("delta").saveAsTable(f"{catalogo}.{esquema}.profession")
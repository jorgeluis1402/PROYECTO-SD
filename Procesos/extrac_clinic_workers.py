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

ruta = f"abfss://{container}@{storage_name}.dfs.core.windows.net/clinic_workers.csv"

# COMMAND ----------

workers_schema = StructType([
    StructField("id_trabajador", IntegerType(), nullable=False),
    StructField("nombre", StringType(), nullable=True),
    StructField("apellido", StringType(), nullable=True),
    StructField("id_profesion", IntegerType(), nullable=False),
    StructField("id_turno", IntegerType(), nullable=False)
])

# COMMAND ----------

df_workers = spark.read \
    .schema(workers_schema) \
    .option("header", True) \
    .option("sep", ",") \
    .csv(ruta)


# COMMAND ----------

df_workers.display()

# COMMAND ----------

df_workers.write.mode("overwrite").format("delta").saveAsTable(f"{catalogo}.{esquema}.workers")
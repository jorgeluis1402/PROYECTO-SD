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

ruta = f"abfss://{container}@{storage_name}.dfs.core.windows.net/clinic_turn.csv"

# COMMAND ----------

turn_schema = StructType([
    StructField("id_turno", IntegerType(), nullable=False),
    StructField("nombre_turno", StringType(), nullable=True),
    StructField("inicio_horario", StringType(), nullable=True),
    StructField("fin_horario", StringType(), nullable=True)
])


# COMMAND ----------

df_turn = spark.read \
    .schema(turn_schema) \
    .option("header", True) \
    .option("sep", ",") \
    .csv(ruta)

# COMMAND ----------

df_turn.display()

# COMMAND ----------

df_turn.write.mode("overwrite").format("delta").saveAsTable(f"{catalogo}.{esquema}.turn")
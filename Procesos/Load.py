# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

dbutils.widgets.text("catalogo", "project_etl")
dbutils.widgets.text("esquema_source", "silver")
dbutils.widgets.text("esquema_sink", "gold")

# COMMAND ----------

catalogo = dbutils.widgets.get("catalogo")
esquema_source = dbutils.widgets.get("esquema_source")
esquema_sink = dbutils.widgets.get("esquema_sink")

# COMMAND ----------

df_clinic_trans = spark.table(f"{catalogo}.{esquema_source}.clinic_transformed")

# COMMAND ----------

df_clinic_trans.display()


# COMMAND ----------

df_clinic_trans.printSchema()

# COMMAND ----------

df_clinic_update = df_clinic_trans.groupBy(
    "DEPARTAMENTO",
    "CATEGORIA_TURNO",
    "NOMBRE_TURNO"
).agg(
    count("ID_TRABAJADOR").alias("TOTAL_TRABAJADORES"),
    collect_set("NOMBRE_PROFESION").alias("PROFESIONES")
).orderBy("TOTAL_TRABAJADORES", ascending=False)

# COMMAND ----------

df_clinic_update.display()

# COMMAND ----------

df_clinic_update.write.mode("overwrite").format("delta").option("mergeSchema", "true").saveAsTable(f"{catalogo}.{esquema_sink}.clinic_gold")
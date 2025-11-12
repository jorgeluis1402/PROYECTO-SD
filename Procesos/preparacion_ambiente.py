# Databricks notebook source
# MAGIC %md
# MAGIC ### Importan funciones y tipos de datos

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import * 

# COMMAND ----------

# MAGIC %md
# MAGIC ### WIDGETS
# MAGIC * Limpias widgets antiguos.
# MAGIC
# MAGIC * Creas un widget con valor por defecto.
# MAGIC
# MAGIC * Lees el valor del widget en una variable Python para usarlo en tu código.

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

dbutils.widgets.text("storageName", "adlsatalaya1402")


# COMMAND ----------

storageName = dbutils.widgets.get("storageName")


# COMMAND ----------


ruta = f"abfss://bronze@{storageName}.dfs.core.windows.net"



# COMMAND ----------

# MAGIC %md
# MAGIC ### Creacion de Catalogos,Esquemas 

# COMMAND ----------

spark.sql("CREATE CATALOG IF NOT EXISTS project_etl")

# COMMAND ----------

spark.sql("create schema if not exists project_etl.bronze");
spark.sql("create schema if not exists project_etl.silver");
spark.sql("create schema if not exists project_etl.gold");

# COMMAND ----------

# MAGIC %md
# MAGIC ### Eliminacion tablas Bronze

# COMMAND ----------

# Eliminación de tablas con PySpark ejecutando sentencias SQL
spark.sql("DROP TABLE IF EXISTS project_etl.bronze.workers")
spark.sql("DROP TABLE IF EXISTS project_etl.bronze.profession")
spark.sql("DROP TABLE IF EXISTS project_etl.bronze.turn")

# COMMAND ----------


## REMOVE DATA (Bronze)
dbutils.fs.rm(f"{ruta}/tablas/workers", True)
dbutils.fs.rm(f"{ruta}/tablas/profession", True)
dbutils.fs.rm(f"{ruta}/tablas/turn", True)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Creacion de los External Locations

# COMMAND ----------

spark.sql(f"""
CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-raw`
URL 'abfss://raw@{storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas raw del Data Lake';
""")

# COMMAND ----------

spark.sql(f"""
CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-bronze`
URL 'abfss://bronze@{storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas bronze del Data Lake';
""")

# COMMAND ----------

spark.sql(f"""
CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-silver`
URL 'abfss://silver@{storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas silver del Data Lake';
""")

# COMMAND ----------

spark.sql(f"""
CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-golden`
URL 'abfss://golden@{storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas golden del Data Lake';
""")
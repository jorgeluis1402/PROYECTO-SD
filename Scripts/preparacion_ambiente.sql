-- Databricks notebook source
-- MAGIC %md
-- MAGIC ### Importan funciones y tipos de datos

-- COMMAND ----------

-- MAGIC %python
-- MAGIC from pyspark.sql.functions import *
-- MAGIC from pyspark.sql.types import * 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### WIDGETS
-- MAGIC * Limpias widgets antiguos.
-- MAGIC
-- MAGIC * Creas un widget con valor por defecto.
-- MAGIC
-- MAGIC * Lees el valor del widget en una variable Python para usarlo en tu código.

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dbutils.widgets.removeAll()

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dbutils.widgets.text("storageName", "adlsatalaya1402")

-- COMMAND ----------

-- MAGIC %python
-- MAGIC storageName = dbutils.widgets.get("storageName")

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Creacion de Catalogos,Esquemas y Volumes

-- COMMAND ----------


CREATE CATALOG IF NOT EXISTS project_etl;

-- COMMAND ----------


create schema if not exists project_etl.bronze;
create schema if not exists project_etl.silver;
create schema if not exists project_etl.gold;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Creacion de los External Locations

-- COMMAND ----------



CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-raw`
URL 'abfss://raw@{storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas raw del Data Lake';


-- COMMAND ----------


CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-bronze`
URL 'abfss://bronze@{storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas bronze del Data Lake';


-- COMMAND ----------


CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-silver`
URL 'abfss://silver@{storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas silver del Data Lake';


-- COMMAND ----------


CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-golden`
URL 'abfss://golden@{storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas golden del Data Lake';

-- Databricks notebook source
-- MAGIC %python
-- MAGIC dbutils.widgets.removeAll()

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dbutils.widgets.text("storageName", "adlsatalaya1402")

-- COMMAND ----------

-- MAGIC %python
-- MAGIC storageName = dbutils.widgets.get("storageName")

-- COMMAND ----------

-- MAGIC %python
-- MAGIC ruta = f"abfss://bronze@{storageName}.dfs.core.windows.net"

-- COMMAND ----------


DROP TABLE IF EXISTS project_etl.bronze.workers;
DROP TABLE IF EXISTS project_etl.bronze.profession;
DROP TABLE IF EXISTS project_etl.bronze.turn;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC ##  REMOVE DATA (Bronze)
-- MAGIC
-- MAGIC dbutils.fs.rm(f"{ruta}/tablas/workers", True)
-- MAGIC dbutils.fs.rm(f"{ruta}/tablas/profession", True)
-- MAGIC dbutils.fs.rm(f"{ruta}/tablas/turn", True)
-- MAGIC
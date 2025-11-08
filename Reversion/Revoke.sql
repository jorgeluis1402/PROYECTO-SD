-- Databricks notebook source

--GRANT USE SCHEMA ON SCHEMA project_etl.bronze TO `vbran2022@gmail.com`;
--GRANT CREATE ON SCHEMA project_etl.bronze TO `vbran2022@gmail.com`;

REVOKE USAGE, CREATE
ON SCHEMA project_etl.bronze
FROM `vbran2022@gmail.com`;



-- COMMAND ----------

--GRANT SELECT ON TABLE project_etl.bronze.turn TO `juanchavez1879@gmail.com`;

REVOKE SELECT ON TABLE project_etl.bronze.turn FROM `juanchavez1879@gmail.com`;

-- COMMAND ----------

--GRANT SELECT ON TABLE project_etl.gold.clinic_gold TO `Analistas`;

REVOKE SELECT ON TABLE project_etl.gold.clinic_gold FROM `Analistas`;
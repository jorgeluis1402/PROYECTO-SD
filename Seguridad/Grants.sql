-- Databricks notebook source



GRANT SELECT ON TABLE project_etl.bronze.profession TO `vbran2022@gmail.com`;


-- COMMAND ----------



GRANT SELECT ON TABLE project_etl.bronze.turn TO `juanchavez1879@gmail.com`;

-- COMMAND ----------


GRANT SELECT ON TABLE project_etl.bronze.workers TO `jorgluis1402@gmail.com`;


-- COMMAND ----------


GRANT SELECT ON TABLE project_etl.silver.clinic_transformed TO `dangarcia3010@gmail.com`;

-- COMMAND ----------


GRANT SELECT ON TABLE project_etl.gold.clinic_gold TO `Analistas`;

-- COMMAND ----------



GRANT USE SCHEMA ON SCHEMA project_etl.bronze TO `Desarrolladores`;

GRANT CREATE ON SCHEMA project_etl.bronze TO `Desarrolladores`;


-- COMMAND ----------



GRANT USE SCHEMA ON SCHEMA project_etl.gold TO `Analistas`;

GRANT CREATE ON SCHEMA project_etl.gold TO `Analistas`;

-- COMMAND ----------


SHOW GRANTS ON TABLE project_etl.bronze.workers;


-- COMMAND ----------


SHOW GRANTS ON SCHEMA project_etl.bronze;



-- COMMAND ----------



SHOW GRANTS ON CATALOG project_etl;


-- COMMAND ----------


SHOW GRANTS ON TABLE project_etl.silver.clinic_transformed;
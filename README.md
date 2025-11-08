<div align="center">

# ☕ Clinica MEDIC+SALUD ETL Pipeline
### Arquitectura Medallion en Azure Databricks

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta&logoColor=white)](https://delta.io/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

*Pipeline automatizado de datos para análisis con arquitectura de tres capas y despliegue continuo*

</div>


🏥 PROYECTO-SD — ETL Clínica Medic+Salud

📊 Arquitectura Medallón en Azure Databricks

📌 Descripción del Proyecto

Este proyecto desarrolla un pipeline ETL para la clínica Medic+Salud, con el objetivo de transformar datos operativos en información estructurada y disponible para análisis y generación de dashboards.

Se utiliza la arquitectura Medallón (Bronze – Silver – Gold) para gestionar y optimizar la calidad del dato dentro de un Data Lake en Azure.

✅ Objetivos Principales

Centralizar datos de la clínica en una estructura confiable
Automatizar la ingestión y transformación de datos
Preparar información para analítica y visualización avanzada
Garantizar calidad y trazabilidad del dato

🧱 Arquitectura del Proyecto

🔹 Diseño Medallón
Capa	                      Propósito	Productos
======================================================
Bronze            	Datos crudos desde landing/raw	
Silver            	Limpieza, tipado y estandarización	
Gold	              Modelos para analítica y reporting	

🛠️ Tecnologías Utilizadas

  Área	                                Tecnologías
  =======================================================
Cloud & Data Lake	          Azure Storage Account, Azure Containers
Procesamiento	              Azure Databricks — PySpark / SQL
Gestión	                    Unity Catalog, Delta Lake
Control de versiones	      GitHub
Visualización	              Dashboard 


📂 Datos utilizados

Se cargaron 3 archivos CSV originales en el contenedor raw del Data Lake:

Dataset                    	Descripción	Registros
clinic_works.csv	          Trabajadores de la clínica	50
clinic_profession.csv      	Especialidades médicas	8
clinic_turn.csv	            Turnos de trabajo	3


🔄 Flujo ETL

1️⃣ Ingesta desde Azure Storage → Bronze
2️⃣ Limpieza y normalización → Silver
3️⃣ Joins + métricas clínicas → Gold
4️⃣ Exportación a dashboards

✅ Resultados

Datos unificados por trabajador, especialidad y turno
Creación de modelos para análisis de RRHH clínico
Dashboard visual listo para gestión de personal

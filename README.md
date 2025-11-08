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



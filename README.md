<div align="center">

# ☕ Clinica MEDIC+SALUD ETL Pipeline
### Arquitectura Medallion en Azure Databricks

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta&logoColor=white)](https://delta.io/)
|![Dashboard](https://img.shields.io/badge/Dashboard-Azure%20Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

*Pipeline automatizado de datos para análisis con arquitectura de tres capas y despliegue continuo*

</div>



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

## 🛠️ Tecnologías

<div align="center">

| Tecnología | Propósito |
|:----------:|:----------|
| ![Databricks](https://img.shields.io/badge/Azure_Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white) | Motor de procesamiento distribuido Spark |
| ![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=flat-square&logo=delta&logoColor=white) | Storage layer con ACID transactions |
| ![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat-square&logo=apache-spark&logoColor=white) | Framework de transformación de datos |
| ![ADLS](https://img.shields.io/badge/ADLS_Gen2-0078D4?style=flat-square&logo=microsoft-azure&logoColor=white) | Data Lake para almacenamiento persistente |
| ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white) | Automatización CI/CD |
| ![Dashboard](https://img.shields.io/badge/Dashboard-Azure%20Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white) | Visualización |


</div>

---

## ⚙️ Requisitos Previos

- ☁️ Cuenta de Azure con acceso a Databricks
- 💻 Workspace de Databricks configurado
- 🖥️ Cluster activo (nombre: `cluster_SD`)
- 🐙 Cuenta de GitHub con permisos de administrador
- 📦 Azure Data Lake Storage Gen2 configurado



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


## 📁 Estructura del Proyecto

```
clinic medic+salud -etl/
│
├── 📂 .github/
│   └── 📂 workflows/
│       └── 📄 databricks-deploy.yml    # Pipeline CI/CD
│
├── 📂 proceso/
│   ├── 📄 1-environment preparation.sql         # Creación de esquema
│   ├── 🐍 2-Ingest-Coffee-Shop-Data.py          # Bronze Layer
│   ├── 🐍 3-Transform.py                        # Silver Layer
│   └── 🐍 4-Load.py                             # Gold Layer
│
└── 📄 README.md
```


✅ Resultados

Datos unificados por trabajador, especialidad y turno
Creación de modelos para análisis de RRHH clínico
Dashboard visual listo para gestión de personal

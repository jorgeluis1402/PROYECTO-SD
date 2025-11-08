<div align="center">

##  Clinica MEDIC+SALUD ETL Pipeline

### Arquitectura Medallion en Azure Databricks

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com/)
[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)](https://spark.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-00ADD8?style=for-the-badge&logo=delta&logoColor=white)](https://delta.io/)
|![Dashboard](https://img.shields.io/badge/Dashboard-Azure%20Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)

*Pipeline automatizado de datos para análisis con arquitectura de tres capas y despliegue continuo*

</div>


## 🎯 Descripción del Proyecto

Este proyecto desarrolla un pipeline ETL en Azure Databricks para la clínica MEDIC+SALUD, transformando datos operativos (personal y turnos médicos) en información estructurada lista para analítica y tableros clínicos.

Implementa la Arquitectura Medallón con Delta Lake para garantizar calidad del dato, auditoría, versionamiento y consistencia ACID.


**Objetivos**:

- ✅  Centralizar datos operativos de clínica
- ✅ Automatizar ingestión y transformación
- ✅ Optimizar calidad del dato
- ✅ Habilitar reporting y dashboards médicos
  

##🏗️ Arquitectura

##📌 Flujo ETL

        📄 CSV en Data Lake (RAW)
                ↓
        🥉 Bronze → Ingesta sin cambios
                ↓
        🥈 Silver → Limpieza y modelo dimensional
                ↓
        🥇 Gold → Métricas para dashboards
                ↓
        📊 Databricks SQL Dashboards


## 📂 Datos Utilizados

| Dataset                 | Descripción            | Registros |
| ----------------------- | ---------------------- | :-------: |
| `clinic_workers.csv`    | Trabajadores clínicos  |     50    |
| `clinic_profession.csv` | Especialidades médicas |     8     |
| `clinic_turn.csv`       | Turnos asignados       |     3     |


## 📦 Capas del Pipeline

| Capa       | Propósito                  | Ejemplo de Tablas                                                   |
| ---------- | -------------------------- | ------------------------------------------------------------------- |
| **Bronze** | Aterrizaje de datos crudos | `bronze.clinic_workers,bronze.clinic_profession,clinic_bronze.turn` |
| **Silver** | Limpieza + Modelado        | ` clinic_transformed`                                               |
| **Gold**   | Métricas para BI           | `clinic_gold`                                                       |





## 📁 Estructura del Repositorio

clinic-medic-salud-etl/
│
├── .github/workflows/
│   └── databricks-deploy.yml    ← CI/CD automático
│
├── proceso/
│   ├── 1-Ddls-Medallion.sql    ← Creación de esquema
│   ├── 2-Ingest.py               ← Bronze: ingesta raw
│   ├── 3-Transform.py            ← Silver: modelo clínico
│   └── 4-Load.py                 ← Gold: métricas
│
└── README.md


📊 Modelo de Datos (Silver – Star Schema)
           DIM_PROFESION
                |
                |
DIM_TURNO — HECHO_TRABAJADOR — (futuro) DIM_AREA
                |
           (Fact Table Clínica)

✅ HECHO_TRABAJADOR
Campo	Tipo	Descripción
id_trabajador	INT	Identificador del trabajador
id_profesion	INT	Especialidad médica (FK)
id_turno	INT	Turno asignado (FK)
salario	DOUBLE	Sueldo mensual
fecha_procesamiento	TIMESTAMP	Auditoría
✅ DIM_PROFESION
Campo	Descripción
id_profesion	PK
nombre_profesion	Médico, cirujano, etc.
✅ DIM_TURNO
Campo	Descripción
id_turno	PK
horario	Mañana, Tarde, Noche
🛠️ Tecnologías
Tecnología	Función
Azure Databricks	Motor de ejecución
Delta Lake	ACID + versionamiento
PySpark	Transformaciones
ADLS Gen2	Data Lake
GitHub Actions	CI/CD
SQL Dashboards	Visualización
🚀 Ejecución
🔄 Despliegue Automático CI/CD
git add .
git commit -m "update: nuevas reglas transformación clínica"
git push origin main


✅ GitHub Actions:

Exporta notebooks

Ejecuta workflow en Databricks

Corre ETL: Bronze → Silver → Gold

▶️ Ejecución Manual en Databricks

Orden recomendado:

1️⃣ 1-1-Ddls-Medallion.sql    → Crear estructura
2️⃣ 2-Ingest.py               → Ingesta a Bronze
3️⃣ 3-Transform.py            → Silver
4️⃣ 4-Load.py                 → Gold

📈 Visualización del Gold Layer

Actualmente se conectan dashboards desde:

✅ Databricks SQL Dashboards

⏳ Power BI (en iteración futura)

KPIs iniciales:

KPI	Objetivo
Distribución de especialidades	Análisis de capacidad
Staff por franja horaria	Planificación operativa
Relación sueldo vs. especialidad	Optimización del gasto
🧩 Próximas Extensiones

✅ Relacionar trabajadores → pacientes → atenciones
🚧 KPI: productividad por médico
🚧 Integración historizada de planillas
🚧 Power BI con DirectQuery

👨‍💻 Autor
<div align="center">
Jorge Luis Atalaya Alva




Data Engineering | Azure Databricks | Delta Lake | CI/CD

</div>
📝 Licencia

Proyecto bajo licencia MIT.

✅ Resultados

Datos unificados por trabajador, especialidad y turno
Creación de modelos para análisis de RRHH clínico
Dashboard visual listo para gestión de personal

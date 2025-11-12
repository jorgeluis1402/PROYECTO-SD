# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F


# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

dbutils.widgets.text("catalogo", "project_etl")
dbutils.widgets.text("esquema_source", "bronze")
dbutils.widgets.text("esquema_sink", "silver")

# COMMAND ----------

catalogo = dbutils.widgets.get("catalogo")
esquema_source = dbutils.widgets.get("esquema_source")
esquema_sink = dbutils.widgets.get("esquema_sink")

# COMMAND ----------

df_workers = spark.table(f"{catalogo}.{esquema_source}.workers")
df_profession = spark.table(f"{catalogo}.{esquema_source}.profession")
df_turn = spark.table(f"{catalogo}.{esquema_source}.turn")


# COMMAND ----------

# MAGIC %md
# MAGIC ### TRANSFORMATION - WORKERS
# MAGIC * Concatenar nombre + apellido → nombre_completo

# COMMAND ----------

df_workers_trans = df_workers \
    .withColumn("nombre_completo", concat_ws(" ", "nombre", "apellido")) \
    .select("id_trabajador", "nombre_completo", "id_profesion", "id_turno")



# COMMAND ----------

display(df_workers_trans)

# COMMAND ----------

# MAGIC %md
# MAGIC ### TRANSFORMATION - PROFESSION
# MAGIC * Crear una columna 'categoria_profesional' basada en el departamento

# COMMAND ----------



df_profession_trans = df_profession.withColumn(
    "categoria_profesional",
    when(
        col("departamento").isin("Especialidades", "Quirófano"), "Especializada"
    )
    .when(
        col("departamento").isin("Medicina General", "Enfermería"), "Asistencia Básica"
    )
    .when(
        col("departamento").isin("Laboratorio", "Imágenes", "Farmacia"), "Diagnóstico/Apoyo"
    )
    .otherwise("Administrativo/General")
)



# COMMAND ----------

display(df_profession_trans)

# COMMAND ----------

# MAGIC %md
# MAGIC ### TRANSFORMATION - TURN
# MAGIC * Crear funcion Tipo Jornada

# COMMAND ----------


def categoria_turno(nombre):
    if nombre == "Mañana":
        return "Diurno"
    elif nombre == "Tarde":
        return "Mixto"
    else:
        return "Nocturno"



# COMMAND ----------

# Registrar UDF
udf_categoria = udf(categoria_turno, StringType())

# COMMAND ----------

# Aplicar la UDF al DataFrame
df_turn_trans = df_turn.withColumn("categoria_turno", udf_categoria("nombre_turno"))

# COMMAND ----------

df_turn_trans.display()

# COMMAND ----------


df_joined = (
    df_workers_trans.alias("w")
    .join(df_profession_trans.alias("p"), col("w.id_profesion") == col("p.id_profesion"), "left")
    .join(df_turn_trans.alias("t"), col("w.id_turno") == col("t.id_turno"), "left")
)

# COMMAND ----------

df_joined.display()

# COMMAND ----------

df_clinic_trans = df_joined.select(
    col("w.id_trabajador"),
    col("w.nombre_completo"),
    col("p.nombre_profesion"),
    col("p.departamento"),
    col("p.categoria_profesional"),
    col("t.nombre_turno"),
    col("t.inicio_horario"),
    col("t.fin_horario"),
    col("t.categoria_turno")
)

# COMMAND ----------

df_clinic = df_clinic_trans.toDF(*[c.upper() for c in df_clinic_trans.columns])

# COMMAND ----------

df_clinic.display()

# COMMAND ----------

df_clinic.write.format("delta") \
    .option("mergeSchema", "true") \
    .mode("overwrite") \
    .saveAsTable(f"{catalogo}.{esquema_sink}.clinic_transformed")

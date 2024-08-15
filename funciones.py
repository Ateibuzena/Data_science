from typing import Type
import pyspark

def shape(tabla_spark: Type[pyspark.sql.dataframe.DataFrame]):
    shape_pyspark = (tabla_spark.count(), len(tabla_spark.columns))
    return shape_pyspark

def obtener_metricas(conjunto):
    diccionario = {"MAE": conjunto.meanAbsoluteError,
                   "RMSE": conjunto.rootMeanSquaredError,
                   "r2": conjunto.r2,
                   "r2_ajustado": conjunto.r2adj}
    
    return diccionario

# Importar las metricas de clasificaciones
from pyspark.mllib.evaluation import MulticlassMetrics

def obtener_metricas_clasificacion(Y):
    metrics = MulticlassMetrics(Y.rdd)
    # Crear el diccionario con las métricas
    metricas_dict = {
                    "Confusion Matrix": metrics.confusionMatrix().toArray(),
                    "Precision label 0": metrics.precision(label=0.0),
                    "Precision label 1": metrics.precision(label=1.0),
                    "Recall label 0": metrics.recall(label=0.0),
                    "Recall label 1": metrics.recall(label=1.0),
                    "F1-Score label 0": metrics.fMeasure(label=0.0),
                    "F1-Score label 1": metrics.fMeasure(label=1.0),
                    "Accuracy": metrics.accuracy,
                    "Falsos positivos label 0": metrics.falsePositiveRate(label=0.0),
                    "Falsos positivos label 1": metrics.falsePositiveRate(label=1.0)
                    }
    return metricas_dict
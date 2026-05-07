from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def add_market_pressure_flag(df: DataFrame, threshold: float = 75.0) -> DataFrame:
    return df.withColumn(
        "market_pressure_flag",
        F.when(F.col("avg_market_price") >= threshold, 1).otherwise(0)
    )


def add_operations_stress_flag(df: DataFrame, threshold: int = 3) -> DataFrame:
    return df.withColumn(
        "operations_stress_flag",
        F.when(F.col("elevated_incident_count") >= threshold, 1).otherwise(0)
    )
from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def add_market_pressure_flag(df: DataFrame, threshold: float = 75.0) -> DataFrame:
    return df.withColumn(
        "is_high_market_price",
        F.when(F.col("avg_price_eur_mwh") >= threshold, 1).otherwise(0)
    )


def add_weather_risk_signal(df: DataFrame, wind_threshold: float = 30.0) -> DataFrame:
    return df.withColumn(
        "weather_risk_signal",
        F.when(
            (F.col("avg_wind_speed_kmh") >= wind_threshold)
            | (F.col("weather_alert_count") > 0),
            "WEATHER_RISK"
        ).otherwise("NORMAL")
    )


def add_operational_status(df: DataFrame) -> DataFrame:
    return df.withColumn(
        "operational_status",
        F.when(F.col("elevated_incident_count") > 0, "ATTENTION")
        .otherwise("NORMAL")
    )
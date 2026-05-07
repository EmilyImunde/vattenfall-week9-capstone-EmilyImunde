from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def standardize_weather_columns(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("region", F.upper(F.trim(F.col("region"))))
        .withColumn("weather_alert_level", F.upper(F.trim(F.col("weather_alert_level"))))
    )

def cast_weather_fields(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("temperature_c", F.col("temperature_c").cast("double"))
        .withColumn("wind_speed_kmh", F.col("wind_speed_kmh").cast("double"))
        .withColumn("precipitation_mm", F.col("precipitation_mm").cast("double"))
    )

def add_weather_day(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("report_day", F.to_date("event_date"))
    )

def filter_invalid_weather(df: DataFrame) -> DataFrame:
    return (
        df
        .filter(F.col("temperature_c").isNotNull())
        .filter(F.col("wind_speed_kmh").isNotNull())
        .filter(F.col("report_day").isNotNull())
    )

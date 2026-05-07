from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def standardize_grid_event_columns(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("region", F.upper(F.trim(F.col("region"))))
        .withColumn("event_type", F.upper(F.trim(F.col("event_type"))))
        .withColumn("severity", F.upper(F.trim(F.col("severity"))))
    )

def cast_grid_event_fields(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("duration_minutes", F.col("duration_minutes").cast("int"))
        .withColumn("event_timestamp", F.to_timestamp("event_ts"))
    )

def add_grid_event_day(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("event_day", F.to_date("event_timestamp"))
    )

def add_severity_band(df: DataFrame) -> DataFrame:
    """Add severity_band based on severity levels"""
    return (
        df
        .withColumn(
            "severity_band",
            F.when(F.col("severity") == "LOW", "MINOR")
            .when(F.col("severity") == "MEDIUM", "MODERATE")
            .when(F.col("severity") == "HIGH", "MAJOR")
            .when(F.col("severity") == "CRITICAL", "CRITICAL")
            .otherwise("UNKNOWN")
        )
    )

def filter_invalid_grid_events(df: DataFrame) -> DataFrame:
    return (
        df
        .filter(F.col("duration_minutes").isNotNull())
        .filter(F.col("duration_minutes") >= 0)
        .filter(F.col("event_day").isNotNull())
    )

def transform_grid_events(df: DataFrame) -> DataFrame:
    """Complete grid events transformation pipeline"""
    return (
        df
        .transform(standardize_grid_event_columns)
        .transform(cast_grid_event_fields)
        .transform(add_grid_event_day)
        .transform(add_severity_band)  # ✅ Added this line
        .transform(filter_invalid_grid_events)
    )
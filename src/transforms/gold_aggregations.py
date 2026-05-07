from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def aggregate_daily_market_summary(df: DataFrame) -> DataFrame:
    return (
        df
        .groupBy("report_day", "region")
        .agg(
            F.round(F.avg("price_eur_mwh"), 2).alias("avg_price_eur_mwh"),
            F.round(F.min("price_eur_mwh"), 2).alias("min_price_eur_mwh"),
            F.round(F.max("price_eur_mwh"), 2).alias("max_price_eur_mwh"),
            F.round(F.sum("volume_mwh"), 2).alias("total_volume_mwh"),
            F.count("*").alias("market_record_count"),
        )
    )


def aggregate_weather_impact_summary(df: DataFrame) -> DataFrame:
    return (
        df
        .groupBy("report_day", "region")
        .agg(
            F.round(F.avg("temperature_c"), 2).alias("avg_temperature_c"),
            F.round(F.avg("wind_speed_kmh"), 2).alias("avg_wind_speed_kmh"),
            F.round(F.max("wind_speed_kmh"), 2).alias("max_wind_speed_kmh"),
            F.round(F.sum("precipitation_mm"), 2).alias("total_precipitation_mm"),
            F.count("*").alias("weather_record_count"),
            F.sum(
                F.when(F.col("weather_alert_level") != "NONE", 1).otherwise(0)
            ).alias("weather_alert_count"),
        )
    )


def aggregate_grid_incident_summary(df: DataFrame) -> DataFrame:
    return (
        df
        .groupBy("event_day", "region", "severity_band")
        .agg(
            F.count("*").alias("incident_count"),
            F.sum("duration_minutes").alias("total_duration_minutes"),
            F.round(F.avg("duration_minutes"), 2).alias("avg_duration_minutes"),
            F.countDistinct("asset_id").alias("affected_asset_count"),
            F.sum(
                F.when(F.col("severity_band") == "ELEVATED", 1).otherwise(0)
            ).alias("elevated_incident_count"),
        )
    )
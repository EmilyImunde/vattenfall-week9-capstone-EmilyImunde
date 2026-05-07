from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def build_regional_operations_base(
    grid_df: DataFrame,
    asset_df: DataFrame,
    weather_df: DataFrame
) -> DataFrame:
    clean_grid_df = (
        grid_df
        .select(
            "event_id",
            "event_day",           # ✅ Removed duplicate event_date
            "event_ts",            # ✅ Changed from event_timestamp
            "region",
            "asset_id",
            "event_type",
            "severity",
            "severity_band",
            "duration_minutes",
            "source_system",
        )
    )

    clean_asset_df = (
        asset_df
        .select(
            "asset_id",
            F.col("asset_name"),
            F.col("asset_type"),
            F.col("region").alias("asset_region"),
        )
    )

    clean_weather_df = (
        weather_df
        .select(
            F.col("region").alias("weather_region"),
            "report_day",
            "temperature_c",
            "wind_speed_kmh",
            "precipitation_mm",
            "weather_alert_level",
        )
    )

    return (
        clean_grid_df.alias("g")
        .join(clean_asset_df.alias("a"), on="asset_id", how="left")
        .join(
            clean_weather_df.alias("w"),
            (F.col("g.region") == F.col("w.weather_region"))
            & (F.col("g.event_day") == F.col("w.report_day")),
            how="left"
        )
    )
from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def add_asset_risk_category(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn(
            "asset_risk_category",
            F.when(F.col("elevated_incident_count") >= 5, "CRITICAL")
            .when(F.col("elevated_incident_count") >= 3, "HIGH")
            .when(F.col("total_incident_count") >= 3, "MEDIUM")
            .otherwise("LOW")
        )
    )


def add_combined_stress_label(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn(
            "combined_stress_label",
            F.when(
                (F.col("market_pressure_flag") == 1)
                & (F.col("operations_stress_flag") == 1),
                "COMBINED_STRESS"
            )
            .when(F.col("market_pressure_flag") == 1, "MARKET_PRESSURE")
            .when(F.col("operations_stress_flag") == 1, "OPERATIONS_PRESSURE")
            .otherwise("NORMAL")
        )
    )


def add_executive_risk_status(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn(
            "executive_risk_status",
            F.when(F.col("combined_stress_label") == "COMBINED_STRESS", "CRITICAL")
            .when(F.col("weather_grid_risk_score") >= 2, "ATTENTION")
            .when(F.col("combined_stress_label").isin("MARKET_PRESSURE", "OPERATIONS_PRESSURE"), "WATCH")
            .otherwise("NORMAL")
        )
    )
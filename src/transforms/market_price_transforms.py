from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def standardize_market_price_columns(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("region", F.upper(F.trim(F.col("region"))))
        .withColumn("market_type", F.upper(F.trim(F.col("market_type"))))
    )

def cast_market_price_fields(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("price_eur_mwh", F.col("price_eur_mwh").cast("double"))
        .withColumn("volume_mwh", F.col("volume_mwh").cast("double"))
    )

def add_market_price_day(df: DataFrame) -> DataFrame:
    return (
        df
        .withColumn("report_day", F.to_date("event_date"))
    )

def filter_invalid_market_prices(df: DataFrame) -> DataFrame:
    return (
        df
        .filter(F.col("price_eur_mwh").isNotNull())
        .filter(F.col("volume_mwh").isNotNull())
        .filter(F.col("report_day").isNotNull())
    )
def transform_market_prices(df: DataFrame) -> DataFrame:
    """Complete market price transformation pipeline"""
    return (
        df
        .transform(standardize_market_price_columns)
        .transform(cast_market_price_fields)
        .transform(add_market_price_day)
        .transform(filter_invalid_market_prices)
    )
       
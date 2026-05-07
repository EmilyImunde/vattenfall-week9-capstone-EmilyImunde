from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def count_duplicate_grain(df: DataFrame, grain_columns: list) -> int:
    return (
        df
        .groupBy(*grain_columns)
        .count()
        .filter(F.col("count") > 1)
        .count()
    )


def count_nulls(df: DataFrame, column_name: str) -> int:
    return df.filter(F.col(column_name).isNull()).count()
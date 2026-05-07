from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def count_nulls(df: DataFrame, column_name: str) -> int:
    return df.filter(F.col(column_name).isNull()).count()

def count_duplicate_grain(df: DataFrame, grain_columns: list) -> int:
    return (
        df
        .groupBy(*grain_columns)
        .count()
        .filter(F.col("count") > 1)
        .count()
    )

def print_basic_quality_summary(df: DataFrame, table_name: str) -> None:
    """Print basic quality metrics for a Silver table."""
    print(f"\n=== Quality Summary for {table_name} ===")
    print(f"Total rows: {df.count():,}")
    
    # Check null counts for all columns
    print("\nNull counts by column:")
    for column in df.columns:
        null_count = count_nulls(df, column)
        if null_count > 0:
            print(f"  {column}: {null_count:,}")
    
    print("\n" + "="*50 + "\n")

    
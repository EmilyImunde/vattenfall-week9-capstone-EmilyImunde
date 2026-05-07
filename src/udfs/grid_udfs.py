from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

@udf(StringType())
def classify_severity_band(severity):
    if severity is None:
        return "UNKNOWN"
    value = str(severity).upper()
    if value in ("CRITICAL", "HIGH"):
        return "ELEVATED"
    if value == "MEDIUM":
        return "WATCH"
    return "NORMAL"

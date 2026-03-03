from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def add_total_column(df):
    return df.withColumn("total", col("a") + col("b"))

def filter_positive_totals(df):
    return df.filter(col("total") > 0)

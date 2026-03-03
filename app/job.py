from pyspark.sql import SparkSession
from app.transformations import add_total_column, filter_positive_totals

def run_job():
    spark = SparkSession.builder.appName("job").getOrCreate()

    data = [(1, 2), (-5, 1)]
    df = spark.createDataFrame(data, ["a", "b"])

    df = add_total_column(df)
    df = filter_positive_totals(df)

    df.show()
    spark.stop()

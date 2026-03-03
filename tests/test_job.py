from app.transformations import add_total_column, filter_positive_totals

def test_job_logic_filters_negatives(spark):
    data = [(1, 2), (-5, 1)]
    df = spark.createDataFrame(data, ["a", "b"])

    result = add_total_column(df)
    result = filter_positive_totals(result)

    rows = result.collect()

    assert df.where(col("total") < 0).count() == 0
    assert rows[0]["total"] == 3

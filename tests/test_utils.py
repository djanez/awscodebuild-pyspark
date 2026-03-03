from app.transformations import add_total_column, filter_positive_totals

def test_add_total_column(spark):
    data = [(1, 2), (3, 4)]
    df = spark.createDataFrame(data, ["a", "b"])
    result = add_total_column(df)

    expected_data = [(1, 2, 3), (3, 4, 7)]
    expected_df = spark.createDataFrame(expected_data, ["a", "b", "total"])

    assert sorted(result.collect()) == sorted(expected_df.collect())


def test_filter_positive_totals(spark):
    data = [(1, 2, 3), (-5, 1, -4)]
    df = spark.createDataFrame(data, ["a", "b", "total"])
    result = filter_positive_totals(df)

    expected_data = [(1, 2, 3)]
    expected_df = spark.createDataFrame(expected_data, ["a", "b", "total"])

    assert result.collect() == expected_df.collect()

import dask.dataframe as dd

# partitioning the data
athlete_df = dd.fron_pandas(df, npartitions=4)

# computing the average age of all the atheletes
result_df = athlete_df.groupby('Year').Age.mean().compute()

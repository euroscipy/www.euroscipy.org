Title:Apache Parquet as a columnar storage for large datasets
URL:2018/descriptions/Apache Parquet as a columnar storage for large datasets.html
save_as: 2018/descriptions/Apache Parquet as a columnar storage for large datasets.html



# Apache Parquet as a columnar storage for large datasets
# Apache Parquet Data Format

Apache Parquet is a binary, efficient columnar data format. It uses various
techniques to store data in a CPU and I/O efficient way like row groups,
compression for pages in column chunks or dictionary encoding for columns.
Index hints and statistics to quickly skip over chunks of irrelevant data
enable efficient queries on large amount of data.

# Apache Parquet with Pandas & Dask

Apache Parquet files can be read into Pandas DataFrames with the two libraries
fastparquet and Apache Arrow. While Pandas is mostly used to work with data
that fits into memory, Apache Dask allows us to work with data larger then memory 
and even larger than local disk space. Data can be split up into partitions
and stored in cloud object storage systems like Amazon S3 or Azure Storage.

Using Metadata from the partiton filenames, parquet column statistics and
dictonary filtering allows faster performance for selective queries without
reading all data. This talk will show how use partitioning, 
row group skipping and general data layout to speed up queries on large
amount of data.
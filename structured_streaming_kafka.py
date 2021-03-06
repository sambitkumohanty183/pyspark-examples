
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = (SparkSession
    .builder
    .appName("StructuredStreamingWithKafka")
    .getOrCreate())
# Subscribe to 1 topic

raw = spark
  .readStream()
  .format("kafka")
  .option("kafka.bootstrap.servers", "localhost:9092")
  .option("subscribe", "demo")
  .load()
  
query = (raw
    .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
    .writeStream
    .format("console")
    .start())

query.awaitTermination()

"""

Launch spark application
$ bin/spark-sumbit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.0,org.xerial.snappy:snappy-java:1.1.4 structured_streaming_kafka.py
"""

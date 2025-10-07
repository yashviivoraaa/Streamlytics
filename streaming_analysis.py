from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

spark = SparkSession.builder.appName("CFPBStreaming").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

schema = """
    date_received STRING,
    product STRING,
    sub_product STRING,
    issue STRING,
    company STRING,
    complaint_what_happened STRING
"""

df = spark.readStream.schema(schema).json("streaming_data")

agg_df = df.groupBy("product").count().orderBy("count", ascending=False)

def write_to_csv(batch_df, batch_id):
    output_path = "dashboard_output/agg.csv"
    batch_df.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)

query = agg_df.writeStream \
    .outputMode("complete") \
    .foreachBatch(write_to_csv) \
    .start()

query.awaitTermination()

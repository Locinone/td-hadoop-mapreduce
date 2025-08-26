import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, to_timestamp

spark = SparkSession.builder \
    .appName("OrganizeTweets") \
    .getOrCreate()

# Lire le JSON depuis HDFS
df = spark.read.json("hdfs://namenode:9000/twitter_data/tweets_with_locations.json")

# Convertir le timestamp et extraire année et mois
df = df.withColumn("timestamp_ts", to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss")) \
       .withColumn("year", date_format(col("timestamp_ts"), "yyyy")) \
       .withColumn("month", date_format(col("timestamp_ts"), "MM"))

# Sauvegarder les tweets partitionnés par année et mois
df.write.partitionBy("year", "month") \
       .mode("overwrite") \
       .json("hdfs://namenode:9000/twitter_data_partitioned")

spark.stop()

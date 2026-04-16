from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, avg
from pyspark.sql.window import Window

# Step 1: Create Spark Session
spark = SparkSession.builder \
    .appName("Lab Test Processing") \
    .getOrCreate()

# Step 2: Load CSV Data
df = spark.read.csv("../data/processing/cleaned_lab_results.csv", header=True, inferSchema=True)

# Step 3: Show Data
df.show(5)

# Step 4: Print Schema
df.printSchema()

# Step 5: Ensure proper date format
df = df.withColumn("collection_date", to_date(col("collection_date")))

# Step 6: Window Function (rolling avg)
window_spec = Window.partitionBy("patient_id") \
    .orderBy(col("collection_date")) \
    .rowsBetween(-30, 0)

df = df.withColumn("avg_last_30_days", avg("test_value").over(window_spec))

# Step 7: Show results
df.select("patient_id", "collection_date", "test_value", "avg_last_30_days").show(10)

# Step 8: Save as Parquet with partitioning
df.write \
    .partitionBy("collection_date") \
    .mode("overwrite") \
    .parquet("../data/output/lab_results_parquet")

# Step 9: Stop Spark (ALWAYS at end)
spark.stop()

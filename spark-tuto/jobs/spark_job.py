from pyspark.sql import SparkSession  
# Initialize Spark session 
spark = SparkSession.builder.appName("IrisDataProcessing").getOrCreate()  

# Read the dataset 
df = spark.read.csv("/data/inputs/iris.csv", inferSchema=True, header=False)  

# Rename columns 
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"] 

df = df.toDF(*columns)  
# Perform a basic data manipulation: calculate average sepal length by species 

avg_sepal_length = df.groupBy("species").avg("sepal_length")  

# Write the results back to the Docker volume 
avg_sepal_length.write.csv("/data/outputs/avg_sepal_length_by_species")  

# Stop the Spark session 
spark.stop()
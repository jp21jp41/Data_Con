#pyspark_hdfs_test
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
import hdfs
import os

"""
NOTE: PYSPARK PATHS ARE ONLY NECESSARY IF YOUR DEFAULT PATH DOES NOT HAVE THE NECESSARY INSTALLATIONS
Otherwise, please note difference between your directories and the ones listed.
"""

# Pyspark Paths
os.environ['PYSPARK_PYTHON'] = "~/Python/Python311/python.exe"
os.environ['PYSPARK_DRIVER_PYTHON'] = "~/Python/Python311/python.exe"

# Spark Home Path
os.environ['SPARK_HOME'] = "C:/spark/spark-3.5.5-bin-hadoop3"

# Hadoop Home Path
os.environ['HADOOP_HOME'] = 'C:/hadoop'

# Java Home Path
os.environ['JAVA_HOME'] = "C:\Program Files\Java\jdk-17"

#Basic Hadoop Client Test
client = hdfs.InsecureClient('http://localhost:9870', user='~')
print("Client:")
print(client)



table_path = "<userdirectory>/spark-warehouse/testpysparktable"

# HDFS Deletion Dependent on whether the status of the client is successful
table_path_status = client.status(table_path, strict=False)
if table_path_status != None:
    client.delete(table_path)


#if os.path.exists(table_path):
#  os.remove(table_path)

# Start Spark Session
spark = SparkSession.builder.appName("SimpleSparkApp").getOrCreate()

# Dataframe to test on
df = [("Steve", "Hat", "Blue", "16.99"), ("Bob", "Radio", "Purple", "35.99"), ("Louise", "Lightbulbs", "White", "20.00")]

# Schema
schema1 = StructType([
   StructField("People", StringType(), True),
   StructField("Item", StringType(), True),
   StructField("Color", StringType(), True),
   StructField("Price", StringType(), True)])


# Spark dataframe created from original dataframe given the schema
df = spark.createDataFrame(df, schema1)

# Show initial dataframe
df.show()

# Function that inserts data in one function call
# To display.
"""
Parameters:
- args: The arguments to be inserted (an array of tuple(s))
- schema: The schema of the DataFrame
- df1: The dataframe to insert
- drop: Boolean option to drop the saved table or not
-- If the drop is set to True, then the file of the table will
-- be deleted. If not, it will be kept in the "testpysparktable"
-- directory.
"""
def easyInto(args, schema, df1, drop = True):
    print("\n***Inserting new data***\n")
    df2 = spark.createDataFrame(args, schema)
    df1.write.saveAsTable("testpysparktable")
    table = df2.write.insertInto("testpysparktable")
    spark.read.table("testpysparktable").show()
    if drop == True:
        spark.sql("DROP TABLE IF EXISTS testpysparktable")
    return table

# Insert new data
df_table = easyInto([("Daisy", "Notebook", "Green", "2.50")], schema1, df)

# Show new dataframe
df.show()

# Convert dataframe from SQL to Pandas, compute transpose
dfp = df.toPandas()
print("Transpose:")
dfp = dfp.T
print(dfp)


# Transpose Schema
schema1_T = StructType([
    StructField(x, StringType(), True) for x in dfp.iloc[0]
])

# Create Transposed dataframe in SQL form
dfp = spark.createDataFrame(dfp[1:], schema1_T)
dfp.show()

# Basic range test
df1 = spark.range(10)

df1.show()

# End session
spark.stop()



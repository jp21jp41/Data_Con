# Pyspark / Hadoop Distributed File System Test
The test is a simple demonstration of Pyspark and HDFS.

It demonstrates:
- Pyspark DataFrames with an SQL insertion as well as a manual Pandas transpose.
- A test of Hadoop through an InsecureClient, which has its status run to decide  whether it has to delete a specific directory or not.
- Shown DataFrames throughout the process.

Though Big Data Management is not truly demonstrated in the test, there is a heavy underlying focus on configuration management.

The environment variable home paths for Pyspark, Spark, Hadoop, and Java needed to be configured. These paths were not necessary in Python as the different applications could have been installed on the Path. The decision was ultimately to change environmental paths.
While the issue could have been intuitively understood with the Pyspark site, path configuration was made with the help of Google Gemini and Google AI Overview.

Pyspark was also not found to be compatible with Python 3.12.x, and converting it to a Python 3.11.x version was a necessary fix found through linking traceback to related StackOverFlow answers.

Hadoop had similar configuration management issues. Hadoop had to be installed and unzipped with the proper setup to its .xml files.
The fixes made to Hadoop could be completed using the Hadoop site alone, though the help of Google Gemini and StackOverFlow was used,  with the overall focus on the "Setting Up a Single Node Cluster" of the Apache Hadoop site, using the Pseudo-Distributed Operation.

Passphraseless SSH required installing Linux, which needed proper JAVA_HOME configuration to run, which was found through StackOverFlow.

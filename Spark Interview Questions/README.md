# Spark, PySpark Interview Question Series

**01. Explain PySpark?**

PySpark Features :
1. In-Memory computation
2. Lazy Evaluation
3. Fault tolerant
4. Immutability
5. Partitioning 
6. Persistence
7. Coarse Grained Operations

**PySpark** is a Python library used for processing large amounts of data in a distributed computing environment using Apache Spark.

**Apache Spark** is an open-source distributed computing framework that allows data processing across multiple machines in a cluster. It provides a unified interface for batch processing, streaming, machine learning, and graph processing. Spark is designed to be highly scalable and fault-tolerant, making it well suited for processing large datasets.

**02. What is lazy evaluation?**

**Lazy evaluation** in PySpark helps to optimize computation and minimize network communication overhead, which can significantly improve the performance of data processing applications.

**03. Stae the differences between PySpark and other languages?**

PySpark has inbuilt API, implicit communication can be done in PySpark

**04. What do you mean by SparkContext?**

**SparkContext** is the entry point for any PySpark program and is responsible for managing the connection to the cluster, setting configuration parameters, creating RDDs, and managing the execution of tasks across the cluster.

**05. Explain SparkConf and how does it work?**

**SparkConf** is a configuration object in PySpark that allows users to set various configuration properties for a PySpark application, which can then be passed to the SparkContext object to manage the execution of the application across the cluster.

**06. What is PySpark Partition?**

A partition in PySpark is a logical division of a large dataset into smaller, more manageable pieces. Partitions allow PySpark to process large datasets in parallel across a cluster of machines, by distributing the data across multiple nodes in the cluster.

PySpark provides several methods to control the partitioning of data, such as **repartition()** and **coalesce()**.

**07. What is RDD? How many types of RDDs are in the PySpark?**

**RDD (Resilient Distributed Dataset)** is the fundamental data structure in PySpark that represents an immutable, distributed collection of objects.

RDDs in PySpark are fault-tolerant, which means that they can recover from failures by recomputing lost data partitions.

RDDs also support lazy evaluation, which means that transformations on an RDD are not executed immediately, but are deferred until an action is called.

There are two types of RDDs in PySpark:
01. Parallelized Collections
02. HDFS Datasets

**08. Explain SparkSession in PySpark?**

**SparkSession** is a unified entry point to PySpark that provides a way to interact with various Spark functionality and features, such as Spark SQL, DataFrame API, and Dataset API. SparkSession is the primary object in PySpark that encapsulates a Spark cluster's resources and is responsible for coordinating the execution of Spark tasks across the cluster.

**SparkSession** in PySpark can be thought of as a combination of SparkContext, SQLContext, and HiveContext, which were used in previous versions of Spark. With SparkSession, developers no longer need to create these contexts separately, as SparkSession automatically creates and manages them under the hood.

**09. Explain How RDD is created in PySpark?**

01. Parallelizing an existing collection:

```python
from pyspark import SparkContext

sc = SparkContext("local", "myApp")
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
```

02. Loading data from a file or external storage system:

```python
from pyspark import SparkContext

sc = SparkContext("local", "myApp")
rdd = sc.textFile("mydata.txt")
```

03. Transformations on existing RDDs:

```python
from pyspark import SparkContext

sc = SparkContext("local", "myApp")
data = [1, 2, 3, 4, 5]
rdd1 = sc.parallelize(data)
rdd2 = rdd1.map(lambda x: x * 2)
```


### References 

1. https://www.youtube.com/watch?v=3XkwLXScXbk&ab_channel=MindMajix

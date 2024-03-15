import findspark

findspark.init()

import pyspark
from pyspark.sql import SparkSession
import pyodbc
import pandas as pd

spark = SparkSession.builder.appName("SSMS to PySpark").getOrCreate()


def connect_ssms():
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=105857-001L\SQLEXPRESS;"
                          "Database=Retail;"
                          "Trusted_Connection=yes;")
    return conn

def customers(conn):
    query = "SELECT * FROM customers"
    df_pandas_customers = pd.read_sql(query, conn)

    df_customers = spark.createDataFrame(df_pandas_customers)

    return df_customers

def order_items(conn):
    query = "SELECT * FROM order_items"
    df_pandas_order_items = pd.read_sql(query, conn)

    df_order_items = spark.createDataFrame(df_pandas_order_items)

    return df_order_items

def orders(conn):
    query = "SELECT * FROM orders"
    df_pandas_orders = pd.read_sql(query, conn)

    df_orders = spark.createDataFrame(df_pandas_orders)

    return df_orders

if __name__ == "__main__":
    conn = connect_ssms()

    df_customers = customers(conn)
    df_order_items = order_items(conn)
    df_orders = orders(conn)

    print(df_order_items.show(truncate=False))
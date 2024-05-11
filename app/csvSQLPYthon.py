import csv
import pandas as pandas
import sqlite3

df = pandas.read_csv(
    filepath_or_buffer = "/Users/andreabad/Desktop/Projects/backend-practice/app/data.csv",
    header = 0
)

print(df)

connection = sqlite3.connect("/Users/andreabad/Desktop/Projects/backend-practice/db/data.db")

df.to_sql(
    name = "data",
    con = connection, 
    if_exists = "replace",
    index = False,

)
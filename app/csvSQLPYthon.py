import csv
import pandas as pandas
import sqlite3
import os
import pathlib


csv_file = 'data.csv'

filepath = f"{os.path.dirname(__file__)}/{csv_file}"
 
print(filepath)

df = pandas.read_csv(
    filepath_or_buffer = filepath,
    header = 0
)

print(df)

db_location = f"{os.getcwd()}/db/data.db"
print(db_location)
connection = sqlite3.connect("/Users/andreabad/Desktop/Projects/backend-practice/db/data.db")

df.to_sql(
    name = "data",
    con = connection, 
    if_exists = "replace",
    index = False,
)
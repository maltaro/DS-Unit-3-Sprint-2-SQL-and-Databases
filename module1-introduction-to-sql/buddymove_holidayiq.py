import pandas as pd
import sqlite3


df = pd.read_csv("buddymove_holidayiq.csv")

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")

curs = conn.cursor()

df.to_sql("buddymove_holidayiq.sqlite3", con = sqlite3.Connection,
if_exists = "replace", index_label = "review")

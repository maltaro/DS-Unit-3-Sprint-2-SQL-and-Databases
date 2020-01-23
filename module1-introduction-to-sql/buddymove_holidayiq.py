import pandas as pd
import sqlite3


df = pd.read_csv("buddymove_holidayiq.csv")

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")

curs = conn.cursor()

df.to_sql('review', conn, if_exists = "replace")

conn.commit()

curs.close()

curs = conn.cursor()

# counting the rows in review:
query = "SELECT COUNT(*) from review;"
print(f"number of rows in review: {curs.execute(query).fetchall()[0][0]}")


# counting the number of users with nature > 100 and shopping > 100

query = """
SELECT Count(*)
FROM
(SELECT Nature, Shopping
FROM review
WHERE Nature > 100 AND Shopping > 100) AS MyTable
"""
print(f"number of users with nature>100 and shopping>100: {curs.execute(query).fetchall()[0][0]}")


# average reviews in Sports

query = "SELECT AVG(Sports) FROM review"
print(f"average number of reviews in Sports: {curs.execute(query).fetchall()[0][0]}")

# average reviews in Religious

query = "SELECT AVG(Religious) FROM review"
print(f"average number of reviews in Religious: {curs.execute(query).fetchall()[0][0]}")

# average reviews in Nature

query = "SELECT AVG(Nature) FROM review"
print(f"average number of reviews in Nature: {curs.execute(query).fetchall()[0][0]}")

# average reviews in Theatre

query = "SELECT AVG(Theatre) FROM review"
print(f"average number of reviews in Theatre: {curs.execute(query).fetchall()[0][0]}")

# average reviews in Shopping

query = "SELECT AVG(shopping) FROM review"
print(f"average number of reviews in Shopping: {curs.execute(query).fetchall()[0][0]}")

# average reviews in Picnic

query = "SELECT AVG(Picnic) FROM review"
print(f"average number of reviews in Picnic: {curs.execute(query).fetchall()[0][0]}")

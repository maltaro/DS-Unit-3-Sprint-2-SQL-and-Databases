import psycopg2
import pandas as pd

df = pd.read_csv("titanic.csv")

dbname = "zrhndczl"

user = "zrhndczl"

password = "TbAkv2zSBoZOljbfhcfERfy6XU7lLzBK"

host = "rajje.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()


create_titanic_table = """
CREATE TABLE titanic (
  passenger_id SERIAL PRIMARY KEY,
  Survived INT,
  Pclass INT,
  Name VARCHAR(80),
  Sex VARCHAR(30),
  Age INT,
  Siblings_or_Spouses_Aboard INT,
  Parents_or_Children_Aboard INT,
  Fare REAL
);
"""

pg_curs.execute(create_titanic_table)
pg_conn.commit()

passenger_list = []

for i in range(0,df.shape[0]):
    passenger_list.append(list(df.iloc[i][:]))

for passenger in passenger_list:
  insert_passenger = """
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_or_Spouses_Aboard, Parents_or_Children_Aboard, Fare)
    VALUES (""" + str(list(df.iloc[i][:]))[1:-1] + ");"
  pg_curs.execute(insert_passenger)
pg_conn.commit()

# something is not working. please refer to titanic_sailing.py for workig code.

import psycopg2
import pandas as pd

df = pd.read_csv("titanic.csv")

dbname = "zrhndczl"

user = "zrhndczl"

password = "TbAkv2zSBoZOljbfhcfERfy6XU7lLzBK"

host = "rajje.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()


import sqlalchemy  # Package for accessing SQL databases via Python

# Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
engine = sqlalchemy.create_engine("postgres://zrhndczl:TbAkv2zSBoZOljbfhcfERfy6XU7lLzBK@rajje.db.elephantsql.com:5432/zrhndczl")
con = engine.connect()

# Verify that there are no existing tables
print(engine.table_names())


table_name = 'titanic'
df.to_sql(table_name, con)

print(engine.table_names())

con.close()

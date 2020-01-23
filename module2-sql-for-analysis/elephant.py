import psycopg2


dbname = "zrhndczl"

user = "zrhndczl"

password = "TbAkv2zSBoZOljbfhcfERfy6XU7lLzBK"

host = "rajje.db.elephantsql.com"

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)


print(type(pg_conn))


pg_curs = pg_conn.cursor()


create_table_statement = """
CREATE TABLE test_table (
  id        SERIAL PRIMARY KEY,
  name  varchar(40) NOT NULL,
  data    JSONB
);
"""

insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""

pg_curs.execute(create_table_statement)
pg_curs.execute(insert_statement)

pg_conn.commit()

query= "SELECT * FROM test_table;"
pg_curs.execute(query)
print(pg_curs.fetchall())


import sqlite3

sl_conn  = sqlite3.connect(r'C:\Users\UX490\Desktop\LambdaForks\DS-Unit-3-Sprint-2-SQL-and-Databases\module1-introduction-to-sql\rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# We care about charactercreator_character table
row_count = 'SELECT COUNT(*) FROM charactercreator_character'
print(sl_curs.execute(row_count).fetchall()[0][0])

# Our goal - copy the characters table from SQLite to PostgreSQL using Python
# Step 1 - E=Extract: Get the Characters
get_characters = 'SELECT * FROM charactercreator_character'
characters = sl_curs.execute(get_characters).fetchall()


create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""
pg_curs.execute(create_character_table)
pg_conn.commit()


# looping over every character from rpg_db.sqlite3 to transform it so that
# the format fits to charactercreator_character. By doing that the table can be
# inserted into PostgreSQL
for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)
pg_conn.commit()


# A quick test that we did this correctly
pg_curs.execute('SELECT * FROM charactercreator_character')
pg_characters = pg_curs.fetchall()
for character, pg_character in zip(characters, pg_characters):
  assert character == pg_character

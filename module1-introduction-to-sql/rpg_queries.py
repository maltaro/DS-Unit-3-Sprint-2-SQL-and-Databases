import sqlite3

conn = sqlite3.connect("rpg_db.sqlite3")

curs = conn.cursor()


# Counting how many characters exist

query = "SELECT COUNT(*) FROM charactercreator_character;"
print(f"amount of total characters: {curs.execute(query).fetchall()[0][0]}")

# counting clerics

query = "SELECT COUNT(*) FROM charactercreator_cleric;"
print(f"amount of clerics: {curs.execute(query).fetchall()[0][0]}")


# counting fighter

query = "SELECT COUNT(*) FROM charactercreator_fighter;"
print(f"amount of fighters: {curs.execute(query).fetchall()[0][0]}")

# counting mage

query = "SELECT COUNT(*) FROM charactercreator_mage;"
print(f"amount of mages: {curs.execute(query).fetchall()[0][0]}")


# counting necromancer

query = "SELECT COUNT(*) FROM charactercreator_necromancer;"
print(f"amount of necromancers: {curs.execute(query).fetchall()[0][0]}")

# counting  thief

query = "SELECT COUNT(*) FROM charactercreator_thief;"
print(f"amount of thieves: {curs.execute(query).fetchall()[0][0]}")

# counting items
query = "SELECT COUNT(*) FROM armory_item;"
print(f"amount of items: {curs.execute(query).fetchall()[0][0]}")


# counting weapons

query = "SELECT COUNT(*) FROM armory_weapon;"
print(f"amount of weapons: {curs.execute(query).fetchall()[0][0]}")

# counting non-wepaons

print(f"amount of non-weapons: {174 - curs.execute(query).fetchall()[0][0]}")

query = """
SELECT COUNT(DISTINCT item_id) FROM armory_item
WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)
"""
 print(f"amount of non-weapons: {curs.execute(query).fetchall()[0][0]}")

# counting items per character

query = """
SELECT character_id, COUNT (item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""
print("amount of items per character_id, first 20 rows")
print(f"{curs.execute(query).fetchall()}")


# counting weapons per character

query = """
SELECT character_id, COUNT (item_id)
FROM charactercreator_character_inventory as character, armory_weapon as armory
WHERE character.item_id = armory.item_ptr_id
GROUP BY character_id
LIMIT 20;
"""
print("amount of weapons per chacter_id, first 20 rows")
print(f"{curs.execute(query).fetchall()}")

# counting the average amount of items per characters
# (of characters that have at least one item)

query = """
SELECT AVG(number_of_items)
FROM
(SELECT character_id, COUNT (item_id) AS number_of_items
FROM charactercreator_character_inventory
GROUP BY character_id) AS MyTable
"""

print("average items per character")
print(f"{curs.execute(query).fetchall()[0][0]}")


# average weapons per character
# of charcters that have at least one wepaon

query = """
SELECT AVG(number_of_weapons)
FROM
(
SELECT character_id, COUNT (item_id) as number_of_weapons
FROM charactercreator_character_inventory as character, armory_weapon as armory
WHERE character.item_id = armory.item_ptr_id
GROUP BY character_id)
"""

print("average weapons per character")
print(f"{curs.execute(query).fetchall()[0][0]}")

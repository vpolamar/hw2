import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Laptop')")
cursor.execute("insert into list (description) values ('Mobile')")
cursor.execute("insert into list (description) values ('Monitor')")
cursor.execute("insert into list (description) values ('Chair')")
cursor.execute("insert into list (description) values ('Headphones')")

connection.commit()
connection.close()

print("Database shopping_list is created and some sample data is inserted successfully.")

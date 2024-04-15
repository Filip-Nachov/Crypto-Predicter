import sqlite3


# Connecting to a database
con = sqlite3.connect("database.db")
# creating a cursor object
cur = con.cursor()

# making the data base
cur.execute("CREATE TABLE IF NOT EXISTS users(email TEXT, password TEXT)")

# close the database
cur.close()
con.close()

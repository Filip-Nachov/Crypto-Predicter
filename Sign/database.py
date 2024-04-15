import sqlite3


# Connecting to a database
con = sqlite3.connect("database.db")
#creating a cursor object
cur = con.cursor()

#defing the database values
cur.execute('SELECT * FROM users')

#close the database
cur.close()
con.close

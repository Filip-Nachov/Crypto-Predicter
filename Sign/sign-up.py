from flask import Flask
import sqlite3

# connecting to a database 
con = sqlite3.connect("database.db")
# making a cursor object
cur = con.cursor()
 
# making the data base
cur.execute("CREATE TABLE IF NOT EXISTS users(email TEXT, password TEXT)")

app = Flask(__name__)

def register():
    ...

def login():
    ...





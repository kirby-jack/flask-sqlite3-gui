import sqlite3

# SQLITE3 CONFIGUARTIONS
# Connect to db
con = sqlite3.connect("database.db", check_same_thread=False)

# Create database cursor 
cur = con.cursor()

# Enable row_factory (for using SQL Queries as dicts) see documentation https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
con.row_factory = dict_factory

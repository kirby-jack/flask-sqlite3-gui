import os
import sqlite3

# Calculate the base directory of your project (adjust if necessary)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, "database.db")  # Adjust "database.db" to your filename

# Connect to db
con = sqlite3.connect(db_path, check_same_thread=False)

# Enable row_factory before creating the cursor
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
con.row_factory = dict_factory

# Create database cursor 
cur = con.cursor()

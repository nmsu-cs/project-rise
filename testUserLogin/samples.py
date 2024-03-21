import sqlite3
import os.path

# Check if the database file exists
if not os.path.isfile('userdata.db'):
    # If the file doesn't exist, create a new database
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE userdata (
            id INTEGER PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(64) NOT NULL
        )
    """)
    conn.commit()
    conn.close()
else:
    # If the file exists, check if the table exists
    conn = sqlite3.connect('userdata.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='userdata'")
    table_exists = cur.fetchone()
    if not table_exists:
        # If the table doesn't exist, create it
        cur.execute("""
            CREATE TABLE userdata (
                id INTEGER PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(64) NOT NULL
            )
        """)
        conn.commit()
    conn.close()
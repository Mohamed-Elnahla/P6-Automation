"""
Utility for database connection and queries.
"""
import sqlite3

def connect_to_db(db_path):
    try:
        conn = sqlite3.connect(db_path)
        print("Database connection established.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

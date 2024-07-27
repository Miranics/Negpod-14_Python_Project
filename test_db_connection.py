#!/usr/bin/python3
# test_db_connection.py
import mysql.connector

def test_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',        # Use 'localhost' if MySQL is on the same machine
            user='root',             # Default MySQL root user
            password='',             # Default password for root user (usually empty by default)
            database='restaurant'    # Ensure this matches your database name
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful")
            connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    test_connection()


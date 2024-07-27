#!/usr/bin/python3
# test_db_connection.py
import mysql.connector

def test_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='miracity',  # Use the new password you set
            database='restaurant'
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful")
            connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    test_connection()



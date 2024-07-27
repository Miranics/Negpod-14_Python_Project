import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='miracity',  # Ensure this matches your MySQL password
        database='restaurant'
    )
    if connection.is_connected():
        print("Connection successful")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        connection.close()

import mysql.connector
from db_config import get_db_connection

def display_menu(lang):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, price FROM menu")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    print(lang['menu'])
    for row in rows:
        print(f"{row[0]}. {row[1]} - ${row[2]:.2f}")

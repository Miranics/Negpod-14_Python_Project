#!/usr/bin/python3
import mysql.connector
from db_config import get_db_connection

def display_menu(lang):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM menu")
    menu_items = cursor.fetchall()

    print("\n" + lang['menu_header'])
    for item in menu_items:
        print(f"{item[0]}. {item[1]} - {item[2]:.2f}")

    cursor.close()
    connection.close()

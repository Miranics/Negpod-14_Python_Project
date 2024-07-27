#!/usr/bin/python3
# menu.py
from db_config import get_db_connection


def display_menu():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, price FROM menu")
    menu_items = cursor.fetchall()

    print("\nMenu:")
    for item in menu_items:
        print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]:.2f} RWF")

    cursor.close()
    connection.close()

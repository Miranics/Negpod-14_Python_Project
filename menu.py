#!/usr/bin/env python3
# menu.py

from db_config import get_db_connection

def display_menu(lang):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    print("-----------------------------")
    print(lang['menu_title'])
    print("-----------------------------")
    for idx, item in enumerate(items, start=1):
        print(f"{idx}. {item[1]} - RWF {item[2]:.2f}")
    cursor.close()
    connection.close()
    print("-----------------------------")

#!/usr/bin/python3
from contextlib import closing
from db_config import get_db_connection

def display_menu():
    with closing(get_db_connection()) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT id, name, price FROM menu")
            menu_items = cursor.fetchall()
            print("\nMenu:")
            for item in menu_items:
                print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]:.2f} RWF")

def search_menu(query):
    with closing(get_db_connection()) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT id, name, price FROM menu WHERE name LIKE %s", ('%' + query + '%',))
            search_results = cursor.fetchall()
            print("\nSearch Results:")
            for item in search_results:
                print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]:.2f} RWF")

#!/usr/bin/python3
import mysql.connector
from db_config import get_db_connection


def place_order(order, lang):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM menu")
    menu_items = cursor.fetchall()

    print("\n" + lang['menu_header'])
    for item in menu_items:
        print(f"{item[0]}. {item[1]} - {item[2]:.2f}")

    while True:
        try:
            item_id = int(input(lang['enter_item_id']))
            quantity = int(input(lang['enter_quantity']))

            cursor.execute("SELECT price FROM menu WHERE id = %s", (item_id,))
            price = cursor.fetchone()

            if price is None:
                print(lang['item_not_found'])
                continue

            total_price = price[0] * quantity
            order.append((item_id, quantity, total_price))
            print(lang['order_added'])
            break
        except ValueError:
            print(lang['invalid_input'])

    cursor.close()
    connection.close()


def review_order(order, lang):
    if not order:
        print(lang['order_empty'])
        return

    print("\n" + lang['order_review'])
    total = 0
    for item in order:
        print(f"Item ID: {item[0]}, Quantity: {item[1]}, Total Price: {item[2]:.2f}")
        total += item[2]
    print(f"Total: {total:.2f}")

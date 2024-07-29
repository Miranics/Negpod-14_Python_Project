#!/usr/bin/env python3
import mysql.connector
from db_config import get_db_connection

def place_order(order, lang):
    while True:
        try:
            item_id = int(input(lang['enter_item_id']))
            quantity = int(input(lang['enter_quantity']))
            order.append((item_id, quantity))
            print(lang['order_added'])
        except ValueError:
            print(lang['invalid_input'])
        more_items = input(lang['add_more_items'])
        if more_items.lower() != 'y':
            break

def review_order(order, lang):
    if not order:
        print(lang['order_empty'])
        return

    print(lang['order_review'])
    total = 0
    for item_id, quantity in order:
        # Fetch item details from the menu table
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name, price FROM menu WHERE id = %s", (item_id,))
        item = cursor.fetchone()
        cursor.close()
        connection.close()

        if item:
            name, price = item
            total_price = price * quantity
            total += total_price
            print(f"{name} (x{quantity}): RWFotal_price:.2f}")

    print(f"Total: RWFotal:.2f}")

def update_order(order, lang):
    try:
        item_id = int(input(lang['enter_item_id_to_update']))
        for i, (id, qty) in enumerate(order):
            if id == item_id:
                new_quantity = int(input(lang['enter_new_quantity']))
                order[i] = (item_id, new_quantity)
                print(lang['order_updated'])
                return
        print(lang['item_not_found'])
    except ValueError:
        print(lang['invalid_input'])

def remove_order(order, lang):
    try:
        item_id = int(input(lang['enter_item_id_to_remove']))
        for i, (id, qty) in enumerate(order):
            if id == item_id:
                del order[i]
                print(lang['order_removed'])
                return
        print(lang['item_not_found'])
    except ValueError:
        print(lang['invalid_input'])

def save_order_to_db(order, lang):
    connection = get_db_connection()
    cursor = connection.cursor()
    for item_id, quantity in order:
        # Fetch item price from the menu table
        cursor.execute("SELECT price FROM menu WHERE id = %s", (item_id,))
        price = cursor.fetchone()[0]
        total_price = price * quantity
        cursor.execute(
            "INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)",
            (item_id, quantity, total_price)
        )
    connection.commit()
    cursor.close()
    connection.close()
    print(lang['order_saved'])

def give_feedback(lang):
    name = input(lang['enter_name'])
    comments = input(lang['enter_comments'])
    try:
        rating = int(input(lang['enter_rating']))
        if rating < 1 or rating > 5:
            raise ValueError(lang['invalid_input'])
    except ValueError:
        print(lang['invalid_input'])
        return

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO feedback (customer_name, comments, rating) VALUES (%s, %s, %s)",
        (name, comments, rating)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print(lang['feedback_thank_you'])

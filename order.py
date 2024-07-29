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


def update_order(order, lang):
    if not order:
        print(lang['order_empty'])
        return

    item_id = int(input(lang['enter_item_id_to_update']))
    for i, item in enumerate(order):
        if item[0] == item_id:
            new_quantity = int(input(lang['enter_new_quantity']))
            new_total_price = item[2] / item[1] * new_quantity
            order[i] = (item_id, new_quantity, new_total_price)
            print(lang['order_updated'])
            return

    print(lang['item_not_found'])


def remove_order(order, lang):
    if not order:
        print(lang['order_empty'])
        return

    item_id = int(input(lang['enter_item_id_to_remove']))
    for i, item in enumerate(order):
        if item[0] == item_id:
            del order[i]
            print(lang['order_removed'])
            return

    print(lang['item_not_found'])


def save_order_to_db(order, lang):
    if not order:
        print(lang['order_empty'])
        return

    connection = get_db_connection()
    cursor = connection.cursor()

    for item in order:
        cursor.execute(
            "INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)",
            (item[0], item[1], item[2])
        )

    connection.commit()
    cursor.close()
    connection.close()
    print(lang['order_saved'])


def give_feedback(lang):
    connection = get_db_connection()
    cursor = connection.cursor()

    customer_name = input(lang['enter_name'])
    comments = input(lang['enter_comments'])
    while True:
        try:
            rating = int(input(lang['enter_rating']))
            if 1 <= rating <= 5:
                break
            else:
                print(lang['invalid_input'])
        except ValueError:
            print(lang['invalid_input'])

    cursor.execute(
        "INSERT INTO feedback (customer_name, comments, rating) VALUES (%s, %s, %s)",
        (customer_name, comments, rating)
    )

    connection.commit()
    cursor.close()
    connection.close()
    print(lang['feedback_thank_you'])

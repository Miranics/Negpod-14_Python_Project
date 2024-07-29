#!/usr/bin/env python3
# order.py

from db_config import get_db_connection

def place_order(order, lang):
    connection = get_db_connection()
    cursor = connection.cursor()
    while True:
        display_menu(lang)
        item_id = input(lang['enter_item_id'])
        quantity = input(lang['enter_quantity'])
        cursor.execute("SELECT price FROM menu WHERE id = %s", (item_id,))
        price = cursor.fetchone()
        if price:
            total_price = price[0] * int(quantity)
            order.append((item_id, quantity, total_price))
            print(f"{lang['item_added']} - RWF {total_price:.2f}")
        else:
            print(lang['invalid_item'])
        more_items = input(lang['add_more_items'])
        if more_items.lower() != 'y':
            break
    cursor.close()
    connection.close()

def review_order(order, lang):
    if not order:
        print(lang['no_items_ordered'])
        return
    print("-----------------------------")
    print(lang['order_review'])
    print("-----------------------------")
    total = 0
    for item in order:
        total += item[2]
        print(f"Item ID: {item[0]}, Quantity: {item[1]}, Total Price: RWF {item[2]:.2f}")
    print("-----------------------------")
    print(f"Total: RWF {total:.2f}")
    print("-----------------------------")

def save_order_to_db(order, lang):
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

def update_order(order, lang):
    item_id = int(input(lang['enter_item_id_to_update']))
    for i, item in enumerate(order):
        if item[0] == item_id:
            new_quantity = int(input(lang['enter_new_quantity']))
            order[i] = (item_id, new_quantity, item[2] / item[1] * new_quantity)
            print(lang['order_updated'])
            return
    print(lang['item_not_found'])

def remove_order(order, lang):
    item_id = int(input(lang['enter_item_id_to_remove']))
    for i, item in enumerate(order):
        if item[0] == item_id:
            order.pop(i)
            print(lang['item_removed'])
            return
    print(lang['item_not_found'])

def give_feedback(lang):
    connection = get_db_connection()
    cursor = connection.cursor()
    name = input(lang['enter_your_name'])
    comments = input(lang['feedback_prompt'])
    rating = int(input(lang['enter_rating']))
    cursor.execute(
        "INSERT INTO feedback (customer_name, comments, rating) VALUES (%s, %s, %s)",
        (name, comments, rating)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print(lang['thank_you_feedback'])

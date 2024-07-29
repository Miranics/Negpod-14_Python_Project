#!/usr/bin/python3
from db_config import get_db_connection


def place_order(order, lang):
    item_id = input(lang['enter_item_id'])
    quantity = input(lang['enter_quantity'])

    try:
        item_id = int(item_id)
        quantity = int(quantity)
    except ValueError:
        print(lang['invalid_choice'])
        return

    order.append({'item_id': item_id, 'quantity': quantity})
    print(lang['order_updated'])


def review_order(order, lang):
    if not order:
        print(lang['order_empty'])
        return

    total_price = 0
    for item in order:
        print(f"Item ID: {item['item_id']}, Quantity: {item['quantity']}")
        total_price += item['quantity'] * get_item_price(item['item_id'])

    print(f"Total Price: {total_price}")


def update_order(order, lang):
    item_id = input(lang['enter_item_id'])
    try:
        item_id = int(item_id)
    except ValueError:
        print(lang['invalid_choice'])
        return

    for item in order:
        if item['item_id'] == item_id:
            new_quantity = input(lang['enter_new_quantity'])
            try:
                new_quantity = int(new_quantity)
            except ValueError:
                print(lang['invalid_choice'])
                return

            item['quantity'] = new_quantity
            print(lang['order_updated'])
            return

    print(lang['item_not_found'])


def remove_order(order, lang):
    item_id = input(lang['enter_item_id'])
    try:
        item_id = int(item_id)
    except ValueError:
        print(lang['invalid_choice'])
        return

    for item in order:
        if item['item_id'] == item_id:
            order.remove(item)
            print(lang['order_removed'])
            return

    print(lang['item_not_found'])


def save_order_to_db(order, lang):
    connection = get_db_connection()
    cursor = connection.cursor()

    for item in order:
        total_price = item['quantity'] * get_item_price(item['item_id'])
        cursor.execute(
            "INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)",
            (item['item_id'], item['quantity'], total_price)
        )

    connection.commit()
    cursor.close()
    connection.close()
    print(lang['order_saved'])


def give_feedback(lang):
    connection = get_db_connection()
    cursor = connection.cursor()

    print(lang['give_feedback_prompt'])
    customer_name = input(lang['enter_name'])
    comments = input(lang['enter_comments'])
    rating = input(lang['enter_rating'])

    try:
        rating = int(rating)
        if rating < 1 or rating > 5:
            raise ValueError
    except ValueError:
        print(lang['invalid_choice'])
        return

    cursor.execute(
        "INSERT INTO feedback (customer_name, comments, rating) VALUES (%s, %s, %s)",
        (customer_name, comments, rating)
    )

    connection.commit()
    cursor.close()
    connection.close()
    print(lang['feedback_thank_you'])


def get_item_price(item_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT price FROM menu WHERE id = %s", (item_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result[0] if result else 0

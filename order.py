#!/usr/bin/python3
# order.py
from db_config import get_db_connection


def place_order(order):
    connection = get_db_connection()
    cursor = connection.cursor()

    item_id = int(input("Enter the menu item ID: "))
    quantity = int(input("Enter the quantity: "))

    cursor.execute("INSERT INTO orders (item_id, quantity) VALUES (%s, %s)", (item_id, quantity))
    connection.commit()

    cursor.close()
    connection.close()

    order.append((item_id, quantity))
    print("Order placed successfully!")


def review_order(order):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT o.id, m.name, o.quantity, m.price FROM orders o JOIN menu m ON o.item_id = m.id")
    orders = cursor.fetchall()

    print("\nYour Order:")
    total = 0
    for order in orders:
        order_id, name, quantity, price = order
        total_price = quantity * price
        total += total_price
        print(f"Order ID: {order_id}, Item: {name}, Quantity: {quantity}, Total Price: {total_price:.2f}")

    print(f"\nTotal Amount Due: {total:.2f}")

    cursor.close()
    connection.close()


def update_order(order):
    review_order(order)
    item_num = int(input("Enter the order ID to update quantity: "))
    new_quantity = int(input("Enter the new quantity: "))

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("UPDATE orders SET quantity = %s WHERE id = %s", (new_quantity, item_num))
    connection.commit()

    cursor.close()
    connection.close()

    print("Order updated successfully!")


def remove_from_order(order):
    review_order(order)
    item_num = int(input("Enter the order ID to remove: "))

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM orders WHERE id = %s", (item_num,))
    connection.commit()

    cursor.close()
    connection.close()

    print("Order removed successfully!")

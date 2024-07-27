#!/usr/bin/python3
# order.py
from menu import display_menu, menu
from db_config import get_db_connection

def place_order(order):
    while True:
        display_menu()
        try:
            item_id = int(input("Enter the item number to order (0 to finish): "))
            if item_id == 0:
                break
            if item_id < 1 or item_id > len(menu):
                print("Invalid item number. Please try again.")
                continue

            quantity = int(input("Enter the quantity: "))
            if quantity < 1:
                print("Quantity must be at least 1. Please try again.")
                continue

            selected_item = menu[item_id - 1]
            total_price = selected_item['price'] * quantity
            order.append({"item_id": item_id, "quantity": quantity, "total_price": total_price})
            print(f"Added {quantity} x {selected_item['name']} to order. Total price: {total_price} RWF")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def review_order(order):
    if not order:
        print("No items in order.")
    else:
        print("Your order:")
        for item in order:
            selected_item = menu[item['item_id'] - 1]
            print(f"{item['quantity']} x {selected_item['name']} - {item['total_price']} RWF")

def save_order_to_db(order):
    connection = get_db_connection()
    cursor = connection.cursor()

    for item in order:
        cursor.execute(
            "INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)",
            (item['item_id'], item['quantity'], item['total_price'])
        )

    connection.commit()
    cursor.close()
    connection.close()
    print("Order has been saved to the database.")


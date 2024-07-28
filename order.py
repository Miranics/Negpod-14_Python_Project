#!/usr/bin/python3
from db_config import get_db_connection
from menu import display_menu, menu

def place_order(order):
    display_menu()
    while True:
        try:
            item_number = int(input("Enter the item number to order (or 0 to finish): "))
            if item_number == 0:
                break
            if item_number < 1 or item_number > len(menu):
                print("Invalid item number. Please try again.")
                continue
            quantity = int(input("Enter the quantity: "))
            item = menu[item_number - 1]
            order.append({
                "id": item_number,
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity
            })
            print(f"Added {quantity} x {item['name']} to your order.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def review_order(order):
    if not order:
        print("No items in your order.")
        return
    total = 0
    print("\nYour Order:")
    for item in order:
        print(f"{item['quantity']} x {item['name']} @ {item['price']} RWF each")
        total += item['price'] * item['quantity']
    print(f"Total: {total} RWF\n")

def update_order(order):
    if not order:
        print("No items in your order to update.")
        return
    review_order(order)
    try:
        item_number = int(input("Enter the item number to update: "))
        for item in order:
            if item['id'] == item_number:
                new_quantity = int(input(f"Enter the new quantity for {item['name']}: "))
                item['quantity'] = new_quantity
                print(f"Updated {item['name']} to {new_quantity} quantity.")
                return
        print("Item not found in your order.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def remove_order(order):
    if not order:
        print("No items in your order to remove.")
        return
    review_order(order)
    try:
        item_number = int(input("Enter the item number to remove: "))
        for item in order:
            if item['id'] == item_number:
                order.remove(item)
                print(f"Removed {item['name']} from your order.")
                return
        print("Item not found in your order.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def save_order_to_db(order):
    if not order:
        print("No items in your order to save.")
        return

    connection = get_db_connection()
    cursor = connection.cursor()

    for item in order:
        cursor.execute(
            "INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)",
            (item['id'], item['quantity'], item['price'] * item['quantity'])
        )

    connection.commit()
    cursor.close()
    connection.close()
    print("Order saved to database.")

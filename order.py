#!/usr/bin/python3
from menu import menu
from db_config import get_db_connection

def display_menu():
    print("Menu")
    for index, item in enumerate(menu, start=1):
        print(f"{index} {item['name']}: {item['price']} RWF")

def place_order(order, lang):
    display_menu()
    while True:
        try:
            item_id = int(input("Enter the item ID to order (0 to finish): "))
            if item_id == 0:
                break
            quantity = int(input("Enter the quantity: "))
            item = menu[item_id - 1]
            total_price = item['price'] * quantity
            order.append({
                "id": item_id,
                "name": item['name'],
                "quantity": quantity,
                "total_price": total_price
            })
            print(f"Added {quantity} x {item['name']} to your order.")
        except (ValueError, IndexError):
            print(lang['invalid_input'])
    review_order(order, lang)

def review_order(order, lang):
    print("Your current order:")
    total = 0
    for item in order:
        print(f"{item['name']} x{item['quantity']} = {item['total_price']} RWF")
        total += item['total_price']
    print(f"Total: {total} RWF")

def update_order(order, lang):
    review_order(order, lang)
    try:
        item_id = int(input("Enter the item ID to update: "))
        for item in order:
            if item['id'] == item_id:
                new_quantity = int(input("Enter the new quantity: "))
                item['quantity'] = new_quantity
                item['total_price'] = menu[item_id - 1]['price'] * new_quantity
                print(f"Updated {item['name']} to {new_quantity} x {item['name']}.")
                return
        print(lang['item_not_found'])
    except ValueError:
        print(lang['invalid_input'])

def remove_order(order, lang):
    review_order(order, lang)
    try:
        item_id = int(input("Enter the item ID to remove: "))
        for item in order:
            if item['id'] == item_id:
                order.remove(item)
                print(f"Removed {item['name']} from your order.")
                return
        print(lang['item_not_found'])
    except ValueError:
        print(lang['invalid_input'])

def save_order_to_db(order, lang):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        for item in order:
            cursor.execute(
                "INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)",
                (item['id'], item['quantity'], item['total_price'])
            )
        connection.commit()
        print(lang['order_saved'])
    except Exception as e:
        connection.rollback()
        print(f"{lang['save_error']}: {e}")
    finally:
        cursor.close()
        connection.close()

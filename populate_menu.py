#!/usr/bin/env python3
from db_config import get_db_connection


def populate_menu():
    menu_items = [
        {"name": "Margherita Pizza", "price": 12000},
        {"name": "Pepperoni Pizza", "price": 12000},
        {"name": "BBQ Chicken Pizza", "price": 13000},
        {"name": "Hawaiian Pizza", "price": 13500},
        {"name": "Veggies Pizza", "price": 11000},
        {"name": "Burger", "price": 6500},
        {"name": "Pasta", "price": 7000},
        {"name": "Salad", "price": 8500},
        {"name": "Soda", "price": 2000},
        {"name": "Fries", "price": 3000},
        {"name": "Steak", "price": 15000},
        {"name": "Ice Cream", "price": 4000},
        {"name": "Sandwich", "price": 6000},
        {"name": "Coffee", "price": 2500},
        {"name": "Latte Coffee", "price": 3500},
        {"name": "Tea", "price": 2000},
        {"name": "Drinking water", "price": 1000},
        {"name": "Fresh Juice", "price": 2000},
        {"name": "Soup", "price": 5000},
        {"name": "Chicken Wings", "price": 9000},
        {"name": "Fish and Chips", "price": 10000},
        {"name": "Smoothie", "price": 3500}
    ]

    conn = get_db_connection()
    cursor = conn.cursor()

    # Clear the menu table
    cursor.execute("TRUNCATE TABLE menu")
    conn.commit()

    # Insert menu items
    for item in menu_items:
        cursor.execute("INSERT INTO menu (name, price) VALUES (%s, %s)", (item['name'], item['price']))

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    populate_menu()

#!/usr/bin/python3
import mysql.connector
from db_config import get_db_connection

# Existing imports and functions...

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

def remove_order(order, lang):
    while True:
        try:
            item_id = int(input(lang['enter_item_id_to_remove']))
            found = False
            for i, (id, qty) in enumerate(order):
                if id == item_id:
                    del order[i]
                    found = True
                    print(lang['order_removed'])
                    break
            if not found:
                print(lang['item_not_found'])
        except ValueError:
            print(lang['invalid_input'])
        more_items = input(lang['add_more_items'])
        if more_items.lower() != 'y':
            break

# Existing functions...

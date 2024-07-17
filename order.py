# order.py

from menu import menu, display_menu

def place_order(order):
    while True:
        display_menu()
        choice = input("Enter the number of the item you'd like to order (1-5), or 'done' to finish: ")
        if choice.lower() == 'done':
            break
        elif choice.isdigit() and 1 <= int(choice) <= 22:
            index = int(choice) - 1
            order.append(menu[index]['name'])
            print(f"{menu[index]['name']} added to your order.")
        else:
            print("Invalid choice. Please enter a number from 1 to 5 or 'done'.")

def review_order(order):
    if not order:
        print("Your order is empty.")
    else:
        print("Your current order:")
        total = 0
        for item in order:
            # Find the item index in the menu list
            item_index = next((index for index, menu_item in enumerate(menu) if menu_item['name'] == item), None)
            if item_index is not None:
                print(f"- {item}: {menu[item_index]['price']} RWF")
                total += menu[item_index]['price']
            else:
                print(f"- {item}: Item not found in the menu.")
        print(f"Total: {total} RWF")
#!/usr/bin/python3
# main.py
from order import place_order, review_order, save_order_to_db, update_order, remove_order

def main():
    print("\n-----------------------------"
          "\n..Welcome To N14 Restaurant.."
          "\n-----------------------------")
    order = []
    while True:
        print("Main Menu:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Review Order")
        print("4. Update Order")
        print("5. Remove Order")
        print("6. Save Order")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            from menu import display_menu
            display_menu()
        elif choice == '2':
            place_order(order)
        elif choice == '3':
            review_order(order)
        elif choice == '4':
            update_order(order)
        elif choice == '5':
            remove_order(order)
        elif choice == '6':
            save_order_to_db(order)
        elif choice == '7':
            print("----Thanks for choosing our Restaurant, visit again----")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()

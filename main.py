#!/usr/bin/python3
from order import place_order, review_order, update_order, remove_from_order
from menu import display_menu, search_menu

def main():
    print("\n-----------------------------"
          "\n..Welcome To N14 Restaurant.."
          "\n-----------------------------")

    order = []
    while True:
        print("\nMain Menu:")
        print("1. View Menu")
        print("2. Search Menu")
        print("3. Place Order")
        print("4. Review Order")
        print("5. Update Order")
        print("6. Remove Item from Order")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            try:
                display_menu()
            except Exception as e:
                print(f"An error occurred while displaying the menu: {e}")
        elif choice == '2':
            query = input("Enter the item name to search: ")
            try:
                search_menu(query)
            except Exception as e:
                print(f"An error occurred while searching the menu: {e}")
        elif choice == '3':
            try:
                place_order(order)
            except Exception as e:
                print(f"An error occurred while placing the order: {e}")
        elif choice == '4':
            try:
                review_order(order)
            except Exception as e:
                print(f"An error occurred while reviewing the order: {e}")
        elif choice == '5':
            try:
                update_order(order)
            except Exception as e:
                print(f"An error occurred while updating the order: {e}")
        elif choice == '6':
            try:
                remove_from_order(order)
            except Exception as e:
                print(f"An error occurred while removing the order: {e}")
        elif choice == '7':
            print("----Thanks for choosing our Restaurant, visit again----")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()

#!/usr/bin/python3
from order import place_order, review_order, update_order, remove_order, save_order_to_db

def main():
    print("\n" + "=" * 60)
    print(" Welcome to N14 Restaurant! ".center(60, "*"))
    print("=" * 60)
    print("\nWe are delighted to have you here. Enjoy our delicious menu!")
    print("------------------------------------------------------------\n")
    order = []
    while True:
        print("Main Menu:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Review Order")
        print("4. Update Order")
        print("5. Remove Order")
        print("6. Confirm and Save Order")
        print("7. Exit Application")
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

# main.py

from order import place_order, review_order

def main():
    
    print("-..--..Welcome To N14 Restaurant..--..-")
    order = []
    while True:
        print("Main Menu:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Review Order")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            from menu import display_menu
            display_menu()
        elif choice == '2':
            place_order(order)
        elif choice == '3':
            review_order(order)
        elif choice == '4':
            print("----Thanks for choosing our Restaurant, pls visit again----")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 15.")

if __name__ == "__main__":
    main()

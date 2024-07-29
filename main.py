#!/usr/bin/python3
from order import place_order, review_order, update_order, remove_order, save_order_to_db, give_feedback
from language_loader import load_language

def main():
    lang = load_language()

    print("\n-----------------------------")
    print(lang['welcome_message_1'])
    print(lang['welcome_message_2'])
    print("-----------------------------")
    order = []
    while True:
        print(lang['main_menu'])
        print(lang['view_menu'])
        print(lang['place_order'])
        print(lang['review_order'])
        print(lang['update_order'])
        print(lang['remove_order'])
        print(lang['save_order'])
        print(lang['give_feedback'])
        print(lang['exit'])
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            from menu import display_menu
            display_menu()
        elif choice == '2':
            place_order(order, lang)
        elif choice == '3':
            review_order(order, lang)
        elif choice == '4':
            update_order(order, lang)
        elif choice == '5':
            remove_order(order, lang)
        elif choice == '6':
            save_order_to_db(order, lang)
        elif choice == '7':
            give_feedback(lang)
        elif choice == '8':
            print(lang['goodbye_message'])
            break
        else:
            print(lang['invalid_choice'])

if __name__ == "__main__":
    main()

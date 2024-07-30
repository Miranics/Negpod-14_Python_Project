#!/usr/bin/env python3
# main.py

from language_loader import load_language
from order import place_order, review_order, update_order, remove_order, save_order_to_db, give_feedback
from menu import display_menu
from db_config import get_db_connection


def main():
    print("-----------------------------")
    print("Welcome to N14 Restaurant")
    print("-----------------------------")
    lang_choice = input(
        "Select Language / Sélectionnez la langue / Hitamo Ururimi:\n1. English\n2. French\n3. Kinyarwanda\nSelect (1-3): ")
    if lang_choice == '1':
        lang = load_language('english')
    elif lang_choice == '2':
        lang = load_language('french')
    elif lang_choice == '3':
        lang = load_language('kinyarwanda')
    else:
        print("Invalid choice. Defaulting to English.")
        lang = load_language('english')

    print("-----------------------------")
    print(lang['welcome_message'])
    print(lang['welcome_message_2'])
    print("-----------------------------")

    order = []

    while True:
        print("Main Menu:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Review Order")
        print("4. Update Order")
        print("5. Remove Order")
        print("6. Save Order")
        print("7. Give Us Feedback")
        print("8. Exit Application")
        choice = input("Choose an Option (1-8): ")

        if choice == '1':
            display_menu(lang)
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

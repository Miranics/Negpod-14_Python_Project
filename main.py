#!/usr/bin/python3
from order import place_order, review_order, update_order, remove_order, save_order_to_db, give_feedback
from menu import display_menu
from language_loader import load_language


def main():
    print("\n-----------------------------")
    print("Welcome to N14 Restaurant")
    print("-----------------------------")

    # Prompt user to select a language
    print("Select Language / Sélectionnez la langue / Hitamo Ururimi:")
    print("1. English")
    print("2. French")
    print("3. Kinyarwanda")
    lang_choice = input("Enter your choice (1-3): ")

    if lang_choice == '1':
        lang = load_language('english')
    elif lang_choice == '2':
        lang = load_language('french')
    elif lang_choice == '3':
        lang = load_language('kinyarwanda')
    else:
        print("Invalid choice. Defaulting to English.")
        lang = load_language('english')

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

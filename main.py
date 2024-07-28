#!/usr/bin/python3
from order import place_order, review_order, update_order, remove_order, save_order_to_db
from menu import display_menu
from language_loader import load_language


def main():
    language = input(" Welcome! Choose your language (english/french/kinyarwanda): ").strip().lower()
    lang = load_language(language)

    # Short welcome message
    print(f"\n{'-' * 30}\n{lang['short_welcome_message']}\n{'-' * 30}")

    order = []
    while True:
        print(lang['main_menu'])
        print(f"1. {lang['view_menu']}")
        print(f"2. {lang['place_order']}")
        print(f"3. {lang['review_order']}")
        print(f"4. {lang['update_order']}")
        print(f"5. {lang['remove_order']}")
        print(f"6. {lang['save_order']}")
        print(f"7. {lang['exit']}")
        choice = input(lang['enter_choice'])

        if choice == '1':
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
            print(lang['thanks_message'])
            break
        else:
            print(lang['invalid_choice'])


if __name__ == "__main__":
    main()


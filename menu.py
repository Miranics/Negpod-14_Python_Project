# Menu Definition with more food options and set prices

menu = [
    {"name": "Pizza", "price": 12000},
    {"name": "Burger", "price": 6500},
    {"name": "Pasta", "price": 7000},
    {"name": "Salad", "price": 8500},
    {"name": "Soda", "price": 2000},
    {"name": "Fries", "price": 3000},
    {"name": "Steak", "price": 15000},
    {"name": "Ice Cream", "price": 4000},
    {"name": "Sandwich", "price": 6000},
    {"name": "Coffee", "price": 2500},
    {"name": "Tea", "price": 2000},
    {"name": "Soup", "price": 5000},
    {"name": "Chicken Wings", "price": 9000},
    {"name": "Fish and Chips", "price": 10000},
    {"name": "Smoothie", "price": 3500}
]

def display_menu():
    print("Menu")
    for index, item in enumerate(menu, start=1):
        print(f"{index} {item['name']}: {item['price']} RWF")


# Cafe Management Order System

def is_valid_name(name):
    return name.isalpha() and any(c.islower() for c in name) and any(c.isupper() for c in name)

def is_valid_phone(phone):
    return phone.isdigit()

def main():
    # Dictionary for menu
    menu = {
        "Pizza": 40,
        "Pasta": 50,
        "Burger": 60,
        "Salad": 70,
        "Coffee": 80
    }

    print("Welcome to our BarbQue restaurant!")

    # Getting customer's name
    while True:
        name = input("Please enter your name (use both uppercase and lowercase letters): ")
        if is_valid_name(name):
            break
        else:
            print("Invalid name. Please use alphabetical characters and include both uppercase and lowercase letters.")

    # Getting customer's phone number
    while True:
        phone = input("Please enter your phone number (numeric values only): ")
        if is_valid_phone(phone):
            break
        else:
            print("Invalid phone number. Please use numeric values only.")

    print("\nWelcome,", name + "!")
    print("Here's the menu:")

    for item, price in menu.items():
        print(f"{item}: Rs{price}")

    total_price = 0
    while True:
        # Taking order
        order = input("\nEnter the item you want to order: ")
        if order in menu:
            total_price += menu[order]
            print(f"Your order of {order} has been added.")
        else:
            print(f"Sorry, we don't have {order} on the menu.")

        # Asking if they want to order more
        another_order = input("Do you want to order anything else? (yes/no): ").strip().lower()
        if another_order != "yes":
            break

    print(f"\nThe total price to pay is Rs{total_price}")
    print("\nThanks for ordering at BarbQue restaurant. Thank you!")
    print("Visit again!")

if __name__ == "__main__":
    main()

import json
import os

# file paths for persistent data storage
inventory_file = 'inventory.json'
sales_history_file = 'sales_history.json'

# check if files exist, otherwise create them with initial data
def initialize_data():
    if not os.path.exists(inventory_file):
        with open(inventory_file, 'w') as f:
            json.dump({
                '1001': {'name': 'shampoo', 'price': 200, 'stock': 50},
                '1002': {'name': 'toothpaste', 'price': 40, 'stock': 100},
                '1003': {'name': 'soap', 'price': 30, 'stock': 75},
                '1004': {'name': 'washing powder', 'price': 150, 'stock': 60},
                '1005': {'name': 'rice', 'price': 60, 'stock': 200}
            }, f)
    
    if not os.path.exists(sales_history_file):
        with open(sales_history_file, 'w') as f:
            json.dump([], f)

# load inventory data from the file
def load_inventory():
    with open(inventory_file, 'r') as f:
        return json.load(f)

# save updated inventory to the file
def save_inventory(inventory):
    with open(inventory_file, 'w') as f:
        json.dump(inventory, f)

# load sales history from the file
def load_sales_history():
    with open(sales_history_file, 'r') as f:
        return json.load(f)

# save updated sales history to the file
def save_sales_history(sales_history):
    with open(sales_history_file, 'w') as f:
        json.dump(sales_history, f)

# function to display available products
def display_products(inventory):
    print("\navailable products:")
    for product_id, details in inventory.items():
        print(f"product id: {product_id}, name: {details['name']}, price: ₹{details['price']}, stock: {details['stock']}")

# function to handle sales and stock update
def process_sale(inventory):
    total = 0
    items_sold = []
    
    while True:
        product_id = input("\nenter product id to add to cart (or 'done' to finish): ").strip()
        if product_id.lower() == 'done':
            break
        if product_id not in inventory:
            print("invalid product id! please try again.")
            continue
        
        try:
            quantity = int(input(f"enter quantity for {inventory[product_id]['name']} (available stock: {inventory[product_id]['stock']}): "))
        except ValueError:
            print("please enter a valid quantity.")
            continue
        
        if quantity > inventory[product_id]['stock']:
            print("not enough stock available!")
            continue
        
        inventory[product_id]['stock'] -= quantity
        total += inventory[product_id]['price'] * quantity
        items_sold.append((inventory[product_id]['name'], quantity, inventory[product_id]['price']))

    # update sales history
    sales_history = load_sales_history()
    sales_history.append({'items': items_sold, 'total': total})
    save_sales_history(sales_history)

    # generating receipt
    print("\n--- sales receipt ---")
    for item in items_sold:
        print(f"{item[0]} (x{item[1]}) - ₹{item[1] * item[2]}")
    
    print(f"\ntotal amount: ₹{total}")
    print("\nthank you for shopping at d-mart!")

# function to manage inventory (add/remove stock)
def manage_inventory(inventory):
    while True:
        action = input("\ndo you want to add or remove stock? (type 'add' or 'remove', 'exit' to quit): ").strip().lower()
        if action == 'exit':
            break
        elif action not in ['add', 'remove']:
            print("invalid action. try again.")
            continue
        
        product_id = input("enter product id: ").strip()
        if product_id not in inventory:
            print("invalid product id!")
            continue
        
        try:
            quantity = int(input(f"enter quantity to {action}: "))
        except ValueError:
            print("please enter a valid quantity.")
            continue
        
        if action == 'add':
            inventory[product_id]['stock'] += quantity
            print(f"{quantity} units of {inventory[product_id]['name']} added to stock.")
        elif action == 'remove':
            if quantity > inventory[product_id]['stock']:
                print("not enough stock to remove.")
                continue
            inventory[product_id]['stock'] -= quantity
            print(f"{quantity} units of {inventory[product_id]['name']} removed from stock.")

    save_inventory(inventory)

# admin authentication
def admin_login():
    correct_username = "admin"
    correct_password = "password123"

    username = input("enter admin username: ")
    password = input("enter admin password: ")

    if username == correct_username and password == correct_password:
        print("login successful.")
        return True
    else:
        print("invalid credentials.")
        return False

# main menu
def main():
    initialize_data()
    inventory = load_inventory()

    while True:
        print("\n--- d-mart management system ---")
        print("1. display products")
        print("2. process sale")
        print("3. manage inventory (admin only)")
        print("4. exit")

        choice = input("enter your choice: ").strip()
        
        if choice == '1':
            display_products(inventory)
        elif choice == '2':
            process_sale(inventory)
        elif choice == '3':
            if admin_login():
                manage_inventory(inventory)
        elif choice == '4':
            print("exiting the d-mart management system.")
            break
        else:
            print("invalid choice! please try again.")

# run the program
if __name__ == "__main__":
    main()

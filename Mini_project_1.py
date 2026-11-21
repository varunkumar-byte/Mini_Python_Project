"""
PROJECT NAME: Inventory Management System

DESCRIPTION:
This project is developed using Python.
It manages products, inventory, shopping carts
and customer orders.

FEATURES:
1. Display Products
2. Add New Product
3. Calculate Inventory Value
4. Remove Product
5. Add Products to Cart
6. View Shopping Cart
7. Place Order
8. Customer Feedback

PYTHON CONCEPTS USED:
- Dictionary
- List
- Tuple
- Functions
- Loops
- Conditional Statements
"""
# Product Details: ID, Name, Price, Stock
products = {
    101: {"name": "Keyboard(Logitech)", "price": 1800, "stock": 10},
    102: {"name": "Mouse(Asus)", "price": 700, "stock": 15},
    103: {"name": "Monitor(Logitech)", "price": 27000, "stock": 25},
    104: {"name": "Headphones(Sony)", "price": 1500, "stock": 18},
    105: {"name": "Webcam(Canon)", "price": 2500, "stock": 12},
    106: {"name": "USB Drive(Transcend)", "price": 500, "stock": 20},
    107: {"name": "External Hard Drive(Seagate)", "price": 4500, "stock": 27},
    108: {"name": "Graphics Card(Gigabyte)", "price": 35000, "stock": 13},
    109: {"name": "RAM(Corsair)", "price": 8000, "stock": 16},
    110: {"name": "Motherboard(MSI)", "price": 22000, "stock": 34}
}

# Shopping Cart
cart = []


# 1. Display Products
def display_products():
    """
    Function Name: display_products

    Purpose:
    Displays all available products.

    Input:
    No input required.

    Output:
    Displays product ID, name, price and stock.
    """
    print("\n------ AVAILABLE PRODUCTS ------")

    for pid, item in products.items():
        print("ID:", pid)
        print("Name:", item["name"])
        print("Price: ₹", item["price"])
        print("Stock:", item["stock"])
        print("-------------------------")


# 2. Add New Product
def add_product():

    """Adds a new product to the inventory."""

    pid = int(input("Enter Product ID: "))

    if pid in products:
        print("Product ID Already Exists")
        return

    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))

    products[pid] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product Added Successfully!")


# 3. Calculate Inventory Value
def calculate_value():

    """Calculates the total value of available inventory."""

    total = 0

    for item in products.values():
        total += item["price"] * item["stock"]

    print("Total Inventory Value: ₹", total)


# 4. Remove Product
def remove_product():

    """Removes a product from the inventory using its ID."""

    pid = int(input("Enter Product ID to Remove: "))

    if pid in products:
        del products[pid]
        print("Product Removed Successfully!")
    else:
        print("Product ID Not Found")


# 5. Add Products to Cart
def add_to_cart():

    """Allows customers to select products and quantities."""

    while True:
        pid = int(input("\nEnter Product ID (0 to finish): "))

        if pid == 0:
            break

        if pid in products:

            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Enter a Valid Quantity")

            elif quantity > products[pid]["stock"]:
                print("Insufficient Stock")

            else:
                cart.append((pid, quantity))
                print("Product Added to Cart!")

        else:
            print("Product ID Not Found")


# 6. View Cart
def view_cart():

    """Displays the contents of the shopping cart."""

    if not cart:
        print("\nYour Cart is Empty!")

    else:
        print("\n------ YOUR SHOPPING CART ------")

        total = 0

        for pid, quantity in cart:

            name = products[pid]["name"]
            price = products[pid]["price"]

            amount = price * quantity
            total += amount

            print("\nProduct:", name)
            print("Quantity:", quantity)
            print("Price: ₹", price)
            print("Amount: ₹", amount)
            print("-------------------------")

        print("\nTotal Cart Value: ₹", total)


# 7. Place Order
def place_order():

    """
    Places an order for the products in the shopping cart.
    """

    if not cart:
        print("Your Cart is Empty!")
        return

    view_cart()

    confirm = input("\nConfirm Order? (yes/no): ").lower()

    if confirm == "yes":

        for pid, quantity in cart:
            products[pid]["stock"] -= quantity

        print("\nOrder Placed Successfully!")

        total = sum(
            products[pid]["price"] * quantity
            for pid, quantity in cart
        )

        print("Total Amount: ₹", total)

        cart.clear()

    else:
        print("Order Cancelled.")


# 8. Feedback
def feedback():

    """Accepts and displays customer feedback."""

    user_feedback = input("Please Give Your Feedback: ")

    print("Thank You for Your Feedback!")
    print("Your Feedback:", user_feedback)

import matplotlib.pyplot as plt

def show_graph():

    names = []
    stock = []

    for item in products.values():
        names.append(item["name"])
        stock.append(item["stock"])

    plt.figure(figsize=(10, 5))

    plt.bar(names, stock)

    plt.title("Inventory Stock Report")
    plt.xlabel("Products")
    plt.ylabel("Available Stock")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

# Main Menu
while True:

    print("\n====== INVENTORY MANAGEMENT SYSTEM ======")

    print("1. Display Products")
    print("2. Add Product")
    print("3. Calculate Inventory Value")
    print("4. Remove Product")
    print("5. Add to Cart")
    print("6. View Cart")
    print("7. Place Order")
    print("8. Feedback")
    print("9. Show Inventory Graph")
    print("10. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        display_products()

    elif choice == "2":
        add_product()

    elif choice == "3":
        calculate_value()

    elif choice == "4":
        remove_product()

    elif choice == "5":
        add_to_cart()

    elif choice == "6":
        view_cart()

    elif choice == "7":
        place_order()

    elif choice == "8":
        feedback()

    elif choice == "9":
        show_graph()

    elif choice == "10":
        print("Thank You for Using Our System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")

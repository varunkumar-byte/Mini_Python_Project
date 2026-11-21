import matplotlib.pyplot as plt

# Product Details
products = [
    "Keyboard",
    "Mouse",
    "Monitor",
    "Headphones",
    "Webcam",
    "USB Drive",
    "Hard Drive",
    "Graphics Card",
    "RAM",
    "Motherboard"
]

stock = [10, 15, 25, 18, 12, 20, 27, 13, 16, 34]

# Create Bar Graph
plt.figure(figsize=(10, 5))

plt.bar(products, stock)

plt.title("Inventory Management System - Product Stock")
plt.xlabel("Products")
plt.ylabel("Available Stock")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
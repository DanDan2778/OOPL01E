from tabulate import tabulate

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}"

# Clothing Subclass of Product
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}, Size: {self.size}"

# Electronics Subclass of Product
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def get_info(self):
        return f"{self.name}, {self.price},  {self.warranty}"

# ShoppingCart Class that contains a list of products
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def view_cart(self):
        print(tabulate([[product.name, product.price] for product in self.products], headers=["Name", "Price"], tablefmt="fancy_grid"))

    def check_out(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

shopping_cart = ShoppingCart()
shirt = Clothing("Shirt", 20, "M")
phone = Electronics("Phone", 15000, 2)
laptop = Electronics("Laptop", 49000, 3)
jeans = Clothing("Jeans", 1500, "28")

while True:
    print("1. Add to Cart")
    print("2. View Cart")
    print("3. Check Out")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("1. Shirt")
        print("2. Phone")
        print("3. Laptop")
        print("4. Jeans")
        print("5. Back")
        while True:
            choice = int(input("Enter choice: "))
            if choice == 1:
                shopping_cart.add_to_cart(shirt)
            elif choice == 2:
                shopping_cart.add_to_cart(phone)
            elif choice == 3:
                shopping_cart.add_to_cart(laptop)
            elif choice == 4:
                shopping_cart.add_to_cart(jeans)
            elif choice == 5:
                break
            else:
                print("Invalid choice")
    elif choice == 2:
        shopping_cart.view_cart()
    elif choice == 3:
        print(f"Total: {shopping_cart.check_out()}")
    elif choice == 4:
        break
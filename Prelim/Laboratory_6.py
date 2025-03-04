from tabulate import tabulate

class Product:
# Initialize the Product class with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Get the information of the product
    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}"

# Clothing Subclass of Product
class Clothing(Product):
# Initialize the Clothing class with name, price, and size
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
# Get the information of the product
    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}, Size: {self.size}"

# Electronics Subclass of Product

class Electronics(Product):

# Initialize the Electronics class with name, price, and warranty
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

# Get the information of the product
    def get_info(self):
        return f"{self.name}, {self.price},  {self.warranty}"

# ShoppingCart Class that contains a list of products

class ShoppingCart:
# Initialize the ShoppingCart class with an empty list of products
    def __init__(self):
        self.products = []

# Add a product to the list of products
    def add_to_cart(self, product):
        self.products.append(product)

# View the list of products
    def view_cart(self):
        print(tabulate([[product.name, product.price] for product in self.products],
                       headers=["Name", "Price"],
                       tablefmt="fancy_grid"))

# Check out the products in the list
    def check_out(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

# Initialize the ShoppingCart class
shopping_cart = ShoppingCart()

# Create instances of the Clothing and Electronics classes
shirt = Clothing("Shirt", 20, "M")
phone = Electronics("Phone", 15000, 2)
laptop = Electronics("Laptop", 49000, 3)
jeans = Clothing("Jeans", 1500, "28")

# Menu for the user to choose from
while True:
# Create a tabulate menu for the user to choose from
    print(tabulate([[1, "Add to Cart"],
                    [2, "View Cart"],
                    [3, "Checkout"],
                    [4, "Exit"]],
                   headers=['Menu'],
                   tablefmt="orgtbl"))
    choice = int(input("Enter choice: "))
    print('\n'*25)
# Create a tabulate menu for the user to choose from to add in the cart
    if choice == 1:
        # create a tabulate menu for the user to choose from
        while True:
            # display the menu for the user to choose from: product name, warranty/size and price
            print(tabulate([[1, 'Shirt', 'M', 20],
                            [2, 'Phone', '2 Years', 15000],
                            [3, 'Laptop', '3 Years', 49000],
                            [4, 'Jeans', '28', 1500],
                            [5, 'Exit']],
                           headers=['MENU', 'Product Name', 'Warranty/Size', 'Price'],
                           tablefmt="orgtbl"))
            choice = int(input("Enter choice: "))
            if choice == 1:
                shopping_cart.add_to_cart(shirt) # Add the shirt to the cart
            elif choice == 2:
                shopping_cart.add_to_cart(phone) # Add the phone to the cart
            elif choice == 3:
                shopping_cart.add_to_cart(laptop) # Add the laptop to the cart
            elif choice == 4:
                shopping_cart.add_to_cart(jeans) # Add the jeans to the cart
            elif choice == 5:
                break
            else:
                print("Invalid choice")
            print('\n'*25)
            # Display the cart and the total
            print("Added to Cart:")
            shopping_cart.view_cart()
            print('Total:', shopping_cart.check_out())
    elif choice == 2: # View the cart
        # Display the cart and the total
        shopping_cart.view_cart()
        print('Total:', shopping_cart.check_out())
    elif choice == 3: # Checkout
        # Display the cart and the total
        shopping_cart.view_cart()
        print(f"Total: {shopping_cart.check_out()}")
        choice = input("Confirm Checkout? (Y/N): ")
        # Confirm the checkout
        if choice.lower() == "y":
            print("Checkout Successful")
            break
    elif choice == 4: # Exit the program
        break
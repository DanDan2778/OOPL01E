# Class for Car
class Car:

# Initializing
    def __init__(self, brand, model, year, engine):
        # Value Holder
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine

# Displaying Information
    def display_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Engine: {self.engine}')
        print()

# Initialize Objects for Class Car
car1 = Car('Toyota', 'Fortuner', 2025, 'Hybrid')
car2 = Car('Ford', 'Everest', 2025, 'Gasoline')
car3 = Car('Mitsubishi', 'Montero', 2025, 'Diesel')

# Displaying Initialized Object
print('Cars: ')
car1.display_info()
car2.display_info()
car3.display_info()
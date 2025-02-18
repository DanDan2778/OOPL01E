class Car:
    def __init__(self, brand, model, year, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine

    def display_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Engine: {self.engine}')

car1 = Car('Toyota', 'Fortuner', 2025, 'Hybrid')
car1.display_info()
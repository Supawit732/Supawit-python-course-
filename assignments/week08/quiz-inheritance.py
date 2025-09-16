""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year
    
    def get_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nModel year: {self.year}"
    
class Car(Vehicle): 
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.doors = number_of_doors
    def get_info(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nModel year: {self.year}\nAll door = {self.doors}"
    
vehicle = Vehicle("Toyota","Camry",2025)
print(vehicle.get_info())

print("")

car =Car("Toyota","Crown Sport",2025,5)
print(car.get_info())

    
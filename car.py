class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        long_name = f"This car is a {self.year} {self.model} {self.make}."
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
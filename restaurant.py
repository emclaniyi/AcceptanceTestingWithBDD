class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def open_restaurant(self):
        print(f"Welcome, {self.name} is now open for business")

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name} and we serve {self.cuisine}-cuisines")


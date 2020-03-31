''' Страница упражнения - 182 '''

# 9-10
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name + " : " + self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant open")

    def increment_number_served(self, amount):
        self.number_served += amount
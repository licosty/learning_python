''' Страница упражнения - 165 '''

# 9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " : " + self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant open")

restaurant = Restaurant('Китайская Грамота', 'Китайская')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
restaurant2 = Restaurant('Боэми', 'Европейская')
restaurant3 = Restaurant('Osteria Mario', 'Итальянская')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("first name: " + self.first_name)
        print("last name: " + self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name, self.last_name)


user1 = User('Hoba', 'Aboh')
user2 = User('Boba', 'Abob')

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
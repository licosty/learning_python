''' Страница упражнения - 169 '''

# 9-4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 9-4
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name + " : " + self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant open")

    def increment_number_served(self, amount):
        self.number_served += amount

restaurant4 = Restaurant('Мари Vanna', 'Русская')
restaurant4.number_served = 30
print(restaurant4.number_served)
restaurant4.increment_number_served(20)
print(restaurant4.number_served)

# 9-5
class User():
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print("first name: " + self.first_name)
        print("last name: " + self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name, self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user3 = User('Ad', 'Da')
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)
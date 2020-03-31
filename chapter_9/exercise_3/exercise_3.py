''' Страница упражнения - 176 '''

from exercise_2 import Restaurant, User

# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors

    def describe_flovers(self):
        for flovor in self.flavors.items():
            print(flovor)

# 9-7
class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)

# 9-8
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

admin = Admin('admin', 'admin', ["add user", "del user", "change user"])
admin.privileges.show_privileges()

# 9-9
# car.py
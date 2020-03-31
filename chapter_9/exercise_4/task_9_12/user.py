''' Страница упражнения - 182 '''

# 9-12
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
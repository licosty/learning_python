''' Страница упражнения - 216 '''

# 11-3
class Employee():
    def __init__(self, first, last, salaty):
        self.first_name = first
        self.last_name = last
        self.salary = salaty

    def give_raise(self, count=None):
        if count:
            self.salary += count
        else:
            self.salary += 5000
        return self.salary
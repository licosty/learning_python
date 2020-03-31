''' Страница упражнения - 183 '''

# 9-13
from collections import OrderedDict
from random import randint

gloss = OrderedDict()
gloss['переменная'] = 'это переменная'
gloss['список'] = 'это список'
gloss['кортеж'] = 'это кортеж'

print()
for word, value in gloss.items():
    print(word + ': ' + value)

# 9-14
print()
class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(str(x), end=' ')

die = Die()
for i in range(10):
    die.roll_die()
print()
die = Die(10)
for i in range(10):
    die.roll_die()
print()
die = Die(20)
for i in range(10):
    die.roll_die()
''' Страница упражнения - 133 '''

# 7-8 7-9
sandwich_orders = ['Бокадильо', 'Арепа', 'Кацу-сандо', 'Pastrami', 'Pastrami', 'Pastrami']
finished_sandwiches = []

print('Pastrami is not')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

for sandwich in sandwich_orders:
    print('I made your ' + sandwich)
    finished_sandwiches.append(sandwich)
for sandwich in finished_sandwiches:
    print(sandwich)

# 7-10
resting_place = []
n = 0
while n < 4:
    resting_place.append(input("Where do you want to spend your vacation? "))
    n += 1

for place in resting_place:
    print(place)
''' Страница упражнения - 130 '''

# 7-4
topping = ''
while True:
    topping = input('Input topping ')
    if topping == 'quit': break
    print(topping.title() + ' add in order ')

# 7-5 7-6
print()
active = True
while active:
    age = input("Input your age or 'q' for exit: ")
    if age == 'q': break

    age = int(age)
    if age < 3:
        print('Ticket is free')
        active = False
    elif 3 <= age < 12:
        print('Price of ticket $10')
    elif 12 < age:
        print('Price of ticket $15')

# 7-7
while 1:
    print("infinity")
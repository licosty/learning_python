''' Страница упражнения - 124 '''

# 7-1
car = input('Какую машину хотите? ')
print('Let me see if i can find you a ' + car)

# 7-2
table = int(input('\nHow many people need a table? '))
if table > 8:
    print('Please wait')
else:
    print('Table is ready')

# 7-3
num = int(input('\nInput anything number: '))
if num % 10:
    print('The number ' + str(num) + ' is not a multiple of 10')
else:
    print('The number' + str(num) + ' is a multiple of 10')
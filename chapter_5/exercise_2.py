''' Страница упражнения - 95 '''

# 5-3
alien_color = 'green'
if 'green' == alien_color:
    print('5')

if 'blue' != alien_color:
    a = 'blue'

# 5-4
if 'green' == alien_color:
    print('You get +5 points!')
else:
    print('You get +10 points!')

if 'blue' == alien_color:
    print('You get +5 points!')
else:
    print('You get +10 points!')

# 5-5
print()
if 'green' == alien_color:
    print('You get +5 points!')
elif 'yellow' == alien_color:
    print('You get +10 points!')
elif 'red' == alien_color:
    print('You get +15 points!')

# 5-6
print()
age = 28

if age < 2:
    print('baby')
elif 2 <= age < 4:
    print('kid')
elif 4 <= age < 13:
    print('child')
elif 13 <= age < 20:
    print('teen')
elif 20 <= age < 65:
    print('adult')
elif 65 <= age:
    print('old man')

# 5-7
print()
fruits = ['Груша', 'Черешня', 'Манго']

print('Черешня' in fruits)
print('Манго' in fruits)

if 'Черешня' in fruits:
    print('You really like черешня')
if 'Манго' in fruits:
    print('You really like манго')
if 'Banana' in fruits:
    print('You really like бананы')

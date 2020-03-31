''' Страница упражнения - 76, 79 '''

# 4-10
cubes = [i for i in range(1, 11)]
print('\nThe first three items in the list are:')
print(cubes[:3])
print('Three items from the middle of the list are:')
print(cubes[len(cubes)//2:len(cubes)//2 + 3])
print('The last three items in the list are:')
print(cubes[-3:])

# 4-11
print()
pizzas = ['Неаполетано', 'Маргарита', 'Четыре сезона']
friend_pizzas = pizzas[:]
pizzas.append('Кальцоне')
friend_pizzas.append('Регина')
print('My favorite pizzas are:')
print(*[pizza for pizza in pizzas])
print("My friend's favorite pizzas are:")
print(*[f_pizza for f_pizza in friend_pizzas])

# 4-13
print()
menu = ('цыпа табака', 'борщ', 'пюре с котлеткой', 'компот', 'пирожок')
for dish in menu:
    print(dish, end=' ')
# or
print()
print(*menu)

menu = ('хот-дог', 'такос', 'пюре с котлеткой', 'компот', 'пирожок')
print(*menu)
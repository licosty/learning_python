''' Страница упражнения - 119 '''

# 6-7
person = {'first_name': 'Diana', 'last_name': 'Chigantseva', 'age': 28, 'city': 'Krasnodar'}
person2 = {'first_name': 'Hoba', 'last_name': 'Aboh', 'age': 50, 'city': 'Krasnodar'}
person3 = {'first_name': 'Boba', 'last_name': 'Abob', 'age': 23, 'city': 'Krasnodar'}
people = [person, person2, person3]

for person in people:
    for key, value in person.items():
        print(key + ': ' + str(value), end=' ')
    print()

# 6-8
print()
hoba = {'cat': 'Diana'}
boba = {'dog': 'Sergei'}
ad = {'hamster': 'Mama'}
pets = [hoba, boba, ad]

for pet in pets:
    for key, value in pet.items():
        print(key + ': ' + str(value), end=' ')
    print()

# 6-9
print()
favorite_places = {'Hoba': ['park', 'forest'],
                   'Boba': ['home', 'forest'],
                   'Ad': ['forest', 'home', 'country']}
for person, places in favorite_places.items():
    print(person + "'s favorite places are:")
    for place in places:
        print('\t' + place)

# 6-10
print()
favorite_numbers = {'Hoba': [7, 15], 'Boba': [5, 23], 'Ad': [8]}
for person, numbers in favorite_numbers.items():
    print(person + "'s favorite numbers are:")
    for num in numbers:
        print('\t' + str(num))

# 6-11
print()
cities = {'Krasnodar': {'county': 'Russia', 'population': '5', 'fact': 'south'},
          'Tula': {'county': 'Russia', 'population': '3', 'fact': 'center'},
          'Moscow': {'county': 'Russia', 'population': '50', 'fact': 'center'}
          }
for city, city_info in cities.items():
    print(city + ":")
    for info, value in city_info.items():
        print('\t' + info + ': ' + value)
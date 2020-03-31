''' Страница упражнения - 113 '''

# 6-4
gloss = {'переменная': 'это переменная', 'список': 'это список', 'кортеж': 'это кортеж'}

print()
for word, value in gloss.items():
    print(word + ': ' + value)

# 6-5
print()
rivers = {"Kuban'": "Russia", "Amazon": "Brazil", "Niger": "Nigeria"}
for river, country in rivers.items():
    print("The " + river + " runs through " + country)
print()
print(*(i for i in rivers.keys()))
print(*(i for i in rivers.values()))

# 6-6
print()
numbers = {'Hoba': 7, 'Boba': 5, 'Ad': 8}
favorite_language = ['Hoba', 'Kevin', 'John', 'Boba', 'Ad']
for name in favorite_language:
    if name in numbers:
        print(name + '. Thank you')
    else:
        print(name + ', please take the survey')
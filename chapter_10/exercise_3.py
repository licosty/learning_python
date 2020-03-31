''' Страница упражнения - 203 '''

# 10-6 10-7
while 1:
    try:
        num1 = input("Input number 1: ")
        if num1 == 'q': break
        num2 = input("Input number 2: ")
        if num2 == 'q': break

        num1 = int(num1)
        num2 = int(num2)

    except ValueError:
        print("Number 1 or number 2 not digital")

    else:
        print(num1 + num2)

# 10-8
print()
try:
    with open('cats.txt') as rfile:
        cats = rfile.read().rstrip()

    with open('dogs.txt') as rfile:
        dogs = rfile.read().rstrip()
except FileNotFoundError:
    # print('File not found')
    # 10-9
    pass
else:
    print(cats)
    print(dogs)

# 10-10
print()
words = ''
try:
    with open('cats.txt') as rfile:
        words = rfile.read()

except FileNotFoundError:
    pass
else:
    print(words.count("CatHoba"))
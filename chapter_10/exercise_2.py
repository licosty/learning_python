''' Страница упражнения - 195 '''

# 10-3
print()
name = input('Input your name: ')
with open('guest.txt', 'w') as wfile:
    wfile.write(name)

# 10-4
print()
with open('guest_book.txt', 'w') as wfile:
    while 1:
        name = input('Input your name (or "q" for exit: ')
        if name == 'q': break
        print('Hello ' + name)
        wfile.write(name + '\n')

# 10-5
print()
with open('answer.txt', 'w') as wfile:
    while 1:
        cause = input('Why do you like programming? (input "q" for exit)')
        if cause == 'q': break
        wfile.write(cause + "\n")
''' Страница упражнения - 151 '''

# 8-9
print()
magicians = ['hoba', 'boba', 'ad']
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title(), end=' ')

show_magicians(magicians)

# 8-10
def make_great(magicians):
    for magician in range(len(magicians)):
        magicians[magician] = 'Greate' + magicians[magician].title()
    return magicians

# 8-11
magicians2 = make_great(magicians[:])
show_magicians(magicians2)
print()
show_magicians(magicians)
''' Страница упражнения - 147 '''

# 8-6
def city_country(city, country):
    return city.title() + " " + country.title()

city_country1 = city_country('Soul', 'Korea')
city_country2 = city_country('Tokyo', 'Japan')
city_country3 = city_country('Krasnodar', 'Russia')

# 8-7
print()
def make_album(author, title, count_tracks=''):
    album = {'author': author, 'title': title}
    if count_tracks:
        album['countet_tracks'] = count_tracks
    return album

album1 = make_album('Death', 'Symbolic')
album2 = make_album('Sepultura', 'Roorback', '13')
album3 = make_album('Skid Row', 'Thickskin', '12')

print(album1)
print(album2)

# 8-8
print()
while 1:
    author = input("Input author of album or 'q' for exit ")
    if author == 'q': break
    title = input("Input title of album or 'q' for exit ")
    if title == 'q': break

    album = make_album(author, title)
    print(album)
''' Страница упражнения - 216 '''

# 11-1 11-2
def city_functions(city, country, population=None):
    result = city.title() + ", " + country.title()
    if population:
        result += " - population " + str(population)
    return result
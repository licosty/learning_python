''' Страница упражнения - 142 '''

# 8-3 8-4
def make_shirt(size = 'L', text = 'I love Python'):
    print('Shirt size ' + size + " with text '" + text + "' on it")

make_shirt('S', 'hey')
make_shirt(text='Hi everyone', size='M')
make_shirt('L')

# 8-5
print()
def describe_city(city, country = 'Russia'):
    print(city + ' is in ' + country)

describe_city('Krasnodar')
describe_city('Soul')
describe_city('Tokyo')
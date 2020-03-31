''' Страница упражнения - 154 '''

# 8-12
def sandwich_components(*components):
    for component in components:
        print(component)

# 8-13
print()
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Diana', 'Chigantseva')
print(user_profile)

# 8-14
print()
def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model

    for key, value in car_info.items():
        car[key] = value

    return car

car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)
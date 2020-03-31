''' Страница упражнения - 95 '''

# 5-8
print()
users = ['anna', 'ivan', 'kevin', 'admin', 'john']

for user in users:
    if user == 'admin':
        print('Hello' + user + 'would you like to see a status report?')
    else:
        print('Hello ' + user + ', thank you for logging in again')

# 5-9
print()
if users:
    users.clear()
else:
    print('We need to find some users')

if users:
    users.clear()
else:
    print('We need to find some users')

# 5-10
print()
current_users = ['anna', 'ivan', 'kevin', 'admin', 'john']
new_users = ['inna', 'oleg', 'john', 'admin', 'john']

for user in new_users:
    if user.lower() in current_users:
        print('Select new name')
    else:
        print('Name is available')

# 5-11
print()
numbers = [i for i in range(1, 10)]
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')
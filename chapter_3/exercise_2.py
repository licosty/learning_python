''' Страница упражнения - 55 '''

# 3-4
print()
party = ['Hoba', 'Boba', 'Ad']
print('Hey ' + party[0] + ', go to my party')
print('Hey ' + party[1] + ', go to my party')
print('Hey ' + party[2] + ', go to my party')

# 3-5
print()
print(party[2])
party[2] = 'Kevin'
print('Hey ' + party[0] + ', go to my party')
print('Hey ' + party[1] + ', go to my party')
print('Hey ' + party[2] + ', go to my party')

# 3-6
print()
print('More guests for the god of guests!!!')
party.insert(0, 'Merry')
party.insert(2, 'Bill')
party.append('you')
print('Hey ' + party[0] + ', go to my party')
print('Hey ' + party[1] + ', go to my party')
print('Hey ' + party[2] + ', go to my party')
print('Hey ' + party[3] + ', go to my party')
print('Hey ' + party[4] + ', go to my party')
print('Hey ' + party[5] + ', go to my party')

# 3-7
print()
print('Only two of you will go to lunch. Fight!')
print(party.pop() + " couldn't ")
print(party.pop() + " couldn't ")
print(party.pop() + " couldn't ")
print(party.pop() + " couldn't ")
print('Hey ' + party[0] + ', go to my party (now for sure)')
print('Hey ' + party[1] + ', go to my party (now for sure)')
del party[1]
del party[0]
print(party)
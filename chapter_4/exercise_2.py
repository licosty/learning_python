''' Страница упражнения - 72 '''

# 4-3
print()
for i in range(1, 21):
    print(i, end=' ')
# or
print()
print(*[i for i in range(1, 21)], end=' ')

# 4-4
print()
for i in range(1, 1_000_001):
    print(i, end='')
# or
print()
print(*[i for i in range(1, 1_000_001)])

# 4-5
print()
million = [i for i in range(1, 1_000_001)]
print(min(million))
print(max(million))
print(sum(million))

# 4-6
print()
nums = [i for i in range(1, 21, 2)]
for num in nums:
    print(num, end=' ')
# or
print()
print(*[i for i in range(1, 21, 2)])

# 4-7
print()
nums = [i for i in range(3, 31, 3)]
for num in nums:
    print(num, end=' ')
# or
print()
print(*[i for i in range(3, 31, 3)])

# 4-8
print()
cubes = [i for i in range(1, 11)]
for cube in cubes:
    print(cube**3, end=' ')

# 4-9
print()
print(*[i**3 for i in range(1, 11)])
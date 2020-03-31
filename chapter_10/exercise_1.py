''' Страница упражнения - 192 '''

# 10-1
with open('learning_python.txt') as rfile:
    lines = rfile.read()
    print(lines)

with open('learning_python.txt') as rfile:
    for line in rfile:
        print(line.rstrip())

with open('learning_python.txt') as rfile:
    lines = rfile.readlines()

for line in lines:
    print(line.rstrip())

# 10-2
print()
for line in lines:
    print(line.rstrip().replace('Python', 'Java'))
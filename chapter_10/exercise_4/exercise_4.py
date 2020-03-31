''' Страница упражнения - 209 '''

# 10-11 10-12
import json

file_name = "favorite_number.json"

try:
    with open(file_name) as rfile:
        favorite_number = json.load(rfile)
except FileNotFoundError:
    with open(file_name, 'w') as wfile:
        favorite_number = input("Input you favorite number: ")
        json.dump(favorite_number, wfile)
else:
    print("I now your favorite number! It's " + favorite_number)

# 10-13
# remember_me.py

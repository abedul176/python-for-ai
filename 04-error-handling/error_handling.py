try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    print(score)
except NameError:
    print("Variable 'score' is not defined!")

try:
    result = "hello" + 5
except TypeError:
    print("Cannot add string and number!")

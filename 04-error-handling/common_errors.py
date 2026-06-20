import os

try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = ""
    print("FileNotFoundError: file not found, using default")

try:
    age = int("hello")
except ValueError:
    print("ValueError: cannot convert 'hello' to int")

float_str = "12.5"
number = int(float(float_str))
print(f"Converted carefully: {number}")

user = {"name": "Alice", "age": 25}
email = user.get("email", "no-email@example.com")
print(f"KeyError fix with get(): {email}")

numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("IndexError: list too short")

try:
    result = "hello" + 5
except TypeError:
    print("TypeError: cannot add string and number")
    result = "hello" + str(5)
    print(f"Fixed: {result}")

try:
    text = "hello"
    text.append("!")
except AttributeError:
    print("AttributeError: strings don't have append")
    text = text + "!"
    print(f"Fixed: {text}")

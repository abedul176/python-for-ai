def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

result = add_return(5, 3)
print(f"The result is {result}")

def calculate_area(width, height):
    area = width * height
    return area

room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")

def double(number):
    return number * 2

result = double(5)

total = double(5) + double(3)

print(double(10))

if double(7) > 10:
    print("Big number!")

def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")

result = get_min_max([5, 2, 8, 1, 9])
print(result)

def get_greeting_print(name):
    print(f"Hello, {name}!")

def get_greeting_return(name):
    return f"Hello, {name}!"

message = get_greeting_print("Alice")
print(message)

message = get_greeting_return("Alice")
print(message.upper())

def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")
print(result)

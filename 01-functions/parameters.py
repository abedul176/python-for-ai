def greet_alice():
    print("Hello, Alice!")

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")

def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")

introduce("Alice", 25)
introduce("Bob", 30)

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculate_total(100, 0.08, 10)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")

greet("Bob", "Hi")
greet("Charlie", "Hey")

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

create_profile("Alice", 25, "NYC")

create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)

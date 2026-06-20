def greet():
    print("Hello, world!")
    print("Welcome to Python!")

greet()


def function_name():
    pass


def calculate_total():
    pass

def send_email():
    pass

def validate_password():
    pass

def func1():
    pass

def Calculate():
    pass


def say_goodbye():
    print("Goodbye!")
    print("See you later!")

say_goodbye()
say_goodbye()
say_goodbye()


def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

check_weather()


def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price()


discount_rate = 0.15

def apply_discount(price):
    discount = price * discount_rate
    return price - discount

result = apply_discount(100)
print(result)


counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)


total = 0

def add_to_total(amount):
    global total
    total += amount


def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True

    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return f"{self.name} barks: Woof!"

    def describe(self):
        return f"{self.name} is a {self.breed}"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} meows: Meow!"

golden = Dog("Buddy", "Golden Retriever")
cat = Cat(name="Whiskers")
print(golden.describe())
print(golden.is_pet)
print(golden.make_sound())
print(cat.make_sound())

class TextModel:
    def __init__(self, model_name, max_length=1000):
        self.model_name = model_name
        self.max_length = max_length
        self.is_loaded = False

    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True

    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed: {text}"

model = TextModel(model_name="gpt-3.5-turbo", max_length=100)
result = model.process_text(text="Hello world")
print(result)

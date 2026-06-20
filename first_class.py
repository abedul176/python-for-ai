class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog(name="Max", breed="Beagle")
print(dog1.name)
print(dog2.breed)

class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

dev_config = APIConfig("sk-dev-key", max_tokens=50)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)
print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)

config1 = APIConfig(api_key="key1", max_tokens=50)
config2 = APIConfig(api_key="key2", max_tokens=200)
config1.max_tokens = 75
print(config1.max_tokens)
print(config2.max_tokens)
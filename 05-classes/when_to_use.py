def clean_text(text):
    return text.strip().lower()

def remove_punctuation(text):
    return text.replace(".", "").replace(",", "")

result = remove_punctuation(clean_text("  Hello, World.  "))
print(result)

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def clean(self):
        self.text = self.text.strip().lower()
        return self

    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self

processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text
print(result)

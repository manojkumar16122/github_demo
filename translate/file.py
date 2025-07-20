from googletrans import Translator

# Initialize the Translator object
translator = Translator()

# Translate text (auto-detects source language, default target is English)
result = translator.translate('namaste')
print(result.text)  # Output: Hello world

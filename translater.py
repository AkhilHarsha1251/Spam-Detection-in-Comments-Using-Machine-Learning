from translate import Translator
from langdetect import detect

def translate_to_english(text):
    source_lang = detect(text)
    translator = Translator(to_lang="en", from_lang=source_lang)
    translated_text = translator.translate(text)
    return translated_text

if __name__ == "__main__":
    text_to_translate = input("Enter the text to translate: ")
    translated_text = translate_to_english(text_to_translate)
    print("Translated text:", translated_text)

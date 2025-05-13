import pyttsx3
from deep_translator import GoogleTranslator

def translate_to_speech():
    language_dict = {
        "en": "English",
        "es": "Spanish",
        "tl": "Tagalog",
    }

    while True:
        language_input = input(
                "Choose a language (en, es, tl): ").lower()

        if language_input in language_dict:
            break
        else:
            print("Invalid choice, try again.")


    text = input("Enter the text to be translated: ")

    translated_text = GoogleTranslator(
            source = 'auto', target = language_input).translate(text)

    print(f"Original text is: {text}")
    print(f"Translated text in {language_dict[language_input]}: "
          f"{translated_text}\n")

    engine = pyttsx3.init()
    engine.say(translated_text)
    engine.runAndWait()

translate_to_speech()
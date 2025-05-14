from polytechpackage.victorio import translate_to_speech
from polytechpackage.raquem import display_fake_profile
from polytechpackage.niones import hex_to_rgb_colors
from polytechpackage.capilitan import random_joke
from polytechpackage.villarta import display_emoji_message
#TODO (Victorio):
#    Create a module named after your last name. (victorio.py)
#    create a function that does anything
#    Use at least 1 external module from PyPI

#TODO (Niones):
#    Create a module named after your last name. (niones.py)
#    Create a function that does anything
#    Use at least 1 external module from PyPI

#TODO (Capilitan):
#    Create a module named after your last name. (capilitan.py)
#    Create a function that does anything
#    Use at least 1 external module from PyPI

#TODO (Villarta):
#    Create a module named after your last name. (villarta.py)
#    Create a function that does anything
#    Use at least 1 external module from PyPI

#TODO (Everyone):
#    Import all created modules in this file (main.py).
#    Call the function from each module in this file.

def main_menu():
    while True:
        # Loop continues until user chooses 6
        print("---[External Module]---")
        print("1. Translate To Speech")
        print("2. Fake Profile Generator")
        print("3. Hex To RGB Converter")
        print("4. Random Joke")
        print("5. Show Emoji Message")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 6:
            print("Exiting the program...")
            break

        match choice:
            case 1:
                translate_to_speech()
            case 2:
                display_fake_profile()
            case 3:
                hex_to_rgb_colors()
            case 4:
                random_joke()
            case 5:
                display_emoji_message()
            case _:
                print("Invalid choice, please try again.")

main_menu()


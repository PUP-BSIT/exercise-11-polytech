from pyjokes import get_joke

def random_joke():
    joke = get_joke()
    print(f"Here's a joke for you: {joke}")
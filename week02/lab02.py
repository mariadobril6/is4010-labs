
def make_greeting(name):
    return f"Hello, {name}!"


def is_even(number):
    return number % 2 == 0


def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.
    >>> repeat_string("hi", 2)
    'hi hi'
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length    


def format_sentence(phrase):
    """
    Format a phrase as a sentence:
    - Start with a capital
    - End with a single full stop

    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('good day')
    'Good day.'
    """
    phrase = phrase.strip()
    phrase = phrase[0].upper() + phrase[1:]
    if not phrase.endswith("."):
        phrase += "."
    return phrase

def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"

    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    default_car = Car()
    assert default_car.fuel == 0, "Default fuel is not set to 0"

    custom_car = Car(fuel=10)
    assert custom_car.fuel == 10, "Car does not set custom fuel correctly"


run_tests()
doctest.testmod()


import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    story = (
        f"Yesterday, I saw a {adjective} {noun} walking down the street. "
        f"It suddenly decided to {verb} toward the park, where it found "
        f"another {adjective} {noun}. The two became friends and spent "
        f"the afternoon together. It was an unforgettable adventure!"
    )
    return story


def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number from 1 to 100: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You guessed the number!")
            break

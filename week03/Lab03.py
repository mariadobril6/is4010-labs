import random

def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f""Yesterday, I saw a **{adjective} {noun}** walking down the street. It suddenly decided to **{verb}** toward the park, where it found a **{adjective} {noun}** sitting on a bench. The two became friends and spent the afternoon **{verb}ing** together. By the end of the day, they were so **{adjective}** that they decided to **{verb}** home and tell everyone about their crazy adventure.

def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.rnadint(1,100)

    While True:
        guess = int(int"Guess a number from 1 to 100: "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You guessed the number!")
            break

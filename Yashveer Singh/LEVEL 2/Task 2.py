import random

def guess_number(min_value, max_value):

    #NUMBER GUESSER GAME

    number = random.randint(min_value, max_value)
    guess = -1
    while guess != number:
        guess = int(input("Guess a number between {} and {}:".format(min_value, max_value)))
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
    return guess

def main():
    """Plays the guessing game."""

    min_value = int(input("Enter the minimum value:"))
    max_value = int(input("Enter the maximum value:"))
    guess =  guess_number(min_value, max_value)
    print("Congratulations! You guessed the number {} correctly.".format(guess))

if __name__ == "__main__":
    main()
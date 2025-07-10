import random

def guess_number():


    number = random.randint(1, 100)
    guess = -1
    while guess != number:
        guess= int(input("Guess a number between 1 and 100:"))
        if guess < number:
            print("Too low.")
        elif guess > number:
            
            print("Too high.")
    return guess

def main():
    """THE GUESSING GAME."""

    guess = guess_number()
    print("Congratulations! You guessed the number {} correctly.",format(guess))

if __name__== "__main__":
    main()
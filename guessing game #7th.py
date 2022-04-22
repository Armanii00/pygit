import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('guess a number between 1 and {x}: '))
        if guess < random_number:
            print("sorry, guess again. too late")
        elif guess > random_number:
            print("sorry, guss again.too high.")

    print(f"yay, congrats. you guessed the number {random_number} correctly.")

guess(10)
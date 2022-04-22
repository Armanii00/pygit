from random import randint

for x in range(1,4):
    GuessNumber = int(input("Enter your guess between 1 to 5: "))
    randomNumber = randint(1, 5)

    if GuessNumber == randomNumber:
        print("you have won")
    else:
        print("you have lost")
        print("Random number was : ", randomNumber)
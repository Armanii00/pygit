import random
from words import words

def get_valid_word(words):
    word = random.choice(words)#randomly choose from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.lower()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() #what the user has guessed

    #getting user input
    user_letter = input("Guess a letter: ").lower()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print("you have already used that character.please tru again.")

    else:
        print("Invalid chacter.")


user_input = input("Type something: ")
print(user_input)
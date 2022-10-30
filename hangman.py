import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in words:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    chances = 10

    #getting user input
    while len(word_letters)>0 and chances>0:
        print("You have",chances,"chances left and you have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if(user_letter in word_letters):
                word_letters.remove(user_letter)
            else:
                chances = chances - 1;
                print("The letter in not in the word!")
        elif user_letter in used_letters:
            print("You have already guessed this letter!")
        else:
            print("You have entered an invalid character. Please Try Again!")
    
    if chances == 0:
        print("Sorry, you ran out of chances! The word was", word)
    else:
        print("Congratulations! You have guessed the word!", word)
hangman()

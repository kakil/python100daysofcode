# Day 7: Hangman Game 

import random 
from hangman_words import word_list
from hangman_art import stages, logo



chosen_word = word_list[random.randint(0,2)]
word_length = len(chosen_word)

# Set 'lives' to equal 6
lives = 6

# TODO-3: Iimport logo from hangman_art.py and print to start the game.
print(f"{logo}\n\n")


display = []

for n in chosen_word:
    display.append("_")


end_game = False

while end_game == False:
    # Guess a letter
    guess = input("Guess a letter: ").lower()


    # Test code
    # print(f"The letter guessed is: {guess}")


    # Check if letter is in word
    found = False

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            found = True
            display[index] = letter
                

    if found == False:
        lives -= 1
        if lives == 0:
                print("You lose.")
                end_game = True
        
    print(f"{''.join(display)}")
    
    print(f"{stages[lives]}")
    
    if "_" not in display:
        end_game = True
        print("You win.")





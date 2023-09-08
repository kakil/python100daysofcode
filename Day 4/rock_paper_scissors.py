## Day 4 - Challenge 4: Rock, Paper, Scissors Game

# Rock wins againt scissors
# Scissors wins againt paper
# Paper wins against rock

import random

rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
'''

paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)
'''

scissors = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
'''

result = ""
player1_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

computer_choice = random.randint(0, 2)

game_images = [rock, paper, scissors]

if player1_choice >=3 or player1_choice < 0:
    result = ("Invalid choice")

elif player1_choice == 0:
    if computer_choice == 1:
        result = "You Lose!"
    elif computer_choice == 0:
        result = "Tie"
    else:
        result = "YOU WIN !!"
        
elif player1_choice == 1:
    if computer_choice == 2:
        result = "You Lose!"
    elif computer_choice == 1:
        result = "Tie"
    else:
        result = "YOU WIN !!"
        
else:   
    if computer_choice == 0:
        result = "You Lose!"
    elif computer_choice == 2:
        result = "Tie"
    else:
        result = "YOU WIN !!"

if result != 'Invalid choice':
    print("\nPlayer 1 chose:")
    print(f"{game_images[player1_choice]}")

    print("Computer chose:")
    print(f"{game_images[computer_choice]}")

    print(result)
else:
    print(result)
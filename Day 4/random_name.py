## Day 4 - Challenge 2: Random Name

# Instructions
#
# You are going to write a program which will select a randome
# name from a list of names.  The person selected will have to pay
# for everybody's food bill.
#
# Important:  You are not allowed to use the choice() function

import random

# Split string method
#names_string = input("Give me everyone's names, sepearated by a comma. ")
#names = names_string.split(", ")
#print(names)
#random_number = random.randint(0, len(names) - 1)
#print(f"{names[random_number]} is going to buy the meal today");

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
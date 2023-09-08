## Day 4 - Challenge 3: Treasure Map
#
# Instructions
#
# You are going to write a program which will mark a spot with an X.
# The map is made of 3 rows of blank squares.
# Your program should allow you to enter the position of the treasure
# using a two-digit system.  The first digit is the vertical column number
# and the second digit is the horizontal row number.

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1

map[row][column] = '❎'
print(f"{row1}\n{row2}\n{row3}")

print(f"Column = {column}")
print(f"Row = {row}")



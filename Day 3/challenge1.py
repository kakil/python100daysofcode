# Day 3 - Challenge 1: Even or Odd

# Write a program that works out whether a given number is an odd or even
# number.
# Even numbers can be divided by 2 with no remainder.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else: 
    print("This is an odd number")
    

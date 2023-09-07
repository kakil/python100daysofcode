# Data Types

# String

print("Hello"[4])

## Code Challenge
## Write a program that adds the digits in a 2 digit number
## e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit numbert: ")

two_digit_string = str(two_digit_number)
first_digit = int(two_digit_string[0])
second_digit = int(two_digit_string[1])

print(str(first_digit) + " + " + str(second_digit) + " = " + str(first_digit+second_digit))





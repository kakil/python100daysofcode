# Challenge 3: Your Life In Weeks

# Create a program using math and f-Strings that tells us how many
# days, weeks, months we have left if we live until 90 years old.
#
# It will take your current age as the input and output a message with
# our time left in this format:
#
# You have x days, y weeks, and z months left.
#
# Where x, y, and z are replaced with the actual calculated numbers.
#
# Example Input
# 56
#
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.
#
# Given:  1 year = 365 days, 1 year = 52 weeks, 1 year = 12 months

age = input("What is your current age? ")

months_remaining = (90 - int(age)) * 12
weeks_remaining = (90 - int(age)) * 52
days_remaining = (90 - int(age)) * 365

print(f"{days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")

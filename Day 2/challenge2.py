# Day 2: Challenge 2

# Instructions:
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and
# a short person both weigh the same amount, the short person is usually more overweight.
#
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#
# BMI = weight(kg)/height^2(m^2)
#
# Result should be converted to a whole number

height = input("enter your height in m: ")
weight = input("enter your weight in lbs: ")

height_value = float(height)
weight_value = float(weight)

bmi = int(weight_value/(height_value**2))

print(str(bmi))


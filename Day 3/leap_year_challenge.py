# Day 3 - Challenge 3: Leap Year
#
# Write a program that works out whether a given year is a leap year. A
# normal year has 365 days, leap years have 366, with an extra day in
# February.
# This is how you work out whether a particular year is a leap year.
#
# Every year that is evenly divisible by 4 ** except ** 
# every year that is evenly divisible by 100 ** unless **
# the year is also evenly divisible by 400
#
# e.g. The year 2000:
# 2000 / 4 = 500 (Leap)
# 2000 / 100 = 20 ( Not Leap)
# 2000 / 400 = 5 (Leap!)

year = int(input("Which year do you want to check? "))

if year % 400 == 0:
    print(f"The year {year} is a Leap Year.")
elif year % 100 == 0:
    print(f"The {year} is not a Leap Year.")
elif year % 4 == 0:
    print(f"The year {year} is a Leap Year.")
else:
    print(f"The {year} is not a Leap Year.")
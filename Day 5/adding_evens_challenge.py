## Day 5 - Challenge 3: Adding Evens

# Instructions
#
# You are going to write a program that calculates the sum of all even
# numbers from 1 to 100, including 1 and 100
#
# e.g. 2 + 4 + 6 + 8 + 10 ... + 98 + 99 + 100
#
# Important, there should only be 1 print statement in your console output.
# It should just print the final total and not every step of the calculation.
#
# Hint: There are quite a few ways of solving this problem, but you will need
# to use the range() function in any of the solutions.

total = 0
for n in range(2, 101, 2):
    total += n
    
print(f"Total: {total}")


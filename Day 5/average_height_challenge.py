## Day 5 - Challenge 1: Average Height Challenge

# Instructions:
#
# You are going to write a program that calculates the average student 
# height from a list of heights.
#
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# The average height can be calculated by adding all the heights
# together and dividing by the total number of heights.
#
# Important:  do not use the sum() or len() functions

student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
count = 0

for height in student_heights:
    total_height += height
    count += 1
    
average_height = (total_height / count)
average_height = "{:.0f}".format(average_height)

print(f"The average student height is: {average_height}")


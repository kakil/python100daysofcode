## Day 5 - Challenge 2: Average Height Challenge

# Instructions
#
# You are going to write a program that calculates
# the highest score from a List of scores.
#
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#
# Important you are not alled to use the max or min functions.
# The output words must match the example.
# .i.e.: The highest score in the class is: x
#
# Example input: `78 65 89 86 91 64 89`
#
# Example output: The highest score in the class is: 91

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0

for score in student_scores:
    print(score)
    if high_score < score:
        high_score = score

print(f"The highest score in the class is {high_score}")


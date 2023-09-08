# Day 3 - Challenge 5: The Love Calculator
#
# You are going to write a program that tests the compatiblity between
# two people.  We're going to use the super scientific method
# recommended by BuzzFeed.
#
# To work out the love score between two people:
# Take both people's names and check for the number of times the
# letters in the word TRUE occurs.  Then check for the number of
# times the letters in the word LOVE occurs.  Then combine these
# numbers to make a 2 digit number.
# 
# For Love Scores less than 10 or greater than 90, the message should
# be:
# "Your score is x, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is y, you are alright together."
# Otherwise the message will just be their score. e.g.:
# "Your score is z."


print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

score1_counter = 0
score2_counter = 0

# count letters for 'true' in name 1
score1_counter = name1.lower().count("t")
score1_counter += name1.lower().count("r")
score1_counter += name1.lower().count("u")
score1_counter += name1.lower().count("e")

# count letters for 'true' in name 2
score1_counter += name2.lower().count("t")
score1_counter += name2.lower().count("r")
score1_counter += name2.lower().count("u")
score1_counter += name2.lower().count("e")

# count letters for 'love' in name 1
score2_counter = name1.lower().count("l")
score2_counter += name1.lower().count("o")
score2_counter += name1.lower().count("v")
score2_counter += name1.lower().count("e")

# count letters for 'love' in name 2
score2_counter += name2.lower().count("l")
score2_counter += name2.lower().count("o")
score2_counter += name2.lower().count("v")
score2_counter += name2.lower().count("e")

print(f"{str(score1_counter)}")
print(f"{str(score2_counter)}")

total_love_str = str(score1_counter) + str(score2_counter)
total_love_int = int(total_love_str)

if total_love_int < 10 or total_love_int > 90:
    print(f"Your score is {total_love_str}, you go together like coke and mentos.")

elif total_love_int >= 40 and total_love_int <= 50:
    print(f"Your score is {total_love_str}, you are alright together")

else:
    print(f"Your score is {total_love_str}")
    



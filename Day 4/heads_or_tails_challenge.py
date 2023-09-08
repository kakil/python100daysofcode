import random


#
#    You are going to write a virtual coin toss program.  It will
#   randomly tell the user "Heads" or "Tails".
#    
#    Important, the first letter should be capitalised and spelled
#   exactly like the example e.g. Heads, not heads.
#   
#    There are many ways of doing this.  But to practice what we 
#    learned in the last lesson, you should generate a random
#    number, either 0 or 1.  Then use that number to print out
#    Heads or Tails.
#    
#    e.g.
#    1 means Heads
#    0 means Tails
#

print("Heads or Tails Coin Flip")

heads_or_tails = random.randint(0,1)

if heads_or_tails == 0:
    print("Tails")
if heads_or_tails == 1:
        print("Heads")
#print(heads_or_tails)


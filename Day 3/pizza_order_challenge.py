# Day 3 - Challenge 4: Pizza Order
#
# Congratulations, you've got a job at Python Pizza. Your first job is to
# build an automatic pizza order program.
# 
# Based on a user's order, work out their final bill.
#
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: + $2
# Pepperoni for Medium or Large Pizza: + $3
# Extra cheese for any size Pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ? ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
pizza_size = ""

if size.lower() == "s":
    bill = 15
    pizza_size = "Small"
elif size.lower() == "m":
    bill = 20
    pizza_size = "Medium"
elif size.lower() == "l":
    bill = 25
    pizza_size = "Large"
    
if add_pepperoni.lower() == "y":
   if size.lower() == "s":
       bill += 2
   else:
       bill += 3

if extra_cheese.lower() == "y":
    bill += 1
    
print(f"You ordered a {pizza_size} pizza")   

if add_pepperoni.lower() == "y":
    print(f"with extra pepperoni") 

if extra_cheese.lower() == "y":
    print("with extra cheese")

print(f"Your order total: ${bill}") 


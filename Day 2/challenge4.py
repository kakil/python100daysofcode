# Challenge 4: Tip Calculator
#
# If the bill was $150.00, split between 5 people with 12% tip.
# Each person should pay ( 150.00 / 5 ) * 1.12

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = bill * (1 + (tip/100))
per_person_payment = round((total_bill / people),2)
per_person_payment = "{:.2f}".format(per_person_payment)
print(f"Each person should pay: ${per_person_payment}")


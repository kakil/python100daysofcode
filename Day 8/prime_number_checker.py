# Day 8: Prime Number Checker challenge
#
# You need to write a function that checks whether the number
# passed is a prime number or not.
#
# e.g. 2 is a prime number
# a prime number is a number that is only divisible by 1 and itself

def prime_checker(number):
    is_prime = True
    
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            
    if is_prime == True:
        print("It is a prime number.") 
    else:
        print(f"It is not prime.")

n = int(input("Check this number: "))
prime_checker(number=n)


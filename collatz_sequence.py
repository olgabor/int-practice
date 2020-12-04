#-----------------------------------------------------------
# Write a function named collatz() that has one parameter named number. 
# If the number is even, then collatz() should print number // 2 and return this value. 
# If the number is odd, then collatz() should print and return 3 * number + 1. 
# Then write a program that lets the user type in an integer and that keeps calling collatz() on that 
# number until the function returns the value 1.
#The output of this program could look something like this:

#Enter number: 3 10 5 16 8 4 2 1 
# -----------------------------------------------------------

def collatz(number):
    if number % 2 == 0:
        return number // 2 
    elif number % 2 == 1: 
        return 3 * (number + 1)

number = input('type number: ')
value = collatz(int(number)) 

while value !=1: 
    number = input('type number: ')
    value = collatz(int(number))
    print(value)
    

    





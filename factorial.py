#This function returns the factorial of a given number.

def factorial(number):

    result = 1 
    if number < 0: 
        return  ' type the positive integer'
    if number !=  0 :
        result = number  * factorial(number-1)

    return result 

number = input('type number :')     
  
print(factorial(int(number)))
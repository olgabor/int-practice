
# Write a function that returns Nth term of Fibonacci sequense. 

# cover theses use cases 
    #1. Negative number 
    #2. String 
    #3. Float number 

def fib(n):
    fib_storage = {}
    if n < 0:
        return 'Type the number larger than 0'
    if n <1: 
        raise TypeError('Provide a positive integer') 
    if type(n) != int: 
        return 'Type the number larger than 0'

   
    if n in fib_storage: 
        return fib_storage[n]

    if n == 1:
        return 1 
    elif n == 2:
        return 1 
    elif n > 2: 
        val = fib(n-1) + fib(n-2)
    
    fib_storage[n] = val 
    return val

#check if float , string, negative values are covered by function 
print(fib(7))

# print the fibonacci sequence 
# for i in range (1, 15): 
#     print(i, ':', fib(i))

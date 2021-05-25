# Write a function that returns Nth term of Fibonacci sequense.
# cover theses use cases 
    #1. Negative number 
    #2. String 
    #3. Float number 

#dynamic programming approach 
def fib(n):
    memo = {}
    
    #covering edge cases 
    if n < 0:
        return 'Type the number larger than 0'
    if n <1: 
        raise TypeError('Provide a positive integer') ``
    if type(n) != int: 
        return 'Type the number larger than 0'

    if n <= 2: 
        return 1 
    if n in memo: 
        return memo[n]
    else:
        val = fib(n-1) + fib(n-2)
    
    memo[n] = val 
    return val

print(fib(7))

# print the fibonacci sequence 
for i in range (1, 15): 
    print(i, ':', fib(i))

#solution with recursion 
def fib_recursively(n): 
    outcome = 0 

    if n == 0: 
        return  1 
    if n == 1: 
        return 1 
    if n == 2: 
        return 1  
    else:
        outcome += fib_recursively(n-1) + fib_recursively(n-2)

    return outcome

for i in range(10): 
    print( i , ':', fib_recursively(i))

# 
def fib(n): 

    outcome = 0 

    if n == 0: 
        return  1 
    if n == 1: 
        return 1 
    if n == 2: 
        return 1  

    else: 
        outcome +=  fib(n-1) + fib(n -2)

    return outcome

for i in range(10): 
    print( i , ':', fib(i))

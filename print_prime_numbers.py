# Given a positive integer n, find all primes less than n.
def is_prime(number):
    
    for i in (range(2, number)):
        if number % i == 0:
                return False 
    
    return True 


def find_primes(n): 
    res = []
    for number in range(2 , n+1 ): 
        if is_prime(number): 
            res.append(number)

    return res


print(find_primes(14)) # [2, 3, 5, 7, 11, 13]

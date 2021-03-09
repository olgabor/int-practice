# -----------------------------------------------------------

#Count the number of prime numbers less than a non-negative number, n.

#Prime number - a positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
# 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6. 
# ----------------------------------------------------------- 

# Use cases
   # number is > 1 
   # number is divisible by itself only  

#brute force 
def countPrime(n):
    count = 0 
    
    for num in range(n): #0,1,2,3,4,5,6,7,8,9 
        if num > 1:
            for i in range(2, num): #3=>2; #4=>2(break),3; #5=>2,3,4; #6=>2(break),3,4,5; #7=>2,3,4,5,6; #8=>2(break),3,4,5,6,7; #9=>2,3,4,5,6,7 
                if num % i == 0 :
                    break
            else: 
                count += 1 

    return count 

print(countPrime(10)) #4
# print(countPrime(0)) #0
# print(countPrime(1)) #0
# print(countPrime(499979)) #0


import math
#faster solution - Sieve of Eratosthenes Algorithm 
#steps: 
  # 1. Define the boolean array of size n and set all elements to True except 0, 1
  #    isPrime = [False, False, True, True, True] 
  # 2. Start a loop in range from 2 to square root of N 
  #    Loop as i from 2 till sqrt(N) 
  #         if isPrime[i]
  #            Loop over multiples of i as a multiple 
  #                 set all multiples of i as multiple 
  #                 isPrime[Multiple] = False 

def countPrimeFast(n):
    if n < 2:
        return 0
    
    isPrime = [True] * n 
    isPrime[0] = isPrime[1] = False 
    
    for i in range(2, int(math.ceil(math.sqrt(n)))): 
        print('i:' , i , 'int(math.ceil(math.sqrt(n)))', int(math.ceil(math.sqrt(n))), 'n', n  )
        if isPrime[i]:
            print( 'i:', i , isPrime[i])
            for multiples_of_i in range(i*i, n, i):
                print( 'multiples_of_i:', multiples_of_i , 'i:', i )
                isPrime[multiples_of_i] = False 
        
    return sum(isPrime)

# print(countPrimeFast(499979)) #41537 

print(countPrimeFast(10)) #4

gain = [-4, 2, 3,]
print([0, gain])
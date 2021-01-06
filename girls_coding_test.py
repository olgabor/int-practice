#list comprehensions 
print([(x**2) for x in range(0, 10)]) #0**2=>0, 1**2=> 1, 2**2=>4, 3**2=> 9, 
print([(2**x) for x in range(0, 10)]) #2**0=> 1, 2**1=> 2, 2**3=> 64  , 
print([(2**x) for x in range(1, 10)])
print([(x**2) for x in range(1, 10)])

print(2**3)
#fuctorial with recursion 
def factorial(num):

    if num == 1: 
        return num 
    else: 
        return num * (factorial(num -1))

# print(factorial(4))

#count how many numbers are less than each number in the array 
def count(numbers_arr):
    result = [0*x for x in range( 0, len(numbers_arr)) ]

    for i in range(len(numbers_arr)): 
        count = 0 
        for j in range(len(numbers_arr)):
            if i != j and numbers_arr[i] > numbers_arr[j]:
                count += 1 
            
        result[i] = count 

    return result 
# print(count([6,5,4,8]))
# print(count([7,7,7,7]))

#You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

def countcoins(coins, amount):
    min_num = []
         
    for coin in coins: 
        coins_count = 0
        if amount % coin == 0: 
            coins_count  =  amount//coin 

        if amount % coin in coins:
            coins_count =  (amount // coin ) + 1 
        
        if amount % coin not in coins : 
           coins_count -= 1 

        min_num.append(coins_count)

    return min(min_num)

# print(countcoins([1,2,5], 11))            
# print(countcoins([1], 2))            
# print(countcoins([1], 1))            
# print(countcoins([2], 3))    
# print(countcoins([1,2,5], 20))    

#Write a function that reverses a string. The sut string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the sut array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
# sut Format
# Example 1 sut: ["h","e","l","l","o"] Output: ["o","l","l","e","h"]
# Example 2 sut: ["H","a","n","n","a","h"] Output: ["h","a","n","n","a","H"]

def reverseString(s): 

   i = 0 
   j = len(s) -1 

   while i < len(s) -1 and j !=i :
       tmp = s[i]
       s[i] = s[j]
       s[j] = tmp
       i += 1 
       j -=1
    
   return s 
  
print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))
array = [12,6,3,7,13,8] 

#function accepts nummer and computes the sum of numbers from 0 to N 
def sum(n):
    if n < 0: 
        return 0
    else: 
        return n + sum(n -1) 

print(sum(15))

#sum up all numbers in list 
def total(array):
    if len(array) ==1: 
        return array[0] 
    else: 
        return array[0] + total(array[1:])

print(total(array))


#return True/False wheather the item is Palindrome or not 
def is_palindrome(word):
    if len(word) == 0 or len(word) == 1: 
        return True 

    if word[0] != word[-1]:
        return False 
        
    else: 
        return is_palindrome(word[1:-1])
    

print(is_palindrome("tacocat"))

#Write a recursive function to count the number of items in a list.
def countNumbers(array):
    count = 1
    if len(array) == 1: 
        return count 
    else: 
        return count + countNumbers(array[1:])


print(countNumbers(array))

#Find the maximum number in a list. 
def findMax(array):
    if len(array) == 1 : 
        return array[0]
    if array[1] <  array[0]:
        return array[0]
    else:
        return findMax(array[1:]) 

print(findMax(array))




#function accepts nummer and computes the sum of numbers from 0 to N 
def sum(n):
    if n < 0: 
        return 0
    else: 
        return n + sum(n -1) 

print(sum(15))

def is_palindrome(word):
    if len(word) == 0 or len(word) == 1: 
        return True 

    if word[0] != word[-1]:
        return False 
        
    else: 
        return is_palindrome(word[1:-1])
    

print(is_palindrome("tacocat"))
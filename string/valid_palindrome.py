# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

def validPalindrome(str):

    start, end = 0, len(str) -1 

    while start <= end :

        while str[start].isalnum() != True:
            print(str[start])
            start += 1
            
        while str[end].isalnum() != True: 
            end -= 1   
           
        if str[start].lower() != str[end].lower():
            return False 

        start += 1 
        end -= 1

    return True  
    
   
print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))


def validPalindromeRecursion(str):
    
    if len(str) == 0: 
        return True 

    if str[0] != str[-1]: 
        return False 
    
    else:
        return validPalindromeRecursion(str[1:-1])
    
    return True 

print(validPalindromeRecursion("tacocat"))
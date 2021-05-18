
# Given two strings s and t , write a function to determine if t is an anagram of s.
# Input: s = "anagram", t = "nagaram"
# Output: true

#SOLUTION using frequency counting technique  
    # have 2 dictionary and save values from both strings to dictionaries 
    # if all d2 = d2 return True , else False 
#time complexity 
    # we are looping two times over the strings, therefore time complexity is O(n) 
    
def isAnagram(s, t):
    d1 = {}
    d2 = {}
    
    for i in s: 
        d1.setdefault(i, 0)
        d1[i] += 1 
    
    for i in t: 
        d2.setdefault(i,0)
        d2[i] += 1 
    
    if d1!= d2: 
        return False 
    
    return True 


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))

#SOLUTION with string sorting 
    # save sorted strings in 2 variables 
    # return bulean value whether the two variables are equal or not 
#time complexity 
    # built in sorted() function is using merge sort algorithm, 
    # therefore the time complexity is O(log n) for both strings  
def isAnagramSorted(s,t): 
    sotred_s = sorted(s)
    sotred_t = sorted(t)

    return sotred_s == sotred_t

print(isAnagramSorted("anagram", "nagaram"))
print(isAnagramSorted("rat", "car"))
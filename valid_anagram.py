
# Given two strings s and t , write a function to determine if t is an anagram of s.
# Input: s = "anagram", t = "nagaram"
# Output: true

# have 2 dictionary and save values from both strings to dictionaries 
# if all d2 = d2 return True , else False 

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

def isAnagramSorted(s,t): 
    sotred_s = sorted(s)
    sotred_t = sorted(t)

    return sotred_s == sotred_t

print(isAnagramSorted("anagram", "nagaram"))
print(isAnagramSorted("rat", "car"))
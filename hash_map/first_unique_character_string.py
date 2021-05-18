# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:
# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.
 
def fist_unique_characher(s):
    
    if len(s) < 1: 
        return -1 

    m = {}
    for i in range(len(s)): 
        m.setdefault(s[i], 0)
        m[s[i]] += 1 

    for i in range(len(s)):
        if m[s[i]] == 1: 
            return i  

    return -1  


print(fist_unique_characher("leetcode"))# 0 
print(fist_unique_characher("loveleetcode")) #2
print(fist_unique_characher("")) #-1 
print(fist_unique_characher("cc")) #-1 
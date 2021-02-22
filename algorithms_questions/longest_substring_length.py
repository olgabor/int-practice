#Given a string s, find the length of the longest substring without repeating characters.

#sliding window 
def lengthOfLongestSubstring(s):
    m = {} 
    left = 0 
    right = 0 
    ans = 0 
    n = len(s)
    
    while (left < n and right< n): 
        el = s[right]
        if el in m:
            left = max(left, m[el]+1)

        m[el] = right 

        ans = max(ans, right - left +1 )
        right+= 1 
    
    return ans 

# print(lengthOfLongestSubstring('abcdababc'))

#Brute force solution 
#space complexity = O(n), time complexity O(n2)
def bruteforce(s):
    ans = 0 
    temp = []
    for i in s: 
        if i in temp:
            temp = []
        else:
            temp.append(i)
        
        ans= (max(ans, len(temp))) 

    return ans

print(bruteforce('abcdababc'))
print(bruteforce('abcabcbb'))
print(bruteforce('bbbbb'))
print(bruteforce('pwwkew'))
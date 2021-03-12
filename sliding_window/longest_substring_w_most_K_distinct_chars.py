# Given a string s and an integer k, 
# return the length of the longest substring of s that contains at most k distinct characters.

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.


def longest_substr_w_k_distinct_chars(s, k):
    m = {} 
    left = 0 
    res = 0 
    for i in range(len(s)):
        m.setdefault(s[i], 0)
        m[s[i]] = i

        if len(m) == k + 1: 
             # delete the leftmost character
            del_idx = min(m.values())
            del m[s[del_idx]]
            # move left pointer of the slidewindow
            left = del_idx + 1

        res = max((i +1 )- left, res)

    return res

print(longest_substr_w_k_distinct_chars("aa",1)) #2
print(longest_substr_w_k_distinct_chars("eceba",2)) #3
print(longest_substr_w_k_distinct_chars("ab", 1)) #1 
print(longest_substr_w_k_distinct_chars("loveleetcode",4)) #
print(longest_substr_w_k_distinct_chars("aa", 2)) #2
print(longest_substr_w_k_distinct_chars("bacc", 2)) #3
print(longest_substr_w_k_distinct_chars("abaccc", 2)) #3
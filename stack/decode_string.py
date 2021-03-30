# 394. Decode String
# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

#steps: 
 # loop through elements 
    # if elem == number save it to r 
    # if elem is [ add it to stack 
        # if elem is ] close the stack 
        # else: 
            #if elem is alpha save it to tmp 
        #while stack: 
            # for i in range(r): 
                # res += tmp 
    # else: 
        # save elem to res 


def decode_string(s): 
    res = ''
    stack = []
    r = 0 
    open_bracket = '['
    closing_bracket = ']'
    
    tmp = ''

    for elem in s:
        if elem.isnumeric(): 
            r = int(elem)
        if elem == '[':
            stack.append(elem) 
        
        if elem.isalpha(): 
            tmp += elem 

            print( 'line 57',tmp , stack)
        if elem == ']':
            stack.pop()
            # tmp = ''
        while not stack and r and tmp:
            res += tmp * r 
            tmp = ''
            r = 0
        else: 
            res += tmp 

    return res
            
print(decode_string("3[a]2[bc]")) #"aaabcbc"
print(decode_string("3[a2[c]]")) # "accaccacc"
print(decode_string("2[abc]3[cd]ef")) # "abcabccdcdcdef"

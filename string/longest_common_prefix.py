# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def largest_common_prefix(strs):
    if len(strs) == 1: 
        return strs[0]
        
    if not strs: 
        return ''

    for i in range(len(strs[0])):   # iterate over indexes of the first word in list 

        for string in strs:         # iterate over each letter in string 
            if i >= len(string) or string[i] != strs[0][i]: # if index is larger then lenght of word 
                                                            # & letter by index i != letter by same index in first word 
                return strs[0][:i]                          # return prefix 
    
    return strs[0]

print(largest_common_prefix(["flower","flow","flight"]))
print(largest_common_prefix(["flower","flower","flower","flower"]))
print(largest_common_prefix(["dog","racecar","car"]))
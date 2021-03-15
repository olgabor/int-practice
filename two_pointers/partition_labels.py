# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:

# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

s = "ababcbacadefegdehijhklij" 

def partition_labels(s): 
    output = []
    m = {char:indx for  indx, char in enumerate(s)}
    # m = {}
    for  index , char in  enumerate(s): 
        print(char, index)
    # for i in range(len(s)): 
    #     m.setdefault(s[i], 0)
    #     m[s[i]] = i 

    start = 0 
    end = 0

    i = 0 
    while i <= len(s) -1: 

        end = max(end, m[s[i]]) 

        if i == end:
            output.append(end - start +1)
            start = i + 1 

        i += 1 
    return output

print(partition_labels(s))
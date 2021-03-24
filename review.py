# 49. Group Anagrams

# Share
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters 
# of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

strs = ["eat","tea","tan","ate","nat","bat"]

def group_anagrams(str): 
     
     # when  values are sorted we can compare them and group together 
     # create empty dictionary to store the values of anagrams  
     # iterate over the list and store the values as a keys 
        # if a sorted version not in dictionary 
            # save the current value as key: value 
        # else: 
            # apeend current i to dictionary key meaning the key already exists 
    # return dicionary values d.values()

    d = {}

    for i in strs:
        if ''.join(sorted(i)) not in d :
            d[''.join(sorted(i))] = [i]
        else: 
            d[''.join(sorted(i))].append(i)

    return d.values()
    

print(group_anagrams(str))
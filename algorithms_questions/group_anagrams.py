#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


def groupAnagram(strs): 
    
    anagr = {}

    for item in strs: 

        a = ''.join(sorted(item))
        if a not in anagr: 
            anagr[a] = [item]
        else:
            anagr[a].append(item)
            
    return anagr.values() 
    

print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))


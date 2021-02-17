#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


def groupAnagram(strs): 
    
    anagr = {}
    answ = []

    for item in strs: 
        a = ''.join(sorted(item))

        if a not in anagr:
            anagr[a] = [item]
        else:
            anagr[a].append(item)

    # write each value of dictionary in list 
    # for p in anagr.values():
    #     print(p)
    #     answ.append(p)
    
    # return answ # will return a list 

    return anagr.values() 
    

print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))
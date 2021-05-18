# Verifying an Alien Dictionary

# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 
def verify_alien_dict(words, order):


    d = {char:freq for freq, char in enumerate(order)}

    for i in range(len(words) -1): 
        word1= words[i]
        word2= words[i+1 ]


    for i in range(min(len(word1), len(word2))): 
         if word1[i] != word2[i]: 
             print(i, d[word1[i]],d[word2[i]] , word1[i] , word2[i])
             if d[word1[i]] > d[word2[i]]:
                 print(d[word1[i]] , d[word2[i]])
                 return False  
             break
             
         else: 
             if len(word1) > len(word2):
                return False
    return True 
   
     
    # order_index = {c: i for i, c in enumerate(order)}

    # for i in range(len(words) - 1):
    #     word1 = words[i]
    #     word2 = words[i+1]

    #     # Find the first difference word1[k] != word2[k].
    #     for k in range(min(len(word1), len(word2))):
    #         # If they compare badly, it's not sorted.
    #         if word1[k] != word2[k]:
    #             if order_index[word1[k]] > order_index[word2[k]]:
    #                 return False
    #             break
    #     else:
    #         # If we didn't find a first difference, the
    #         # words are like ("app", "apple").
    #         if len(word1) > len(word2):
    #             return False

        # return True
print(verify_alien_dict(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(verify_alien_dict(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
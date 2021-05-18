# This function returns an array of all combinations of the given letters
# Input type: array of single characters
# For example, letterCombinations(["a","b","c"]) would return the following
# ["a","b","c","ab","ac","ba","bc","ca","cb","abc","acb","bac","bca","cab","cba"]

def letterCombinations(l = ["a","b","c"]):
    k = [] 
    for i in range(len(l) ):
        count = len(l)-1 
        if l[i] not in k:
            k.append(l[i])
        else: 
            m = k[i] + k[i-1]
            k.append(m)
            count -= 1 
    # print(len(l))
    return k , count 

print(letterCombinations(l = ["a","b","c"]))
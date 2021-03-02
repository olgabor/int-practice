import timeit
start = timeit.default_timer() 

wordList = ['APPLE', 'PLEAS', 'PLEASE']
keyPad =  ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY']

#expected output = [0, 1, 3, 2, 0 ]
def findSubstring(wordList, keyPad): 

    hashWord = {}
    hasKeyPad = {}
    res = []
    
    for key in keyPad: 
        hasKeyPad[key] = {}
        w = 0 
        for i in range(len(key)): 
            if (hasKeyPad[key].get(key[i]) is None):
                hasKeyPad[key][key[i]] = 0  
            hasKeyPad[key][key[i]] += 1 

        for word in wordList:
            count = 0 
            hashWord[word] = {}
            for i in range(len(word)): 
                if (hashWord[word].get(word[i]) is None): 
                    hashWord[word][word[i]] = 0 
                hashWord[word][word[i]] += 1 

                if (hasKeyPad[key].get(word[i]) is None): 
                    hasKeyPad[key][word[i]] = 0
 
                if hasKeyPad[key][word[i]] <= hashWord[word][word[i]] and hasKeyPad[key][word[i]] != 0:
                    count += 1 
                
                if count == len(word) and key[0] in word:
                    w += 1 

        res.append(w)
    return res 

print(findSubstring(wordList, keyPad))

stop = timeit.default_timer()
print('Time: ', stop - start)
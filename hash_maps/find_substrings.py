import timeit
start = timeit.default_timer()

wordList = ['APPLE', 'PLEAS', 'PLEASE']
keyPad =  ['AELWXYZ', 'AELPXYZ', 'AELPSXY', 'SAELPRT', 'XAEBKSY']

#expected output = [0, 1, 3, 2, 0 ]

def findSubstring(word, keyPad): 
    
    # define two empty dictionarires 
        # hashWord 
        # hashKeypad 
    hashWord = {}
    hasKeyPad = {}

    #first for loop: fill out hash map for keypad  
    for i in range(0, len(keyPad)): 
        hasKeyPad.setdefault(keyPad[i], 0)
        hasKeyPad[keyPad[i]] += 1 
    # print(hasKeyPad)
        
    # defiene the count - this will be used to store the matches found in both inputs 
    count = 0 
    
    #loop through the given word and fill out the hashWord 
    for i in range(len(word)): 
        hashWord.setdefault(word[i], 0)
        hashWord[word[i]] += 1 
        # print(hashWord)
        # print(hasKeyPad.get(word[i]))
        if (hasKeyPad.get(word[i]) is None): 
            hasKeyPad[word[i]] = 0

       # if word letter apears in keypad increase count 
        # print(hasKeyPad[word[i]], hashWord[word[i]], hashWord[word[i]] <= hasKeyPad[word[i]]  )
        if hasKeyPad[word[i]] <= hashWord[word[i]] and hasKeyPad[word[i]] != 0:
        # if hasKeyPad[word[i]] <= hashWord[word[i]] :
            print( word, word[i], hasKeyPad[word[i]] , hashWord[word[i]], hasKeyPad[word[i]] <= hashWord[word[i]] and hasKeyPad[word[i]] != 0)
        # if  hashWord[word[i]] >= hasKeyPad[word[i]]:
            # print(hashWord[word[i]] , hasKeyPad[word[i]])
            count += 1 
        
        if count == len(word): 
            # print(word)
            return True 
    return False

res = [] * len(keyPad)

for keypad in keyPad: 
    count = 0
    for word in wordList :  
        if findSubstring(word, keypad) == True: 
            count += 1 
    res.append(count)       
    print(res)

stop = timeit.default_timer()

print('Time: ', stop - start)
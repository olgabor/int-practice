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

    # # first for loop: fill out hash map for keypad  
    # for key in keyPad: 
    #     hasKeyPad[key] = {}
    #     for i in range(len(key)): 
    #         hasKeyPad[key].setdefault(key[i], 0)
    #         hasKeyPad[key][key[i]] += 1 


    # # #loop through the given word and fill out the hashWord 
    # for word in wordList:
    #     hashWord[word] = {}
    #     for i in range(len(word)): 
    #         hashWord[word].setdefault(word[i], 0)
    #         hashWord[word][word[i]] += 1 
    
    # for key in keyPad: 
    #     w = 0
    #     for word in wordList: 
    #         count = 0 
    #         for  i in range(len(word)): 
    #             if (hasKeyPad[key].get(word[i]) is None): 
    #                 hasKeyPad[key][word[i]] = 0
 
    #             if hasKeyPad[key][word[i]] <= hashWord[word][word[i]] and hasKeyPad[key][word[i]] != 0:
    #                 count += 1 
                
    #             if count == len(word):
    #                 w += 1 
    #     res.append(w)
    # return res 
      

print(findSubstring(wordList, keyPad))

stop = timeit.default_timer()
print('Time: ', stop - start)

# # print(3%5 )

# def fizzBuzz(n):
#     # Write your code here
#     for i in range(1,n +1 ): 
#         if i % 3 == 0 and i % 5 == 0: 
#             print('FizzBuzz')
#         elif i % 3 == 0: 
#             print('Fizz')
#         elif i % 5 == 0 : 
#             print('Buzz')
#         else:
#            print(i)
        
# print(fizzBuzz(15))

# 1
# 2
# FizzBuzz
# 4
# Buzz
# FizzBuzz
# 7
# 8
# FizzBuzz
# Buzz
# 11
# FizzBuzz
# 13
# 14
# FizzBuzz
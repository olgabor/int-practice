
words = ['man', 'woman', 'manhandle', 'handle', 'race', 'drag', 'car', 'racecar', 'computer', 'bag', 'dragon', 'manbag']

def concatenate_words(words): 

    def dynamic_program(word): 
        if word in memo: 
            return True 

        for i in range(min_lenght, len(word) - min_lenght +1):
            if word[:i] in memo and dynamic_program(word[i:]): 
                return True 
        
        return False
    
    output = []
    memo= set()
    words.sort(key=len)
    min_lenght = (max(len(words[0]), 1))

    for word in words: 
        if dynamic_program(word): 
            output.append(word)
        memo.add(word)

    return output 


print(concatenate_words(words))

    

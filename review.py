def two_sum(digits, target):

    m = {}

    #iterate over the array and write down the values to dict 
    # if the differnce of target and each value exists in m return the key 
    for i in range(len(digits)):
        diff = target - digits[i]

        if diff in m: 
            return m[diff], i 
        else: 
            m[digits[i]] = i  
    
print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
# -----------------------------------------------------------
#Given an array of integers nums.
#A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#Return the number of good pairs. 
# -----------------------------------------------------------

def numberIdenticalPairs(nums): 
    pairs = 0 
    for i in range(len(nums)): 
        for j in range(i +1 , len(nums)): 
            if nums[i] == nums[j] and i < j: 
                pairs+= 1 
        
    
    return pairs 

def fastersolution(nums):
    pairs = 0 
    num_dict = {}
    for num in nums: 
        num_dict.setdefault(num, 0)
        if num in num_dict: 
            pairs += num_dict[num]
        num_dict[num] += 1 

    return pairs

print(numberIdenticalPairs([1,2,3,1,1,3]))
print(numberIdenticalPairs([1,1,1,1]))
print(numberIdenticalPairs([1,2,3]))

print(fastersolution([1,1,1,1]))
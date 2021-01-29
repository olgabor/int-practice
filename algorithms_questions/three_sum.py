# Given an array nums of n integers, are there elements a, b, c in 
# nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.
 
# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


# brute force solution is to loop over the array three times and add the values 


def threeSum(nums):

    d = {}
    i = 0 
    
    # if len(nums) < 3:
    #     return []
    # for i in range(len(nums) -1): 
    while i < len(nums) -1: 
        diff = 0  - (nums[i] + nums[i+1])
        print(diff)
        # if diff not in d and diff in nums:  
        if diff not in d :  
            d[i] = [nums[i] , nums[i+1] , diff] 
            del nums[i] , nums[i+1] 
        elif diff in d: 
           return d[i]
        # elif diff not in d:
        #     return []
        i += 1 

    return list(d.values())
    

# print(threeSum([-1,0,1,2,-1,-4]))
# # print(threeSum([0]))
# print(threeSum([0, 0, 0 ]))
# print(threeSum([0,1,1]))

# print(threeSum([0, 0, 0, 0]))
print(threeSum([-2, 0, 1, 1, 2]))


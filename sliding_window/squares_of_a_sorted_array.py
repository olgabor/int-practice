# Given an integer array nums sorted in non-decreasing order, return an array of the 
# squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

nums = [-4,-1,0,3,10]
nums1 = [-7,-3,2,3,11]
nums2 = [1]
nums3 = [-1,1]

#Brute Force - time comlexity is O(n) + O(logn)
# loop through the array and replace each item with its squared version 
#return sorted array 

# for i in range(len(nums)):
#     nums[i] = nums[i] * nums[i]
# print(sorted(nums)) 
def squeares_of_sorted_array(nums): 
    output = [0] * len(nums)

    if len(nums) == 1: 
        output[0] = nums[0] * nums[0]
        return output 

    l = 0
    r = len(nums) -1 

    for i in range((len(nums) -1), -1, -1 ):        
        if abs(nums[l]) < abs(nums[r]): 
            output[i] =  nums[r] * nums[r]
            r -= 1 

        elif abs(nums[l]) > abs(nums[r]): 
            output[i] = nums[l] * nums[l]
            l += 1 

        elif abs(nums[l]) == abs(nums[r]):
            output[i] = nums[l] * nums[l] 
            l += 1
        
    return output  
                      
print(squeares_of_sorted_array(nums))
print(squeares_of_sorted_array(nums1))
print(squeares_of_sorted_array(nums2))
print(squeares_of_sorted_array(nums3))


def squeares_of_sorted_array_v2(nums): 
    
    output = [0] * len(nums)

    if len(nums) == 1: 
        output[0] = nums[0] * nums[0]
        return output 
        
    l = 0
    r = len(nums) -1 
    insert = len(nums) -1 

    while insert > 0 : 
        if  abs(nums[l]) < abs(nums[r]): 
            output[insert] = nums[r] * nums[r]
            r -= 1 
            insert -= 1

        if  abs(nums[l]) > abs(nums[r]): 
            output[insert] = nums[l] * nums[l]
            l += 1 
            insert -= 1 
        
        if abs(nums[l]) == abs(nums[r]) and l != r:
            output[insert] = nums[r] * nums[r] 
            output[insert-1] = nums[l] * nums[l] 
            r -= 1 
            l += 1 
            insert -= 2

        if l == r : 
            output[insert] = nums[l] * nums[l]  
        
    return output  

print(squeares_of_sorted_array_v2(nums))
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#Example 1:

nums = [2,7,11,15]
nums1 = [11,15, 2,7]
nums2 = [2, 11,15,7]
target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target): 
    output = []
    for i in range(len(nums)):
        if nums[i] < target: 

    
print(two_sum(nums, target))
print(two_sum(nums1, target))
print(two_sum(nums2, target))

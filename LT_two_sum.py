#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
#Example 1:

nums = [2, 7, 11, 15]
nums1 = [3, 2, 4] 
nums2 = [3, 3]
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target): 
    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            if nums[i] + nums[j] == target:
                return i , j 
       
    return 'no numbers add up to target'
    
# print(two_sum(nums, 9))
# print(two_sum(nums1, 6))
# print(two_sum(nums2, 6))

#hash maps 
def twoSumHashmap(nums, target): 

    m = {}
    for i in range(len(nums)):
        
        diff = target - nums[i]  

        if diff in m:
            return m[diff], i
        else: 
            m[nums[i]] = i  
 
print(twoSumHashmap(nums, 9))
print(twoSumHashmap(nums1, 6))
print(twoSumHashmap(nums2, 6))
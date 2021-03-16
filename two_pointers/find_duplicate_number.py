# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [1,1]
# Output: 1

# Example 4:
# Input: nums = [1,1,2]
# Output: 1

def find_duplicate(nums):

    nums.sort()

    for i in range(len(nums) -1): 
        if nums[i] == nums[i+1]: 
           return nums[i]

print(find_duplicate([1,3,4,2,2]))
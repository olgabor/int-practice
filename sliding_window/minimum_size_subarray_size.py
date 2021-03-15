# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
# of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

def minimal_length_of_contiguous_subarray(nums, target): 
    output = float('inf')
    if sum(nums) < target:
        return 0 
    if target in nums: 
        return 1 

    left = 0 
    current_s = 0 
    for i in range( len(nums)): 
        current_s += nums[i] 
        while current_s >= target: 
            output = min(output, (i +1 - left))
            current_s -= nums[left]
            left += 1 
      
    return output
print(minimal_length_of_contiguous_subarray([2,3,1,2,4,3], 7)) #2+3+1+2= 8 , 3+1+2+4 = 10 , 1+2+4 = 7, 2+4+3= 9, 4+3=7 
print(minimal_length_of_contiguous_subarray([1,4,4], 4))
print(minimal_length_of_contiguous_subarray([1,1,1,1,1,1,1,1], 11))
print(minimal_length_of_contiguous_subarray([1,2,3,4,5], 11)) # 1+2+3+4+5= 15 , 2+3+4+5= 14 , 3+4+5= 12 
print(minimal_length_of_contiguous_subarray([1,2,3,4,5], 15))
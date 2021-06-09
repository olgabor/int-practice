#Given an integer array nums, find the contiguous subarray
#  (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(nums):
         
    curr_sum = max_sum = nums[0]

    for i in range(len(nums)):
        curr_sum = nums[i]
        max_sum = max(curr_sum, max_sum)

        if curr_sum > 0: 
            for j in range(i+1, len(nums)):
                curr_sum += nums[j]

                if curr_sum > max_sum: 
                    max_sum = curr_sum 
        
    return max_sum 

    
print(maxSubArray([-2, 1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([-2,1]))
print(maxSubArray([1]))
print(maxSubArray([-2,-1]))
print(maxSubArray([0,3,-1]))
print(maxSubArray([-1,0,-2]))


def maxSubArrayBruteforce(nums):

    curr_sum = max_sum = nums[0]

    for i in range(1, len(nums)):

        curr_sum = max(nums[i], (curr_sum +  nums[i]))
        max_sum = max(curr_sum, max_sum)
        
    return max_sum 

print(maxSubArrayBruteforce([-2, 1,-3,4,-1,2,1,-5,4]))


def maxSubArraySlidingWindow(nums):
	    n = len(nums)
	    max_sum = nums[0]
	    for i in range(1, n):
	        if nums[i - 1] > 0:
	            nums[i] += nums[i - 1]
	        max_sum = max(nums[i], max_sum)
	
	    return max_sum

print(maxSubArraySlidingWindow([-2, 1,-3,4,-1,2,1,-5,4]))
print(maxSubArraySlidingWindow([-1]))

# Given an array of positive numbers and a positive number ‘k,’ 
# find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# use the sliding window technique 
  # start from defining max_Sum = 0 to compare it with curr_sum 
  # define curr_sum = should be a sum of items in range provided by target 

  # define the pointer i = 0 - use this pointer to iterate over the list and increase it by one for each iteration 
  # start the while loop ( while i < len(nums) -3 )
          # within the loop new curr_sum should be calculated every time the pointer is increasing 
          # curr_sum = curr_sum - nums[i] + nums[i+3]
          # find max by - max_sum = max(curr_sum, max_sum) 
          # return max_sum 

def maxSumSubArray(nums, k): 
    
    max_sum = 0 
    curr_sum = 0 
    for i in range(k): 
        curr_sum += nums[i]


    i = 0 
    while i < (len(nums) -3): 
        curr_sum = (curr_sum - nums[i]) + nums[i + k]
        max_sum = max(curr_sum, max_sum)
        i += 1 

    return max_sum 
print(maxSumSubArray([2, 1, 5, 1, 3, 2], 3))

def max_sum_sub_array_brute_force(nums, k): 
    max_sum = 0 

 
    for i in range(len(nums)): 
        cur_sum = 0 
        for j in range(i, k +1 ): 
            cur_sum += nums[j]
            max_sum = max(cur_sum , max_sum)
    
    return max_sum


print(max_sum_sub_array_brute_force([2, 1, 5, 1, 3, 2], 3))
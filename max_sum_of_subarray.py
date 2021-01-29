# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

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
    for i in range(3): 
        curr_sum += nums[i]

    i = 0 
    while i < (len(nums) -3): 

        curr_sum = (curr_sum - nums[i]) + nums[i +k ]
        max_sum = max(curr_sum, max_sum)
        
        i += 1 

    return max_sum 

print(maxSumSubArray([2, 1, 5, 1, 3, 2], 3))
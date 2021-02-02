# Given an array of positive numbers and a positive number ‘S,’ 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0 if no such subarray exists.

# Example 1:
# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

#STEPS: 
# define the veriable l = 0, which should modified and returned as functions output 
# define the curr_sum = nums[0], this variable will be used to compare with given S 
    # if curr_sum greater or == S ==> need to find number of elements this sum consists of 

    # if curr_sum less than S => add one more element to it and check again 
        # if curr_sum greater or == S ==> need to find number of elements this sum consists of 
    
    # return the smallest l 
        #l = min(l, len(curr_sum))


import math 

def smallest_subarray_with_given_sum(arr,s):
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]  # add the next element
        #shrink the window as small as possible until the 'window_sum' is smaller than 's'
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
  
    return min_length

print(smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7 ))


def smallestSubarray(nums, s):
    pass 

print(smallestSubarray([2, 1, 5, 2, 3, 2], 7 ))
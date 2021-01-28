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
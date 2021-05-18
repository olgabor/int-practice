#find maximum sum of contiguous array of size 3 

def max_sum(nums):
    max_sum = 0 
    l = 1 
    r = len(nums) -1 
    cur_window = (nums[l-1] + nums[l] + nums[l+1]) 
    
    while l<=r and  l+3 < r:
        cur_window = cur_window + nums[l+3]  - nums[l-1]
        max_sum = max(cur_window, max_sum)
        l += 1 

    return max_sum

print(max_sum([4, 2, 1, 7, 8, 2, 8, 1, 0]))
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

#Brute force solution: 
 # loop through in range of a given K 
 # assign the last digit of the array to previous variable 
    # Loop through the array in len(nums)
     # switch the values of previous and Arr[j]

def rotateWith_slicing(arr, k):

    for i in range(k):
        previous = arr[-1]
        for j in range(len(arr)):
            arr[j] , previous  =  previous, arr[j] 
    
    return arr 

print(rotateWith_slicing([1,2,3,4,5,6,7], 3))
print(rotateWith_slicing([-1,-100,3,99], 2))



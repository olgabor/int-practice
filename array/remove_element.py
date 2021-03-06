# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.


def removeElement(nums, value):
    i = 0 
    j = len(nums) -1  
      
    while i <= j :

        if nums[i] == value:
            del nums[i]
            j = len(nums) - 1 
        else: 
            i += 1 
    
    return len(nums)

def removeElementSorted(nums, value):
    for n in sorted(nums):
        if n == value:
            nums.remove(n)
        
    return len(nums)

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))
print(removeElementSorted([0,1,2,2,3,0,4,2], 2))

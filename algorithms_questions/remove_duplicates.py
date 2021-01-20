#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):

    l = len(nums) -1 
    i = 0
    while i < l: 

        if nums[i] ==  nums[i + 1]:
            del nums[i] 
            l = len(nums)-1 
        else: 
            i += 1 
        
    return len(nums), nums

print(removeDuplicates([1,1,2]))
print(removeDuplicates([1,1,2,2,3,4,4]))
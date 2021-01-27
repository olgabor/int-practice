# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

def insertPosition(nums, target):

    pointer = 1 
    index = 0 
    if target in nums: 
        return nums.index(target)
    
    while pointer <= len(nums): 

        if target - pointer in nums:
            index =  nums.index(target - pointer) + 1 
            return index 
            
        if target + pointer  in nums: 
            index =  nums.index(target + pointer)
            return index 
        else: 
            pointer += 1 

        
# print(insertPosition([1,2,5,6], 5 ))
# print(insertPosition([1,2,5,6], 3 ))
# print(insertPosition([1,3,5,6], 2))
# print(insertPosition([1,3,5,6], 0))
# print(insertPosition([2,3,4,8,10], 0))
# print(insertPosition([2,3,4,7,8,9], 11))
# print(insertPosition([3,6,7,8,10], 5))
# print(insertPosition([2, 5], 1))
# print(insertPosition([5, 6, 8, 10], 1)) 


def insertPostionBinary(nums, target): 

    right, left = 0, len(nums) - 1 

    while right < left: 
        
        mid = left - right // 2 
        
        if nums[mid] == target: 
            return mid 
        if nums[mid] > target: 
            left -= 1 
        if nums[mid] < target: 
            right += 1 
   
    return left 

print(insertPostionBinary([5, 6, 8, 10], 1)) 
print(insertPostionBinary([1,2,5,6], 3))
print(insertPostionBinary([1,2,5,6], 5 ))
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

def insertPosition(nums, target):
    # if number in list 
         #return index
    pointer = 1 
    index = 0 
    # index = nums.index(target) 
    # if target == 0 and target not in nums: 
    #     return 0 
    if target in nums: 
        return nums.index(target)
    
    while pointer <= len(nums): 

        if target - pointer in nums:
            index =  nums.index(target - pointer) + 1 
            # print('index line 17', index, pointer) 
            return index 
            
        if target + pointer  in nums: 
            index =  nums.index(target + pointer)
            # print('index line 22', index) 
            return index 
        else: 
            pointer += 1 

    # return index 
    # print('pointer:', pointer)
    # return  nums.index(target - pointer) + 1 

        
    # print(index) 

    # if number not in list: 
        # find the value that is smaller by one and larger by one 
        # if both exist 
            #return smaller value index +1 

        
# print(insertPosition([1,2,5,6], 5 ))
# print(insertPosition([1,2,5,6], 3 ))
# print(insertPosition([1,3,5,6], 2))
print(insertPosition([1,3,5,6], 0))
# print(insertPosition([2,3,4,8,10], 0))
print(insertPosition([2,3,4,7,8,9], 11))
print(insertPosition([3,6,7,8,10], 5))
print(insertPosition([2, 5], 1))
print(insertPosition([5, 6, 8, 10], 1)) 
# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].



#Use cases : 
    #number is lover target 
    #number is greated target 
    #number == target: 
        #if index == 0 ==> write down the mid 
        #if nums[mid +1] == target 
def searchRange(nums, target):
    position = []

    l = 0 
    r = len(nums) - 1 
   

    while l < r :

        mid = (r - l) // 2
        print(mid)
        if nums[mid] == target:
            print('WOA')
            l +=1 
            if mid == 0:
                position.append(mid) 
            if nums[mid+1] == target:
                position.append(mid +1)

        if nums[mid] > target:
            print(nums[mid] , mid) 
            l += 1
        if nums[mid] < target:  
            l -= 1 
       
    
    return position 


# print(searchRange([5,7,7,8,8,10] , 8))
# print(searchRange([5,7,7,8,8,10] , 6))

print(2//2)
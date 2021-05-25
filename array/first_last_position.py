# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

#Use cases : 
    #number is less than target 
    #number is greated than target 
    #number == target: 
        #if index == 0 ==> remember the mid 
        #if nums[mid+1] == target 

def search_range(nums, target):
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

# print(search_range([5,7,7,8,8,10] , 8))
# print(search_range([5,7,7,8,8,10] , 6))

def search_range1(nums, target):
    result = []

    left = 0 
    right = len(nums) -1 
    print(right)
    while left < right:

        mid = (left +right) // 2
        if nums[mid] > target:
            right = mid
        if nums[mid] < target:
            left = mid

        # if nums[mid] == target:
        #     result.append(mid)
        #     left = mid + 1 
        if nums[mid] == target:
            if nums[mid+1] != target:
                result.append(mid)
                right = mid
            if  nums[mid-1] != target:
                result.append(mid)
                left  = mid
            if mid == 1 and nums[mid -1] != target:
                return result

    return result 

print( search_range1([5,7,7,8,8,10] , 8)) 
# print( search_range1([5,7,7,8,8,8,10] , 8)) 
# print(search_range1([5,7,7,8,8,10] , 7))
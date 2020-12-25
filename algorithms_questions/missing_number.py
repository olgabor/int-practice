#Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

#Follow up: Could you implement a solution using only O(1) 
# extra space complexity and O(n) runtime complexity?

#Gauss formula to get the sum (n*(n+1) /2) )

def missingNumberFast(nums):
    n = len(nums)
    nums_list = n*(n+1)/2
    
    return int(nums_list) - sum(nums) 

print(missingNumberFast([9,6,4,2,3,5,7,0,1]))
print(missingNumberFast([3, 0, 1]))
print(missingNumberFast([0]))
print(missingNumberFast([1]))
print(missingNumberFast([1,2]))
print(missingNumberFast([1,2,3]))
print(missingNumberFast([0,1]))

#brute force 
def missingNumber(nums):

    for num in range(len(nums) +1 ):
        if num not in nums: 
            return num

# print(missingNumber([3, 0, 1]))
# print(missingNumber([0, 1]))
# print(missingNumber([0]))
# print(missingNumber([1]))

#hash map 
def missingNumbHashMaps(nums):
    d = {}
    for num in range(len(nums)+1): 
        if num not in nums: 
            d[num] = "false"
            return num
        else:
            d[num] = 'true' 
    

# print(missingNumbHashMaps([3, 0, 1]))
# print(missingNumbHashMaps([0, 1]))
# print(missingNumbHashMaps([0]))
# print(missingNumbHashMaps([1]))
# print(missingNumbHashMaps([9,6,4,2,3,5,7,0,1]))
# print(missingNumbHashMaps([1,2,3]))

#sort 
def missingNumbSort(nums):
    
    if len(nums) ==1: 
        if nums[0] == 1: 
            return 0 
        else: 
            return 1 
  
    nums.sort()
    
    for n in range(len(nums)-1, -1, -1 ):
        if nums[n] - nums[n -1]  != 1 :
            return n 
        if nums[-1] != len(nums):
            return len(nums)

# print(missingNumbSort([3, 0, 1]))
# print(missingNumbSort([9,6,4,2,3,5,7,0,1]))
# print(missingNumbSort([0]))
# print(missingNumbSort([1]))
# print(missingNumbSort([1,2]))
# print(missingNumbSort([1,2,3]))
# print(missingNumbSort([0,1])) 
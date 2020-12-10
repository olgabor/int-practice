# -----------------------------------------------------------
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
# ----------------------------------------------------------- 
import copy 

def smallerNumber(nums):

    new = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)): 
            if nums[i] > nums[j]:
                count += 1

        new.append(count)

    return new

if smallerNumber([8,1,2,2,3]) == [4,0,1,1,3]: print(True)
if smallerNumber([6,5,4,8]) == [2,1,0,3]: print(True)
if smallerNumber([7,7,7,7]) == [0,0,0,0]: print(True)


def smallerNumberSort(nums):
    n = copy.deepcopy(nums)
    nums.sort( reverse= True)

    i = 0 

    while i < len(nums):
        if nums[i] == nums[i+1]: 
            nums[i] = len(nums) - (nums.index(nums[i]) + 2)
        else: 
            nums[i] = len(nums) - nums.index(nums[i])
        i +=1 
    return nums

print(smallerNumberSort([8,1,2,2,3]))
#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
def runningSum(nums):
    output = []
 
    for i in range(len(nums)):
        tmp = 0 
        for j in range(i + 1):
            tmp += nums[j]
        output.append(tmp)
    
    return output 


def runningSumFaster(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
        
    return nums

print(runningSumFaster([3,1,2,10,1]))
print(runningSumFaster([1,2,3,4]))

print(runningSum([3,1,2,10,1]))
print(runningSum([1,2,3,4]))
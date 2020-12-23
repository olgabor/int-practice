nums = [10, 11, 12, 13, 14, 15, 16]

target = 15 

def binarySearch(nums, target):
    right  = len(nums) -1  #6 
    left = 0

    while left <= right: 
        mid = (right - left )// 2
        if nums[mid] > target:
            left += 1
        elif nums[mid] < target:
            left -= 1
        elif nums[mid] == target: 
            return f'index of given target is {mid}'.format(mid)

    return 'number is not present in list '


print(binarySearch([10, 11, 12, 13, 14, 15, 16], 1))
print(binarySearch([10, 11, 12, 13, 14, 15, 16], 10))
print(binarySearch([10, 11, 12, 13, 14, 15, 16], 15))

#time complexity => O(log(n)) 
#space complexity => O(1)
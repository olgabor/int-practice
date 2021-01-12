#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

def majorityElement(nums):
    
    m = {}
    for num in nums:
        if num in m:
            m[num] += 1 
        if num not in m:
            m[num] = 1 
        if m[num] > len(nums) / 2: 
            return num 

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))

def majorityElement_version_1(nums):
    m = {}
    for num in nums:
        m[num] = m.get(num, 0) + 1 

    for num in nums:
        if m[num] > len(nums)/2:

            return num 

print(majorityElement_version_1([3,2,3]))
print(majorityElement_version_1([2,2,1,1,1,2,2]))

def func(num):
    if num == 0:
        return 1
    return num * func(num - 2)

print(func(8))

s = 'dog'
print(s.split('dog'))
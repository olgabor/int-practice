# 496. Next Greater Element I
# You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.

# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation:
# For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
# For number 1 in the first array, the next greater number for it in the second array is 3.
# For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation:
# For number 2 in the first array, the next greater number for it in the second array is 3.
# For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

#brute force 
def next_greater_elem(nums1, nums2):
    res = [0] * len(nums1)
    for i in range(len(nums1)):
        for j in range(nums2.index(nums1[i]), len(nums2)): 
            if nums2[j] > nums1[i]:
                res[i] = nums2[j]
                break
            res[i] = -1 
  
    return res


print(next_greater_elem([4,1,2], [1,3,4,2])) # output [-1,3,-1]
print(next_greater_elem([2,4], [1,2,3,4])) # output [3,-1]


#stack solution 
def next_greater_elem_stack(nums1, nums2):
    res = []
    stack = []
    mapping = {}
    
    for i in range(len(nums2)): 
        # 0 = nums2[0] = 1, stack=[1], map = {}, 
        # 1 = nums2[1] = 3, stack=[], map = {3 : 1}
        # 2 = nums2[2] = 4, stack=[4], map = {3 : 1, 4 : 3} 
        # 3 = nums2[3] = 2, stack=[4, 2], map = {3 : 1} 
        while stack and nums2[i] > stack[-1]:  # stack not empty & if nums2[i] less then previous element 
            mapping[stack.pop()] = nums2[i]    # write element,next_greater_element pair in dict 
        stack.append(nums2[i])                 # push each element nums2[i] on stack 
    
    while stack: #[4,2]                        # for each element in stack that has no pair of smaller element in nums2
        mapping[stack.pop()] = -1              # assign value of  -1 to it 
    
    for i in range(len(nums1)):               # for each element in nums1 write down the value saved in dict 
        res.append(mapping[nums1[i]])
    
    return res
print(next_greater_elem_stack([4,1,2], [1,3,4,2])) # output [-1, 3, -1]

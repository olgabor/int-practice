# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

    # If nums1 is larger than nums2, swap the arrays.

    # Add it to the hash map m.

    # Increment the count if the element is already there.

    # Iterate along nums2:
    # If the current number is in the hash map and count is positive:
        # write the number into res list 
        # Decrement the count in the hash map by -1 
    # Return res 


def array_intersection(nums1, nums2): 
    
    m = {}
    res = []
  
    if len(nums1) < len(nums2):
        nums2, nums1 = nums1, nums2

      
    for i in range(len(nums1)): 
        m.setdefault(nums1[i], 0)
        m[nums1[i]] += 1 
    
    for i in range(len(nums2)): 
        if nums2[i] in m and m[nums2[i]] != 0: 
            # print(nums2[i])
            res.append(nums2[i])
            m[nums2[i]] -= 1

    return res

print(array_intersection([1,2,2,1], [2,2]))
print(array_intersection([4,9,5],[9,4,9,8,4]))
print(array_intersection([1,2],[1,1]))
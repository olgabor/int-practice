#Merge Sorted Array
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively. 
# You may assume that nums1 has a size equal to m + n 
# such that it has enough space to hold additional elements from nums2.
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]


def merge_sorted_array(nums1, nums2,  m, n): 

    nums1_copy = nums1[:]

    p1 = 0  #read copy 
    p2 = 0 #read nums2
    p3 = 0 #write nums1 
    
    while p3 <= n+m - 1:
        # print('line 27 ' , p1 , p2 , p3 , nums1, nums1_copy)
        # if nums1_copy[p1] <= nums2[p2] and p1 < n and p2 < n: 
        print(p2 >= n, p1 < m )
        if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
     
        # if nums1_copy[p1] <= nums2[p2] and p1 <= m and p2 <= m: 
        #    print('line 35 ' , p1 , p2 , p3 , nums1, nums1_copy)
           nums1[p3] =  nums1_copy[p1]
           p1 +=1

        else: 
        #    print('line 33' , p1 , p2 , p3, nums1 , nums1_copy)
           nums1[p3] = nums2[p2]
           p2 +=1
        p3 += 1
    
    return nums1

print(merge_sorted_array([1,2,3,0,0,0], [2,5,6], 3, 3)) #[1, 2, 2, 3, 5, 6]
print(merge_sorted_array([1], [], 1, 0,)) #[1]
print(merge_sorted_array([0], [1], 0, 1,)) #[1]

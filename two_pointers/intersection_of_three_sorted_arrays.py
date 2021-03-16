# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

# Example 1:

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
# Example 2:

# Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
# Output: []

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

# arr1 = [197,418,523,876,1356]
# arr2 = [501,880,1593,1710,1870]
# arr3 = [521,682,1337,1395,1764]

def intersection_three_arrays(arr1, arr2, arr3): 
    output = []
    m = {}

    #add three arrays into one to avoid code repetition while adding values to dictionary 
    n = arr1 + arr2 + arr3
    for i in range(len(n)): 
        m.setdefault(n[i], 0)
        m[n[i]] += 1 
    
    for num, value in m.items(): 
        if value >= 3: 
            output.append(num)

    return output

# print(intersection_three_arrays(arr1, arr2, arr3))

# three pointers 

def intersection_w_pointers(arr1, arr2, arr3): 
    p1, p2, p3 = 0, 0, 0

    output = []
    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3): 
        if arr1[p1] == arr2[p2] and arr2[p2] == arr3[p3]:
            output.append(arr1[p1])
            p1 += 1 
            p2 += 1 
            p3 += 1
        else: 
            if arr1[p1] < arr2[p2]:

                p1+= 1 
            elif arr2[p2] < arr3[p3]: 

                p2 += 1
            elif arr3[p3] < arr1[p1]: 

                p3 += 1 
    
    return output



print(intersection_w_pointers(arr1, arr2, arr3))


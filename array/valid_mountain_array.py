# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

def validMountainArray(arr):

    if len(arr) < 3: # array with length less than 3 cant be mount_array 
        return False 

    i = 1 

    while i < len(arr) and arr[i] > arr[i-1]: # check if the current element is bigger than a previous
        i += 1 
    
    if i == 1 or i == len(arr):               # if after while loop the index is still 1 or it reached the end  
        return False                          # it means that there were no numbers larger the previous or only larger numbers are in array  
        

    while i < len(arr) and (arr[i] < arr[i-1]): # check if there are smaller numbers than previous 
        i += 1 
    
    if i == len(arr):                          # if we reached the end of the array - it means it is validMountainArray
        return True 
    else: 
        return False 
        
    
print(validMountainArray([0,3,2,1])) #True 
print(validMountainArray([3,5,5])) #Flase 
print(validMountainArray([0,2,3,4,5,2,1])) #True 
print(validMountainArray([0, 2, 3, 3, 5, 2, 1, 0])) #True 
print(validMountainArray([1,3,2])) #False 
print(validMountainArray([0,1,2,3,4,5,6,7,8,9])) #False 
print(validMountainArray([9,8,7,6,5,4,3,2,1])) #False 
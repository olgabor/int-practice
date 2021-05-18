# -----------------------------------------------------------
#You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

#You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.
# -----------------------------------------------------------

def firstBadversion(n):

    left = 1 
    right = n 
    
    while left < right:
        mid = (right + left) // 2 
        
        if isBadVersion(mid) == True:
            right = mid #move right pointer to mid since we found a first bad version and need to iterate through all elemets till mid 
        else: 
            left = mid +1 #if the version is not BAD ignore all elemets before it and start searching from mid+1  

    return left 
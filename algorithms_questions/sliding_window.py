#given an array of integers of size N, find maximum sum of K consequtive elements 

n = 4 
k = 2
arr = [80, -50, 90, 100 ]

def maxSumBruteForce(arr, n, k):
    max_sum = 0 
    for i in range(0, (n - k + 1)): 
        sum = 0 
        for j in range(k):
            sum += arr[i + j] 
        
        if sum > max_sum: 
            max_sum = sum
       
    return max_sum

print(maxSumBruteForce(arr, n, k))

def maxSumSlidingWindow(arr,k): 
    arraySize = len(arr)
    if arraySize <= k:
        return 'Invalid operation'
    
    #calculate the sum of first window 
    window_sum = (sum(arr[i] for i in range(k)))
    max_sum = window_sum 

    for i in range(arraySize-k): 
        print(i)
        window_sum = window_sum - arr[i] + arr[ i + k]
        max_sum = max(window_sum, max_sum)

    return max_sum 

print(maxSumSlidingWindow(arr,k))
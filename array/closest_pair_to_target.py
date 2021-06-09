# Given a sorted array and a number x, find the pair in array whose sum is closest to x11:05
# Given a sorted array and a number x, find a pair in array whose sum is closest to x. 
# Examples: Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54 Output: 22 and 30 Input: arr[] = {1, 3, 4, 7, 10}, x = 15 Output: 4 and 10

def find_pair_memo(arr, target): 
    start = 0 
    end = len(arr) -1 
    diff = float('inf')

    res_l , res_r = 0, 0 

    while start < end: 
        if abs(arr[start] + arr[end] - target) < diff: 
            res_l = start
            res_r = end  
            diff = abs(arr[start] + arr[end] - target)
        if arr[start] + arr[end] == target: 
            return arr[start] ,  arr[end]
        if arr[start] + arr[end] > target: 
            end -= 1 
        else:
            start += 1
 
    return (arr[res_l], arr[res_r])

print(find_pair_memo([10, 22, 28, 29, 30, 40], 54)) # 22, 30 
print(find_pair_memo([1, 3, 4, 7, 10], 15)) # 4, 10 


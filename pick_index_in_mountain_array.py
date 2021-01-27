def peakIndexInMountainArray(arr):

    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return start
        
print(peakIndexInMountainArray([0,1,0]))
print(peakIndexInMountainArray([0,2,1,0]))
print(peakIndexInMountainArray([3,4,5,1]))


def peakIndexEnumearate(arr):
    for index, value in enumerate(arr):
        if arr[index+1] < arr[index]:
            return index 

print(peakIndexEnumearate([3,4,5,1])) 

def indexPeakLinear(arr):
    for i in range(len(arr)):
        if arr[i +1]  < arr[i]:
            return i 
            
print(indexPeakLinear([3,4,5,1])) 

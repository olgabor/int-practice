#binary search algorithm implementation 

myList = [3, 3, 6, 7, 8, 12] 

def binarySearch(array, item): 
    low = 0 
    high = len(array)-1 
    mid = (low + high) // 2

    while mid >= low and mid <= high: #mid value is greater or equal to low and not larger or equal high 
        
        guess = array[mid]
        if guess == item:
            return 'number ' + str(guess) + ' exists in given array'
        if guess > item: 
            mid = mid - 1 
        if guess < item: 
            mid = mid + 1 
        
    return None 

def binarySearchRecursively(array, item): 
    low = 0 
    high = len(array)-1 
    mid = (low + high) // 2  
   
    
    while mid >= low and mid <= high: 
        guess = array[mid]
        if guess == item:
            return 'number ' + str(guess) + ' exists in given array'
        if guess > item:  
            return binarySearch(array[:mid], item)
        if guess < item:  
            return binarySearch(array[mid:], item)
        else: 
            return None 


print(binarySearch(myList, 52)) 
print(binarySearch(myList, 2)) 
print(binarySearch(myList, 12)) 
print(binarySearchRecursively(myList, 52)) 
print(binarySearchRecursively(myList, 2)) 
print(binarySearchRecursively(myList, 12)) 
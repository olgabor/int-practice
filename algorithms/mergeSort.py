array = [12,6,3,7,13,8] 

def split(array):
    
     
    k = 0
    middle = len(array) // 2 
    print(middle)
    if len(array) == 1: 
        return array 
    else: 
        left = array[:middle]
        right = array[middle:]
        split(left)
        split(right)
    
    
    i = 0 #index of left 
    j = 0 # index of right
    
    while len(left) == 1 and len(right) == 1:
        if left[i] < right[j]:
            array[k] = left[i] 
            k += 1 
            i += 1 
            print(i, j,  left ,right, array  )
        if right[j] < left[i]:
            array[k] = right[j]
            array[2] = left[i] 
            k += 1 
            j += 1 
            k = 2  
        return array 
        
    
    while j < len(right): 
        print(k, i , j,  left , right ) 
        if left[i] < right[j]: 
            array[k] = left[i]
            k += 1 
            i += 1 
        if right[j] < left[i]: 
            array[k] = left[i]
            j += 1
            k += 1 
    
    
print(split(array))
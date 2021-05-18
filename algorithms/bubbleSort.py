#buuble sort algorithm implementation  
myArray = [12,6,3,7,13,8]
myArray1 =[20,30,30,40,90,50,60,70,80,30,100,110]
myArray2 = [3,6,7,8,12,13] 
myArray3 = [100, -3, -1, 5, 100]

def bubbleSort(array):
    
    for i in range(len(array)):
        for j in range(i+1 , len(array)):
            if array[i] > array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp 
    
    return array

print(bubbleSort(myArray))
print(bubbleSort(myArray1))
print(bubbleSort(myArray2))
print(bubbleSort(myArray3))

#buuble sort function 
myArray = [12,6,3,7,13,8]
myArray1 =[20,30,30,40,90,50,60,70,80,30,100,110]
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

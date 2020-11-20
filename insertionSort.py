#Insertion sort algorithm implmentation 
array = [30,20,10,15,10,40,90] 
array1 = [20,30,30,40,90,50,60,70,80,30,100,110] 
array2 = [3,6,7,8,12,13] 
array3 = [100, -3, -1, 5, 100]

def insertionSort (array):
    
    for i in range(len(array)-1):

        # store the current item value 
        tempList = [] 

        if array[i] > array[i+1]: 
            # Loop  through the sorted portion of the array 
            # insert the value
            for j in range(i + 1): 
                tempList.append(array[j]) 

                if array[i+1] < tempList[j]:
                        array[j] = array[i+1] 
                        array[i+1] =  tempList[j]
                        print(tempList, array)
        
    return array 
           

print(insertionSort(array))
print(insertionSort(array1))
print(insertionSort(array2))
print(insertionSort(array3))
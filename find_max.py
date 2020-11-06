#This function returns the largest number in a given array.

verbose = True

def find_max(ar, n):
    if len(ar) == 1 and n == ar[0]:
        return 'the list has one value ' , ar[0]

    if n > ar[0] and len(ar) == 1:
        return n

    if n >= ar[0]: # if n is larger OR equals last value => run the function excluding the last value
        return find_max(ar[1:], n )

    if n < ar[0]: # if n smaller the last value in list ==> run the function excluding the last value and switching n with larger value 
        return find_max(ar[1:], ar[0]) 


ar = [3,4,2,1,2,6,1]
ar1 = [3,4,2,1,2]
ar3 = [9]


print(find_max(ar1, ar1[0]))
print(find_max(ar, ar[0]))
print(find_max(ar3, ar3[0]))



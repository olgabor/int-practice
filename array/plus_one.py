#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

#You may assume the integer does not contain any leading zero, except the number 0 itself.

def plus_one(digits):

    number = ''
    for num in digits: 
        number += str(num)

    n = int(number)+1

    return list(str(n))

print(plus_one([1,2,3]))
print(plus_one([4,3,2,1]))
print(plus_one([0]))
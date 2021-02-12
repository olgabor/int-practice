# Question: Given a list of digits from 0 - 9, return the largest number. 
# Assume that this number is small enough to fit in memory. 

# Please do not: convert the numbers into strings and sort them and join the array as a solution

# How would you solve this without using a string conversion? 

# Input: [0, 1, 1, 9]
# Output: 9110 

# Input: [3, 1, 8, 0]
# Output: 8310 

# Solution with frequency counting technique 
  # create empty dictionary(d) and empty string(output)
  # iterate over all numbers in given list and fill out the dictionary with number of appearances for each number
  # iterate over the sorted dictionary key, value 
    # in range of value (which is a number of appearances add key(number) to output string 
def largestNumber(num):
    d = {}
    output = ''
    for i in num:
        d.setdefault(i, 0)
        d[i] += 1 
    
    for k,v in sorted(d.items()):
        for i in range(v):
            output = output + str(k)
    print(type(output))
    return ''.join(reversed(output))


print(largestNumber([0, 1, 1, 9]))
print(largestNumber([3, 1, 8, 0]))
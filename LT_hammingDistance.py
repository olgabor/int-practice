#--------------------------------------------------------------------------------
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:
# Input: x = 1, y = 4
# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#The above arrows point to positions where the corresponding bits are different
#--------------------------------------------------------------------------------

def hammingDistance(x, y): 
    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]

    diff_count = 0 
    i = 0 

    if x_bin == y_bin:
        return 0 

    while i < len(x_bin) and i < len(y_bin):
        if x_bin[i] != y_bin[i]:
            diff_count += 1 
        i += 1  
        
    return diff_count
   
print(hammingDistance(680142203,1111953568))
print(hammingDistance(1,4))

#strings solution
def hammingDistanceString(x, y): 

    diff_count = 0 
    i = 0 

    while i < len(x) and i < len(y):
        if x[i] != y[i]:
            diff_count += 1 
        i += 1  
        
    return diff_count


print(hammingDistanceString('AGCAGACCCACAA','TGCAGCGAAACGA'))
print(hammingDistanceString('ACTGTGCAATACCTAAGTGAAAGGGGTGCATAGATCATTCTTTCGTTACCTCGGGTGCTATGA','ACTCCTCTGTGTCTAAGTGAAAGGGGTGCTTGCAGGGTAATCCTTCCACCTGATACCGACTCG')) 

#XOR solution 
def hammingDistanceXOR(x,y):
    return bin(x ^ y).count('1')

#x ^ y Does a "bitwise exclusive or". 
# Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,
# and it's the complement of the bit in x if that bit in y is 1.

print(hammingDistanceXOR(680142203,1111953568))

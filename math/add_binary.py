#Given two binary strings a and b, return their sum as a binary string.

def addBinary(a, b):
  
    carry = 0 
    total = []

    if len(a) < len(b):
        diff = len(b) - len(a)
        a = ('0' * diff ) + a
    else: 
        diff =  len(a) - len(b) 
        b = ('0' * diff ) + b

    a_index, b_index  = len(a) -1 , len(b) -1 

    while a_index >= 0 or b_index >= 0 :

        if a[a_index] == '1' and b[b_index] == '1':
            
            if carry == 0: 
               total.insert(0, '0')
               carry = 1
            else: #   carry == 1: 
                total.insert(0, '1')
                carry = 1
               
        if a[a_index] == '0' and b[b_index] == '0': 
            if carry == 0: 
               total.insert(0, '0')
            else: 
                 total.insert(0, '1')
                 carry = 0  
            
        if a[a_index] == '1' and b[b_index] == '0': 
            if carry == 0: 
                total.insert(0, '1')
            else: 
                total.insert(0, '0')
                carry = 1
            
        if a[a_index] == '0' and b[b_index] == '1':
            
            if carry == 0: 
               total.insert(0, '1')
            else: 
                total.insert(0, '0')
                carry = 1
    
        a_index -= 1 
        b_index -= 1

    if carry == 1: 
        total.insert(0, str(carry))

    return ''.join(total)

print(addBinary("0", "0"))
print(addBinary("1010", "1011"))
print(addBinary("11", "1"))
print(addBinary("1", "111"))
print(addBinary("1111", "1111"))


def addBinaryFaster(a,b):
    result = []
    carry = 0 
    i, j = len(a) -1, len(b) -1

    while i >= 0 or j >= 0 or carry: 
        total = carry 

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total%2))
        carry = total // 2 
    
    return ''.join(reversed(result))

print(addBinaryFaster("1111", "1111"))

print((2 % 2)) 
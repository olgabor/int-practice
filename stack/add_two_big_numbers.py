
def addStrings(string1, string2):
    res = []
    point = '.'
    carry = 0 
    string1, string2 = list(string1), list(string2)
    
    if not string1 or not string2: 
        return 
    if len(string1)  < len(string2): 
        for i in range(len(string2) - len(string1)): 
            string1.append( str(0))
    elif  len(string2) < len(string1):
        for i in range(len(string1) - len(string2)): 
            string2.append( str(0))


    while string1 and string2 or carry : 
        st1 = string1.pop()
        st2 = string2.pop()

        if st1.isalnum() and st2.isalnum() :
            t = int(st1) + int(st2) 
            
            if t == 10: 
                res.insert(0, '0')
                carry += 1 
            elif t < 10 and carry: 
                t += carry 
                carry -= 1
                res.insert(0, str(t))
            else: 
                res.insert(0, str(t))

        else: 
            if st1 == point or st2 == point:
                res.insert(0, point)

    return ''.join(res)
 
print(addStrings('3.14', '0.9'))
print(addStrings('3', '3'))
print(addStrings('1.0', '3'))
print(addStrings('1.0', '0'))
print(addStrings('3', '0.2')) 
print(addStrings('0', '')) 

def decode(s):

    i = 0
    res = ''
    print(s[len(s) -1])
    while( i < len(s) -1) :

        # Counting occurrences of s[i]
        count = 1

        while s[i] == s[i + 1] :
            i += 1
            count += 1

        res += (str(count)) + s[i]
        i += 1

        if i == len(s) -1:         
            res += str(1) + s[i]
            break 
   
    return res

print(decode('wwwbbbw'))
print(decode('aabbcde'))


def string_compression(s): 
    res = ''
    i = 1 
    count = 1

    if len(s) == 0: return ''

    if len(s) ==1: return s + '1'


    while i < len(s):  
        if s[i] == s[i -1]: 
            count += 1
        else: 
            res += s[i -1] + str(count)
            count= 1    

        i += 1

    res += s[i -1] + str(count)
    return res   


print(string_compression('AAAABBBBBCCCCDDEEEE'))
print(string_compression('A'))

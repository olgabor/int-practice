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


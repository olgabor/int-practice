
#Implement function ToLowerCase() that has a string parameter str, 
# and returns the same string in lowercase.

# ord() returns ASCII code 
# chr() returns 


def toLowerCase(inp):
    if type(inp) not in [str]:
        raise TypeError('Parameter should be string')
    if len(inp) == 0:
        return 'string is empty'
    else: 
        for letter in inp: 
            if ord(letter) <= 90 and ord(letter) >= 65: #uppercase letters in ASCII are higher than 90 and lower than 65 
                inp = inp.replace(letter, chr(ord(letter) + 32)) 
            
    return inp 
    
print(toLowerCase("Hello"))
print(toLowerCase("here"))
print(toLowerCase("Apple"))
print(toLowerCase("LOVELY"))
print(toLowerCase("al&phaBET"))
print(toLowerCase("PiTAs"))
print(toLowerCase("PiTAs24<<<<"))
print(toLowerCase(""))
print(toLowerCase(12))
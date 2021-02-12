
def convert(s):

    output = []
    print(len(s))
    for i in range(len(s)):
        print(i)
        if i == 0: 
            output.insert(i, '(')
            print(output)
        elif i == 4: 
            output.insert(i, ')')
        elif i == 5: 
            output.insert(i, ' ')
        elif i == 9: 
            output.insert(i, ' ')
        else:
            output.insert(i, s[i])
  
    return output 

print(convert([1234567890])) 
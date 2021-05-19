def reverse(x): 

    res = ''
    if int(x) < 0: 
        res+= ('-')
    converted_number = [number for number in str(x)]
    # print(converted_number)
    while converted_number:
        last_digit = converted_number.pop() 
        if last_digit == '-': 
            break
        else:   
            res += last_digit
    
    if int(res) >= -2147483648 and int(res) <= 2147483647:
        return int(res)
    else:
        return 0

print(reverse('23'))
print(reverse('-23'))
print(reverse(123))
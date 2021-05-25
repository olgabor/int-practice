#Write a recursive function called reverse that accepts a string and returns a reversed string.

def reverse(word):
    tmp = ''  
    if type(word) != str:
        # raise ValueError ('This is not a string')
        return 'This is not a string'
    elif len(word) == 0: 
        return  ''
    elif len(word) < 1: 
        return word 
    else: 
        tmp = word[-1]
        tmp = tmp + reverse(word[:-1])  
        return tmp 

print(reverse("")) # ""
print(reverse("a")) # "a"
print(reverse("ab")) # "ba")
print(reverse("computer"))
print(reverse("abcdefghijklmnopqrstuvwxyz")) # "zyxwvutsrqponmlkjihgfedcba"
print(reverse(reverse("computer"))) # "computer"
print(reverse(2)) #'This is not a string'


#Write a function that reverses a string. The input string is given as an array of characters char[].
def reverseTwoPointers(char):
  
    tmp = ''
    start = 0 
    end = len(char) -1 

    while start <= end: 
        tmp = char[start]
        char[start] = char[end]
        char[end] = tmp 
        start += 1
        end -= 1

    print(char)

print(reverseTwoPointers(["h","e","l","l","o"]))
print(reverseTwoPointers(["h","e","l","l","o"]))

#given a string return, write a function to reverse a string in place 
def reverse_string_in_place(s):

    new = list(s)
    l , r = 0, len(new) -1

    while l <= r: 
        new[l], new[r] = new[r], new[l]
        l += 1 
        r -= 1  
    
    return ''.join(new)

print(reverse_string_in_place('abcd'))

print(reverse_string_in_place('hello world'))


def reverse_integer(x):

    res = ''
    if x < 0: 
        x = abs(x)
        res= '-'

    while x > 0: 
        tmp = x%10
        n = x // 10 
        res+= str(tmp)
        x = n 

    return int(res)

print(reverse_integer(123))
print(reverse_integer(-123))
print(reverse_integer(120))

def reverse_string_recursion(s): 

    if len(s) ==1: return s

    else: return s[-1] + reverse_string_recursion(s[:-1])

print(reverse_string_recursion('hello world'))
print('helloworld'[:-1])
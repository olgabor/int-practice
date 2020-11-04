#Write a recursive function called reverse that accepts a string and returns a reversed string.

def reverse(word ):
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
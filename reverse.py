#Write a recursive function called reverse that accepts a string and returns a reversed string.

def reverse(word ):
    tmp = ''  
    if len(word) == 0: 
        return  ''
    if len(word) < 1: 
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
#calculate the amount of charachters in the string 
message = 'it was a bright cold day in April, and the clocks were striking thirteen.'

#with setdefault() method
count = {}
for character in message:
    count.setdefault(character , 0)
    count[character] = count[character] +1 
print(count)

#another version 
c = {} 
for char in message: 
    if char not in c:
        c[char] = 0
    else: 
        c[char] =+1 
print(c)
spam = ['apples', 'bananas', 'tofu', 'cats'] 
# spam = []
spam1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
spam1 = ["apple"]

#write a function that takes a list as argument and returns a string with all items separated by comma and a space 
# with 'and' inserted before last item. 

# example: 'apples, bananas, tofu, and cats'

def separated(spam):
    if len(spam) != 0:
        for i in range(len(spam) -1):
            print ( spam[i] + ', ' ,  end = ' ' ) 
        print( 'and', spam[-1], end='\n')
    if len(spam) == 1: 
        print(spam[0])
    else:
        return 'Given list is empty'
    return '' 

print(separated(spam))
print(separated(spam1))
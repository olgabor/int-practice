#write a function named displayInventory() 
# that would take any possible 'inventory' and dsipaly like the folowing: 
# Inventory:
# 12 arrows
# 42 gold coins
# 1 rope
# 6 torches
# 1 dagger
# Total number of items: 62

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
nums = {'Math': 0, 'English': 0, 'Science': 0}
fruit = {"apple": 430, "banana": 312, "orange": 525, "pear": 217}

def displayInventory(inventory):
    print('Inventory:')
    total = 0 

    word_ending = ['s', 'sh', 'ch', 'x', 'z'] # use 'es' to make a plural all oter use 's'
    
    for key, value in inventory.items():
        
        if value <= 1: 
            print(value , key)
        elif value != 1:
            if key[-1] in word_ending or key[-2:] in word_ending and value > 1:
                print(value, key + 'es')
            else:
                print(value, key + 's')

        total += value 

    print('Total number of items: ', total) 

    return '' 

print(displayInventory(stuff))
print(displayInventory(nums))
print(displayInventory(fruit))
    

#write a function named addsToInventory() that takes the list and adds it to main inventory dictionary 
addStuff = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addsToInventory(inventory, addStuff):

    for item in addStuff:
        inventory.setdefault(item, 0) 
        inventory[item] = inventory[item] + 1 

    return inventory
    
inv = addsToInventory(stuff, addStuff) 

#display updated inventory
print(displayInventory(inv))
        

#Write a function called pretty_print that accepts a complex dictionary and prints out all of it's keys and all of its values. 
#The dictionary can have dictionaries nested inside of it.

o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}
o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}

def pretty_print(dictionary, indent): 

    for key, value in dictionary.items():
        
        if isinstance(value, dict) == True:
            pretty_print(value, indent + 2)
        else: 
            print (indent * ' ' , key,  ':', value) 
    pass
    return ''

print('------o1-------' ,  pretty_print(o1, 2 ))
print('------o2-------' , pretty_print(o2, 2 ))
print('------o3-------' , pretty_print(o3, 2 ))

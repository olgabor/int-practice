#write a function to return the key of the largest value in an object of key=>value pairs  
sample_dict = {
  "val1": 5,
  "val2": 0,
  "val3": 1964, 
  "val4": 20
}

def dict_max_val(sample_dict):

    max_val = 0 
    for value in sample_dict.values():
        if value > max_val: 
            max_val = value 

    return max_val

print(dict_max_val(sample_dict))

#faster solution 
print(max(sample_dict, key=sample_dict.get))
#print numbers recursively 

numbers = [1,2,3,4,5]
len_numbers = 5 
def print_numbers_recursive(index):
    if index == len_numbers: # exiting when this condition is not met 
        return 
    print(numbers[index])
    print_numbers_recursive(index + 1)

print_numbers_recursive(0)

#iterative 
def print_numbers_iterative(numbers): 
    for number in numbers:
        print(number)
print_numbers_iterative(numbers)


#Flatten a JSON object: 
# Input:{ a { b { c { d : e} } } }
# Output: {a.b.c.d: e} 
# You can only expect nested JSON objects. There won’t be any, sets, or other types of data structures. 

#the reccursive approach is better because i dont know how many nested dict we have 
elem = { 'a': {' b': { 'c': { 'd' : 'e'} } } } 
output = {}
def flatten_dict(elem, key=""):
    if not isinstance(elem, dict): 
        output[key] = elem
        return 
    if key != "":
        key = key + "."
    
    for k,v in elem.items():

        flatten_dict(v, key + k)
    
flatten_dict(elem)
print(output)
         

# Given a string, find ALL permutations 
# Input: “abc” 
# Output: [“abc”, “acb”, “bac”, “bca”, “cab”, “cba”] (order of output doesn’t matter as long as you’ve got all the permutations) 

def permutation(string, l, r):
    if l == r: 
        print(string)
        
    else: 
        for i in range(l, r +1):
            string[l], string[i] = string[i], string[l]
            permutation(string, l+1, r)
            string[l], string[i] = string[i], string[l]

print(permutation(["a", "b", "c"], 0, 2 ))
# Given a string, return a string with all the vowels reversed.
# Input: “rainbow” 
# Output: “roinbaw”




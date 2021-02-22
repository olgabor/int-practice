#Flatten a JSON object: 
# Input:{ a { b { c { d : e} } } }
# Output: {a.b.c.d: e} 
# You can only expect nested JSON objects. There won’t be any, sets, or other types of data structures. 

inp = { 'a': {' b': { 'c': { 'd' : 'e'} } } } 

def flatten_dict(inp):

    m = {}

    key = '' #until final val is found - change key 


     
    for k, v in inp.items(): 
        print(k,v)
        if type(k) == str:
            print(k)
        #  if type(v) == dict: 
        #      key += k 
        #      m[key] = 
         

print(flatten_dict(inp))
         






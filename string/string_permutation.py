#Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

# For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# Note: If a character is repeated, treat each occurence as distinct, 
# for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'

def permute(s):
    # list to save all variants 
    output = []
    
    #base case - return s is string length is 1 
    if len(s) <= 1:
        output=[s]
    else:
        # For every letter in string
        for i, let in enumerate(s):
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i]+s[i+1:]):
                # Add it to output
                output+=[let+perm]

    return output

print(permute('abc'))
s = 'abc'


# -----------------------------------------------------------
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.
# -----------------------------------------------------------

def balancedString(s):

    l_counter = 0 
    r_counter = 0 
    count = 0 

    for i in range(len(s)): 
        if s[i] == 'R': 
            r_counter += 1 
        if s[i] == 'L': 
            l_counter += 1 
        if l_counter == r_counter: 
            count+= 1 

    return count 

if balancedString('RLRRLLRLRL') == 4: print(True)
if balancedString('RLLLLRRRLR') == 3: print(True)
if balancedString('LLLLRRRR') == 1: print(True)
if balancedString('RLRRRLLRLL') == 2: print(True)

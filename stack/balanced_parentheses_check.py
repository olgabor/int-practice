# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

#steps: 
    #scan the string from left to right and every time you see the opening parenthesis push the item to stack
    # when we see a closing parenthesis we check whether the last open one is corresponding closing match by opening the element from stack
    # if it is a match, we proceed forward, if not - return False 
    # if the stack is empty we return False , because there is no opening parenthesis associated with this closing one 
    # at the end we also check if stack is empty, yes - return True , no - False because there were some opened parenthesis that were not closed  


def balance_check(s):

    #edge case check 
    if len(s)%2 != 0: 
        False 
    
    opening = set('([{') #creates a set of opening brackets {'(', '{', '['} 

    matches = set([('(', ')'), ('[',']'), ('{', '}')]) # creates open, closed parenthesis set {('[', ']'), ('(', ')'), ('{', '}')}

    stack = []

    for paren in s: 
        #is it is an opening - push to stack 
        if paren in opening:
            stack.append(paren)

        else: 
            if len(stack) == 0: #if stack is empty - there was no opening parenthesis 
                return False 
            
            last_open = stack.pop() #pop the last item from the stack 
            
            if (last_open, paren) not in matches: #check if last iten fron the stack and current item in sting both are in matches 
                return False

    return len(stack) == 0 

print(balance_check('[]'))
print(balance_check('[{{{{((({{{[[[]]]}}})))}}}}]'))
print(balance_check('[{{{{((({{{[[[]]]}}})))}}}]'))
print(balance_check('{{[[]]}}'))
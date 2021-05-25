# 739. Daily Temperatures

# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. 
# If there is no future day for which this is possible, put 0 instead.

# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

def daily_temp(T): 

    stack = []
    output = [0] * len(T) 

    for index, temp in enumerate(T):
    
        while stack and temp > T[stack[-1]]:        # until the curent temerature is larger than last item in stack 
            stack_peek = stack.pop()                # pop the last stack element 
            output[stack_peek] = index - stack_peek # write diff between current index and last stack elem 

        stack.append(index) 

    return output


print(daily_temp([73, 74, 75, 71, 69, 72, 76, 73])) # [1, 1, 4, 2, 1, 1, 0, 0] 
print(daily_temp([89,62,70,58,47,47,46,76,100,70]))# [8,1,5,4,3,2,1,1,0,0]

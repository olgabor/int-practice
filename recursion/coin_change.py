# Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.

# For example:
# If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:

# 1+1+1+1+1+1+1+1+1+1
# 5 + 1+1+1+1+1
# 5+5
# 10
# With 1 coin being the minimum amount.

# IMPORTANT TO READ https://runestone.academy/runestone/books/published/pythonds/Recursion/DynamicProgramming.html

#Recursive Solution 
def rec_coin(target,coins):
    '''
    INPUT: Target change amount and list of coin values
    OUTPUT: Minimum coins needed to make change
    
    Note, this solution is not optimized.
    '''
    
    # Default to target value
    min_coins = target
    
    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1
    
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive Call (add a count coin and subtract from the target) 
            num_coins = 1 + rec_coin(target-i,coins)
            
            # Reset Minimum if we have a new minimum
            min_coins = min(num_coins, min_coins)
                
    return min_coins

print(rec_coin(15,[1,5,10])) #2 

#Dynamic Programming Solution - correct solution 
def rec_coin_dynam(target, coins, known_results):
    # Default output to target
    min_coins = target
    
    # Base Case
    if target in coins:
        known_results[target] = 1
        return 1
    
    # Return a known result if it happens to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:
            
            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)
            
            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins
                
                # Reset the known result
                known_results[target] = min_coins
                
    return min_coins
target = 63
coins = [1,5,10,25]
known_results = [0]*(target+1)

print(rec_coin_dynam(target,coins,known_results)) # 6 

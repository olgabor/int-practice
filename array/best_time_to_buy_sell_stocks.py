#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock
#and choosing a different day in the future to sell that stock.

# have the lovest number saved to variable buy as a first item in the array 
# set profit to 0 
# loop through the array and in the rage from 1 to lenght of array 
    # if the current element is less than variable buy => assign it to buy 
    # if result of substraction is larget than value of profit = save this value as profit 
# return profit 

def maxProfitOneTransaction(prices):

    buy = prices[0]
    profit = 0 
    
    for i in range(1, len(prices)): 
        if prices[i] < buy:
            buy = prices[i]

        if (prices[i] - buy) > profit:
            profit = prices[i] - buy 
 
    return profit 

# print(maxProfitOneTransaction([7,1,5,3,6,4]))
# print(maxProfitOneTransaction([7,6,4,3,1]))
# print(maxProfitOneTransaction([1,2]))

#BRUTE force solution 
# loop through all numbers and compare the differences between the current number and next one in the list 
# keep comparing the max_number and current difference  
# return the max difference beetween numbers 

def maxProfitBruteForce(prices):
    max_profit = 0 
    for i in range(len(prices)): 
        for j in range( i +1, len(prices)): 
            max_profit = max(prices[j] - prices[i], max_profit ) 
    
    return max_profit

# print(maxProfitBruteForce([7,1,5,3,6,4]))
# print(maxProfitBruteForce([1,2]))
# print(maxProfitBruteForce([7,6,4,3,1]))

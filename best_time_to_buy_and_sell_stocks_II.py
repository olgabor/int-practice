def maxProfit(prices):
    
    max_profit = 0 

    for i in range(1, len(prices)):

        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit


# print(maxProfit([1,2,3,4,5,3,5]))
# print(maxProfit([1,2,3,4,5]))
# print(maxProfit([7,6,4,3,1]))
# print(maxProfit([7,1,5,3,6,4]))
# print(maxProfit([1, 7, 2, 3, 6, 7, 6, 7])) # 7 -1 = 6 ,3 -2,  6-3 = 3 , 7 -6 = 1, 7-6 = 1 


#peak and valley approach 

def max_profit_peak_vallye(prices): 
    maxProfit = 0 
    i = 0 
    valley = prices[0]
    peak = prices[0]

    while (i < len(prices) - 1): 
        
        while (i < (len(prices) - 1)  and prices[i] >= prices[i + 1]): 
            i += 1 
            valley = prices[i]
            
        while (i < len(prices) - 1 and prices[i] <= prices[i + 1]): 
            i += 1 

        peak = prices[i]
        
        maxProfit += peak - valley 

    return maxProfit 

print(max_profit_peak_vallye([1,2,3,4,5,3,5]))
print(max_profit_peak_vallye([1,2,3,4,5]))
print(max_profit_peak_vallye([7,6,4,3,1]))
print(max_profit_peak_vallye([7,1,5,3,6,4]))
print(max_profit_peak_vallye([1, 7, 2, 3, 6, 7, 6, 7]))

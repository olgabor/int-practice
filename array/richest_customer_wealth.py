#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​
# customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

#A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.
accounts = [[1,2,3],[3,2,1]]
accounts1 = [[1,5],[7,3],[3,5]]
accounts2 = [[2,8,7],[7,1,3],[1,9,5]]

def maximumWealth(accounts):
    maxWealth = 0 

    for i in range(len(accounts)):
        wealth = 0 
        for j in range(len(accounts[i])):
            wealth += accounts[i][j]

            if wealth > maxWealth:
                maxWealth = wealth 
    
    return maxWealth

print(maximumWealth(accounts))
print(maximumWealth(accounts1))
print(maximumWealth(accounts2))

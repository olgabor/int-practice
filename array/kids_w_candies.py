#Given the array candies and the integer extraCandies, where candies[i] 
# represents the number of candies that the ith kid has.

#For each kid check if there is a way to distribute extraCandies among
#the kids such that he or she can have the greatest number of candies 
# among them. Notice that multiple kids can have the greatest number of candies.

#Input: candies = [2,3,5,1,3], extraCandies = 3
#Output: [true,true,true,false,true] 

def kidsWithCandies(candies, extraCandies):
    max_val = 0
    # max_val  = max(candies)
    # #find the max value in list 
    for i in range(len(candies)):
        if candies[i] > max_val:
            max_val = candies[i]

    for i in range(len(candies)):
        if not (candies[i] + extraCandies) >= max_val:
            candies[i] = False  
        else:
            candies[i] = True  

    return candies


print(kidsWithCandies([2,3,5,1,3], 3))
print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([12,1,12], 10))
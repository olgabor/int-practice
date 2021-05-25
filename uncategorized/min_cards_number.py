
# You are playing a cards game whee each card has a number representing how much points is worth. 
# The goal of the cards game is to find the smallest number of cards that sum up o a specific 
# amount of poins. 
# If the total can not be summed up to with any combination of cards, return -1 
# Assume you can use as many of he same cards as many time as you want. 

#example 1 
# cards = [1,2,5]
# total = 11 
# output = 3 
# explanation = 11 = 5+5+1 

#example 2
# cards = [1,4,5]
# total = 12
# output = 3 
# explanation = 12 = 4 +4 +4 

#example 3 
# cards = [2]
# total = 3
# output = -1

#example 4
# cards = [1]
# total = 0
# output = 0

def count_cards(cards, total): 
    output = 0 
    for card in reversed(cards):
        # print(card)
        # while we can still use coin, use it until we can't
        while card <= total:
            total = total - card
            print(card)
            output += 1
    print(total)
    return output
# print(count_cards([1,2,5], 11)) #3 
# print(count_cards([1,4,5], 12)) #3 Gives 4 
# print(count_cards([2], 3))#-1 gives 1 


def combinationSum(arr, sum): #https://www.geeksforgeeks.org/combinational-sum/
    ans = []
    temp = []
    # first do hashing nothing but set{}
    # since set does not always sort
    # removing the duplicates using Set and
    # Sorting the List
    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, temp, sum, 0)
    return ans
 
def findNumbers(ans, arr, temp, sum, index):
     
    if(sum == 0):
        # Adding deep copy of list to ans
        ans.append(list(temp))
        return
       
    # Iterate from index to len(arr) - 1
    for i in range(index, len(arr)):
 
        # checking that sum does not become negative
        if(sum - arr[i]) >= 0:
 
            # adding element which can contribute to
            # sum
            temp.append(arr[i])
            findNumbers(ans, arr, temp, sum-arr[i], i)
 
            # removing element from list (backtracking)
            temp.remove(arr[i])
# # Driver Code
# arr = [2, 4, 6, 8]
# sum = 8
# ans = combinationSum(arr, sum)
# # If result is empty, then
# if len(ans) <= 0:
#     print("empty")
     
# # print all combinations stored in ans
# for i in range(len(ans)):
 
#     print("(", end=' ')
#     for j in range(len(ans[i])):
#         print(str(ans[i][j])+" ", end=' ')
#     print(")", end=' ')
 
# print(combinationSum([1,2,5], 11))
def combinationSum(cards, total):

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(len(list(comb)))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(cards)):
                # add the number into the combination
                comb.append(cards[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - cards[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(total, [], 0)

        return min(results)


print(combinationSum([1,2,5], 11)) # min number is 3 

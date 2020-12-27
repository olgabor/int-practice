# -----------------------------------------------------------
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
# -----------------------------------------------------------

#math formula - 2∗(a+b+c)−(a+a+b+b+c)=c

def singleNumber(nums): 

    return 2* sum(set(nums)) - sum(nums)

print(singleNumber([2,2,1]))
print(singleNumber([2,2,1,1,4]))


#has table => time compexity O(n), space complexity is O(n)
#iterate over nums
    #set default value of 0 for each num in new dictionary  
    #for each number in nums increase value in dictionary by 1 
    #if dictionary value equals 1 return the number 

def hashTableSolution(nums): 
    n = {}
    for num in nums: 
        n.setdefault(num, 0)
        n[num] += 1  
    
    for num in n:
        if n[num] == 1: 
            return num

print(hashTableSolution([2,2,1]))
print(hashTableSolution([4,1,2,1,2]))
print(hashTableSolution([1]))
        
#list methods => time complexity O(n2), space complexity O(n)
  #iterate over nums
    #if num not in new list append it 
    #if num already in list delete it 
    #return result of .pop() 

def singleNumberList(nums):
    n = []

    for num in nums:
        if num not in n:
            n.append(num)
        else:
            n.remove(num)

    return n.pop()
            
print(singleNumberList([2,2,1]))

from collections import Counter 

def sort_by_occurrence(inp):
    
    """ fist method: Couner.most_common() + list comprehension """
    list_by_occurrence_v1  = [ k for k, v in Counter(inp).most_common() for k in [k] * v ] 
    
    """ second method: Couner.most_common() + dict + list comprehension """
    memo = {} 
    list_by_occurrence_v2=[]
    for index, value in enumerate(inp): 
        memo.setdefault(inp[index], 0)
        memo[inp[index]] += 1 

    list_by_occurrence_v2 = [ k for k, i   in  (sorted(memo.items(), key=lambda x : x[0], reverse=True )) for k in [k] * i ] 

    """ third method: Couner.most_common() + for loop """
    list_by_occurrence_v3 = []
    for key, value in Counter(inp).most_common(): 
        for i in range(value): 
            list_by_occurrence_v3.append(key)
    
    return list_by_occurrence_v1, list_by_occurrence_v2, list_by_occurrence_v3
 

print(sort_by_occurrence([4,5,3,5,2,3,5])) # [5, 5, 5, 3, 3, 4, 2]

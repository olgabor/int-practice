# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

def numRescueBoats(people, limit):
    people.sort()
    boats = 0 
   
    left = 0 
    right = len(people)-1
    
    while left <= right: 
        
        if people[left] + people[right] <= limit: 
            boats += 1
            left +=1 
            right -=1 
            
        elif people[right] <= limit:

            boats += 1
            right -= 1 
            
        elif people[left] <= limit: 
            boats += 1 
            left += 1 
        
    return boats 

#cleaner version 
def numRescueBoatsClean(people, limit):
    people.sort()
    boats = 0 
   
    left = 0 
    right = len(people)-1
    
    while left <= right: 
        if(left == right):
            boats += 1 
            break 

        if people[left] + people[right] <= limit: 
            left +=1 

        right -=1 
        boats += 1
            
    return boats 

print(numRescueBoats([3,2,2,1], 3))
print(numRescueBoats([1,2], 3))
print(numRescueBoats([3,5,3,4], 5))
print(numRescueBoats([2,2], 6))


print(numRescueBoatsClean([3,5,3,4], 5))
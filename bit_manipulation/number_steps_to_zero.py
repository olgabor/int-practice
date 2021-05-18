
#--------------------------------------------------------------------------------
#Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

#Input: num = 14
#Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.
#--------------------------------------------------------------------------------

def numberOfSteps(num):
    #return number of steps to reduce it to zero 
    steps = 0 
    #if number is even  => devide by 2 

    #if number is off => substract 1 
    while num > 0:
        if num % 2 == 0: #number is even 
            new = num / 2 
            steps += 1 
            num = new 
        else: 
            new = num - 1 
            num = new 
            steps += 1 
        
    return steps 

print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(123))





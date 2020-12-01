#You're given strings J representing the types of stones that are jewels, 
# and S representing the stones you have.  Each character in S is a type of stone you have.  
# You want to know how many of the stones you have are also jewels.

#The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def numJewelsInStones(J, S): 

    count = 0 
    # letterlist = [ch for ch in J] #converts the string to list with list comprehension

    for i in S: 
        if i in list(J):
            count += 1 
  
    return f'{count} stones are also jewels.'

print(numJewelsInStones(J='aA', S='aAAbbbb'))
print(numJewelsInStones(J='z', S='ZZ'))

#recursive version 
def numJewelsInStonesRecursion(J, S): 
    count = 0 
    if len(S) == 0:
        return count 
    else: 
        for i in S: 
            if i in list(J):
                return count +  numJewelsInStonesRecursion(J, S[1:])

print(numJewelsInStones(J='aA', S='aAAbbbb'))
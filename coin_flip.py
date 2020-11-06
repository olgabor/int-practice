
#write a program to find out how often streak of six heads or streak of six tails 
# comes up in a randomly generated list of heads and tails

import random 
numberOfStreaks = 0 

heads_count = 0 
tails_count = 0 

for experiment in range(10000):
    guess = random.randint(0, 1) 
    if guess == 1: 
        heads_count +=1 
        tails_count = 0 
        if heads_count == 6: 
            numberOfStreaks +=1 
            heads_count == 0 
    else: 
        tails_count +=1 
        heads_count = 0 
        if tails_count == 6: 
            numberOfStreaks +=1 
            tails_count == 0 

print(numberOfStreaks)
print('Chanse of getting the streak : %s%%' %  (numberOfStreaks / 100))




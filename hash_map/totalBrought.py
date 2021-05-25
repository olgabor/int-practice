allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'sandwitch': 2, 'apples': 2}, 
             'Carol': {'cups': 3, 'pies': 1}
             }

def totalaBrought(guests, item): 
    numBrought = 0 
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0 )
    return numBrought

print( ' Apples '  + str(totalaBrought(allGuests, 'apples')))
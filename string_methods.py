spam = 'Hello, world!'
print(spam[0:5])
print(spam[:5])
print(spam[-5:])
print(spam[:-5])
print(spam[7:])
print(spam[-2:])
print(spam[:-2])

#validate user imput examples 
while True: 
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break 
    print('Please enter a number of your age.')

while True: 
    print('Select a new password (letter and numbers only):')
    password = input()
    if password.isalnum():
        break 
    print('Password can only have letters and numbers.')

#use the string methods to display tabular data 
def printPicnic(itemsDict, lefWidth, rightWidth):
    print('PICNIC ITEMS'.center(lefWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(lefWidth, '.') + str(v).rjust(rightWidth))
        
picnicItems = {'sandwitches': 4, 'apples': 12, 'cups': 4, 'cookes': 8000 }
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 4)

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
print(spam.strip('Spam'))

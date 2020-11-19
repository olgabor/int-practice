# multi-clipboard program 

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""", 
        'upspell': """ Would you consider making this a monthly donation?"""}

import sys, pyperclip 

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy pharase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line argument is the keypharase 

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipbord.')
else: 
    print('There is no text for ' + keyphrase)




def tweet():
    feed = {}
    
    while True: 
        print('Enter a username')
        username  = input()
        
        menu = ['new message', 'print feed', 'new user' ]

        print('Choose from options : new message, print feed, new user')
        option = input()

        if option == menu[0]: 
            #add new message 
            print('Enter your message')
            message = input()
            if username not in feed:
                feed[username] = [message]
            else: 
                feed[username].append(message)

        if option == menu[1]:
            #print feed 
            if username not in feed:
                print(f"you have no tweets {username}")
            else: 
                print(str(feed[username])) 


        if option == menu[2]: 
             print('Enter a username')
             username  = input()

        elif option not in menu: 
            print("MAKE choice")
        
        for key, value in  feed.items():
            print ("username",  key, "has tweets : ", str(value))

tweet()

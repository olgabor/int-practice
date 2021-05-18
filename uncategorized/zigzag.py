import time , sys 
indent = 0 #  how many spaces to indent 
indentIncreasing = True #Whatever the indentation is incresing or not 

try: 
    while True: # the main program loop 
        print(' ' * indent, end='')
        print('*********')
        time.sleep(0.5)

        if indentIncreasing: 
            #increase th enumber of spaces: 
            indent = indent + 1 
            if indent == 20: ≈
                # Change direction 
                indentIncreasing = False
        
        else: 
            #Decrease the number of spaces 
            indent = indent - 1 
            if indent == 0: 
                #Change direction 
                indentIncreasing = True 

except KeyboardInterrupt: 
    sys.exit()
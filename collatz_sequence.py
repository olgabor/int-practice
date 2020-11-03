# import sys 

# def collatz(): 
#     outcome =  0 
#     while outcome != 1:
#         try: 
#             number = input('Enter the number: ')

#             if int(number) % 2 == 0:
#                 outcome == int(number) // 2 
#             elif int(number) % 2 == 1:
#                 outcome ==  (3 * (int(number) + 1 ))

#         except ValueError:  
#             print('please enter a number')



# print(collatz())

def collatz(number):
    if number % 2 == 0:
        return number // 2 
    elif number % 2 == 1: 
        return 3 * (number + 1)


number = input('type number: ')

value = collatz(int(number))
while value !=1: 
    value = collatz(int(number))
    print(collatz(int(number)))

    

    





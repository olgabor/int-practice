#write  calculator function which takes input from console and computes the result 

def calculator():
    total = 0 
    
    while True: 
        try: 
            print('enter a FIRST number')
            first_number = input()
            print('enter a SECOND number')
            second_number = input() 
            first_number, second_number = float(first_number),  float(second_number)


            print('Enter an operation "+" , "-", "/", "*", "%"' )
            operation = input() 
            operation_inputs = ["+" , "-", "/", "*", "%"] 

            if operation == "+":
                total = float(first_number) + float(second_number)
                print(total)
            if operation == "-":
                total = float(first_number) - float(second_number)
                print(total)
            if operation == "/":
                total = float(first_number) / float(second_number)
                print(total)
            if operation == "*":
                total = float(first_number) * float(second_number) 
                print(total)

            if operation not in operation_inputs: 
                print('Enter VALID operation ')
        
        except ValueError:
            print("NOT A NUMBER ")
   
    return total
            
#Given a string s representing an expression, implement a basic calculator to evaluate it. 
# implenent the solution using stacks 
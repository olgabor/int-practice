def fizzBuzz(n):
    # Write your code here
    for i in range(1,n +1 ): 
        if i % 3 == 0 and i % 5 == 0: 
            print('FizzBuzz')
        elif i % 3 == 0: 
            print('Fizz')
        elif i % 5 == 0 : 
            print('Buzz')
        else:
           print(i)
        
print(fizzBuzz(15))

# Expected output: 
# # 1
# 2
# FizzBuzz
# 4
# Buzz
# FizzBuzz
# 7
# 8
# FizzBuzz
# Buzz
# 11
# FizzBuzz
# 13
# 14
# FizzBuzz
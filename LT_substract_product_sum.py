#Given an integer number n, return the difference between the product of its digits and the sum of its digits.
#example: Input: n = 234 Output: 15 

def subtractProductAndSum(n):
    
    if type(n) in [str, float]:
        return 'Only positive integers allowed' 

    product = 1
    product_sum = 0
    
    tmp = 0 
    while n > 0 :
        tmp = n % 10
        product = tmp * product 
        product_sum += tmp
        n = n //10

    return product - product_sum 

print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))
print(subtractProductAndSum('number'))
print(subtractProductAndSum(9.8))
#Python comprehensions

nums = [1,2,3,4,5,6,7,8,9,10]

#save only odd numbers in mew list 
my_list = [n for n in nums if n%2 == 0]
print(my_list)

#with lambda 
my_list_with_lambda = map(lambda n: n%2 == 0, nums) 

# save a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list_with_tuples = []
for letter in 'abcd': 
    for num in range(4): 
        my_list_with_tuples.append((letter, num))

# comprehension 
my_list_with_tuples_compr = [ (letter, number) for letter in 'abcd' for number in range(4)]
print(my_list_with_tuples_compr)

##############################################################
#Dictionary comprehensions 
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool' ]

my_dict = {}
for name, hero in zip(names, heros): 
    my_dict[name] = hero 
print(my_dict)

my_dict_coprehension = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict_coprehension)

##############################################################
#Set comprehensions
num = [1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 6, 7, 9]
my_set = set()
for n in num: 
    my_set.add(n)

my_set_coprehension = { n for n in num}
print(my_set, my_set_coprehension)

# comprehension with Counter to return list by occurrence 

from collections import Counter 
nums = [4, 5, 3, 5, 2, 3, 5]

nums = [ number for number, occur in Counter(nums).most_common() for number in [number] * occur ]
print(nums)
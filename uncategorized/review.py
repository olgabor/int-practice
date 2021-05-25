
nums = [3,5,8,8,2,9,9,2,0,0,5]
accounts = [[2,8,7],[7,1,3],[1,9,5]] 
from collections  import Counter 


s = "A man, a plan, a canal: Panama"
t = "nagaram" 
people = [3, 2, 2, 1 ]
limit = 3 
arr = [0,3,2,9,2,1] 

#  cards = [1,4,5]
# total = 12
# output = 3 
# explanation = 12 = 4 +4 +4  

# def mountain_array(nums, target):

    
# print(mountain_array(nums, target))

# DELETE Node 
# Remove N-th NODE 
# Reverse Linked list 
# Merge Two sorted lists 
# Palindrome linked list 
# Linked lIsts Cycle  

class Node: 

    def __init__(self, node, next_node=None):
        self.node = node
        self.next_node = next_node 


# class LinkedList: 
#     def __init__(self, head=None): 
#         self.head = head 

#     def insert(self, value): 
#         node = LinkedList(value)

#         if self.head ==  None: 
#             self.head = node 
#             return

#         current_node = self.head 

#         while True: 
#             if current_node.next_node = None:
#                 current_node.next_node = 
nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
def max_subarray(nums): 
    
    max_sum = 0 
    for i in range(len(nums)): 
        cur_sum = nums[i]  
        for j in range(i , len(nums)): 
            cur_sum += nums[j] 
            
            max_sum = max(cur_sum, max_sum )
            
              # iterate through list and add numbers continuously for each index 
    # write down the sum for each iteration and compare it with max sum using max 

    return max_sum
# print(max_subarray(nums)) 
def reverse(s): 
    tmp = ''
    
    if len(s) == 0: 
        return s 
    elif len(s) < 1: 
        return s
    elif len(s) == 0: 
        return ''
    else: 
        tmp = s[-1]
        tmp = tmp + reverse(s[:-1])
        return tmp 

    # tmp = ''  
    # if type(s) != str:
    #     # raise ValueError ('This is not a string')
    #     return 'This is not a string'
    # elif len(s) == 0: 
    #     return  ''
    # elif len(s) < 1: 
    #     return s 
    # else: 
    #     tmp = s[-1]
    #     tmp = tmp + reverse(s[:-1])  
    #     return tmp 
    # #base case 
    #  

# print(reverse('hello world'))


def decode(s):


    i = 0
    res = ''
    print(s[len(s) -1])
    while( i < len(s) -1) :

        # Counting occurrences of s[i]
        count = 1

        while s[i] == s[i + 1] :
            i += 1
            count += 1

        res += (str(count)) + s[i]
        
        i += 1

        if i == len(s) -1:         
            res += str(1) + s[i]
            break 

        
   
    return res

print(decode('wwwbbbw'))
print(decode('aabbcde'))


#Find most frequent element in a list 

def mostFreq(nums):
  if len(nums)==0: return ''
  elif len(nums)==1: return nums[0]

  d = {}
  counter = 0 
  response = ''

  for num in nums:
    if num not in d:
      d[num] = 1 
    else:
      d[num] += 1
    
    # keep track of largest counter 
    # every time the current number appears more than counter: 
         # replace the counter with this value 
         # assign the number to respone 
    if d[num] > counter:
        counter = d[num]
        response = num 
    
  return response 
  
## another option is to use list comprehension and lambda 
#   # use list comprehension to convert dictionary to list with tuples 
#   dict_list = [(k, v) for k, v in d.items()]
#   #sort the list with lamdba 
#   dict_list = sorted(dict_list, key = lambda x: -x[1])
#   print('the most freq', dict_list[0][0])

# print(mostFreq([2, 1, 2, 2, 1, 3, 5,5,5,5,5,4,5,4,7]))

# Use counter 
  # counter will keep track on how often each elemt appears in list: Counter({5: 6, 2: 3, 1: 2, 4: 2, 3: 1, 7: 1}) 
  # all elements in counter are placed in accending order 
  # use most_common method which returns the number of most common elements as value passed to method 
  # return .most_common(1)[0][0] to return first value 
 
from collections import Counter

def mostt_fr(nums):
  counted = Counter(nums)
  most_common = counted.most_common(1)[0][0]
  
  ## OR iterate over elements in most_most common(1) and retun number 
  # for k,v in most_common:
  #   return k 
  return most_common
	
# print(mostt_fr([2, 1, 2, 2, 1, 3, 5,5,5,5,5,4,5,4,7]))

#count() Returns the number of elements with the specified value
def most_freq(List):
    counter = 0
    num = List[0]

    for i in List:
        #count() Returns the number of elements with the specified value
        curr_frequency = List.count(i)
        #print("the output from List.count(i){} for {}".format(curr_frequency, i))
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

List = [2, 1, 2, 2, 1, 3, 5,5,5,5,5,4,5,4,7]
# print(most_freq(List))


def most_freq2(List):
  dict = {}
  max_count, itm = 0, ''
  for item in reversed(List):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= max_count:
            max_count = dict[item]
            itm = item

  return(itm)

List = [2, 1, 2, 2, 1, 3, 5,5,5,5,5,4,5,4,7]
# print(most_freq2(List))

## find the most requent value with .setdefault dictionary method: 
  # initiate empty dictionary, counter and most_common variables  
  # start the for loop 
  # for each number in the list .setdefault(list number , zero) will set {list_number, zero} to each number in the list 
  # as item appears in list again increase the value by 1 in dictionary d[list_number] += 1
  # at each itearation compare the count variable to d[list_number] 
    # if it is smaler replace the counter value with d[list_number] 
    # replace the value of most_common with curernt number in the list 
def mostCommonDefault(List): 
  d = {}
  count = 0
  most_common = 0
  
  for i in List:
    d.setdefault(i, 0)
    d[i] += 1 
    if count < d[i]: 
      count = d[i]
      most_common = i
  
  return most_common

print(mostCommonDefault([2, 1, 2, 2, 1, 3, 5,5,5,5,5,4,5,4,7]) )
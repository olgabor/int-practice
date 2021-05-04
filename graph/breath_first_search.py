from collections import deque

graph = {
    'you': ['alice', 'bob', 'claire'], 
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'], 
    'claire': ['thom', 'jonny'], 
    'anuj': [], 
    'peggy': [], 
    'thom': [], 
    'jonny': []
}


def search(name): 
    search_queue : deque()
    search_queue += graph[name]
    searched = []
    while search_queue: 
        person = search_queue.popleft() 
        if person_is_seller(person):
            print (person , 'is a mango seller!')
            return True
        else:
            search_queue += graph[person] 
            searched.append(person)

    return False
    


print(search('you'))
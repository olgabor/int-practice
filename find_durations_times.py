activity = [(1, '@login', None),
(5, '@startVideo', 'Bob'),
(20, '@startVideo', 'Thomas'),
(66, '@stopVideo', 'Thomas'),
(70, '@startVideo', 'Lily'),
(75, '@stopVideo', 'Bob'),
(78, '@stopVideo', 'Lily'),
(100, '@logout', None),
(150, '@login', None),
(160, '@startVideo', 'Thomas'),
(205, '@stopVideo', 'Thomas'),
(210, '@logout', None) ]


def loginLogoutDuration(activity):
    duration = 0 
    for i in range(len(activity)):
        if activity[i][1] == '@login': 
            duration -=  activity[i][0] 
        if activity[i][1] == '@logout' :
            duration +=  activity[i][0] 
     
    end = 0 
    stream_time = 0
    start = 0 
    for i in range(len(activity)):

        if activity[i][1] == '@startVideo':

            for j in range(i +1, len(activity)): 
                if activity[j][1] == '@startVideo' and start < 2:

                    stream_time -= activity[j][0]
                    start += 1 
                if activity[j][1] == '@stopVideo' and end < 2  :

                    end += 1 
                    stream_time += activity[j][0]
  
               
                
    return duration , stream_time 
            
        # if activity[i][1] == '@stopVideo': 
        #     print(activity[i][2])

print(loginLogoutDuration(activity))

 
# (5, '@startVideo', 'Bob'), start 
# (20, '@startVideo', 'Thomas'), start 
# (70, '@startVideo', 'Lily') start 


# (75, '@stopVideo', 'Bob'), stoip 
# (78, '@stopVideo', 'Lily'), stop 
# (66, '@stopVideo', 'Thomas'), stop 
# Question
# Given a class of Interval, which has start and end point as integer, and a list of such Intervals.
# We want to insert another interval into this list of Intervals.
#
# eg: <4,7><10,15><20,21>
#
# # insert <5, 8>, get <4,8><10,15><20,21>
# > mergeIntervals((5,8), [(4,7),(10,15),(20,21)])
# > [(4,8),(10,15),(20,21)]
#
# # insert <16,17>, get <4,8><10,15><16,17><20,21>
# > mergeIntervals((16,17), [(4,7),(10,15),(20,21)])
# > [(4,8),(10,15),(16,17),(20,21)]
#
# # insert <1,30>, get <1,30>
# > mergeIntervals((1,30), [(4,7),(10,15),(20,21)])
# > [(1,30)]

def mergeIntervals(interval, list_of_intervals):

        intervals = [[]]
     #   print("[[]]", type(intervals))

        #combaning all intevals to one list

        intervals = interval + list_of_intervals

        #doing sort
        intervals.sort(key=lambda item: item[0])
        i = 0
        while (i + 1) < len(intervals):

            curr_a = intervals[i]
            next_a = intervals[i+1]

            #is overlaping?
            if curr_a[1] >= next_a[0]:

                #The last element of the first array should be set up
                intervals[i][1] = max(curr_a[1], next_a[1])

                # removing unnesary one
                intervals.pop(i+1)
            else:
                i += 1
        return intervals
list_of_intervals = [[4,7],[10,15],[20,21]]
#interval = [[5,8]]
interval = [[16,17]]
#interval = [[11,12]]
print(mergeIntervals(interval, list_of_intervals))
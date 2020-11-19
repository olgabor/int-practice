# -----------------------------------------------------------
#write a fucntion printTable that takes lis of lists of strings and displays 
# it in a table with each column right adjusted. 

#the fucntion should print: 
#      apples Alice  dogs
#     oranges Bob    cats
#    cherries Carol moose
#      banana David goose
# -----------------------------------------------------------

tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']] 

def printTable(tableData):
    
    #find the max value of each inner string and write it dowm 
    # to colWidth list create colWidth list with integers, equivalent to len(tableData)
    colWidth = [0] * len(tableData)
    

    #iterate over each element in inner list replace the value in colWith if length of
    #  inner list value is larger than colWidth value corresponding same index
    for i in range(len(tableData)):
        for k in range(len(tableData[i])):
            if len(tableData[i][k]) > colWidth[i]: 
                colWidth[i] = len(tableData[i][k])

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):

            #print each value left adjusting it within maximum lenth of items in inner list 
            print(tableData[j][i].rjust(colWidth[j]), end=' ') 
        print('')
        
print(printTable(tableData))



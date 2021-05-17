from typing import List

#sum up the items in matrix by diagonal without intersections (5 is not added 2 times) 
def summatrix(mat): 
    s = 0 
    index1 = len(mat) -1 
    for i in range(len(mat)):
        s += mat[i][i] # 0 0, 1 1, 2 1
        
        if mat[i][i] != mat[i][index1]: 
            s += mat[i][index1] # 0 2, 2, 2 
            
        index1 -= 1 
       
    return s 


mat = [[1,2,3],
       [4,5,6],
       [7,8,9,]] 

print(summatrix(mat))


#print matrix   #1 2 4 3 5 7 a 6 8 b c 9 d e f 
def printMatrix( mat):
  
  for col in range(len(mat) + len(mat[0])):

    start=col
    for row in range(len(mat)):
      #print (start, row)
      if (start<len(mat[0])) and (start>=0):
        print(mat[row][start])
      start -=1
  return True
  


mat = [[1,2,3, 'a', 'b'], [4,5,6, 'c', 'd'], [7,8,9, 'e', 'f']]
# printMatrix(mat)


# print the matrix with 1 4 2 3 5 7 8 6 a b c 9 e d f
def printMatrix( mat):
  
  flag = True
  for col in range(len(mat) + len(mat[0])):

    
    if flag:
      start=col
      for row in range(len(mat)):
        #print (start, row)
        if (start<len(mat[0])) and (start>=0):
          print(mat[row][start])
        start -=1
    else:
      start=col-len(mat)+1
      for row in range(len(mat)-1, -1, -1):
        #print (start, row)
        if (start<len(mat[0])) and (start>=0):
          print(mat[row][start])
        start +=1

    flag = not flag

  return True

mat = [[1,2,3, 'a', 'b'], [4,5,6, 'c', 'd'], [7,8,9, 'e', 'f']]
# printMatrix(mat)


#print matrix zigzag 
def print_spriral_matrix(m):

	if not m:
		return None

	start_row = 0
	start_col = 0
	end_row = len(m) - 1
	end_col = len(m[0]) - 1


	while start_row < end_row and start_col < end_col:

		# right
		for j in range(start_col, end_col):
			print(m[start_row][j], end = " ")

		# down
		for j in range(start_row, end_row):
			print(m[j][end_col], end = " ")

		# left
		for j in range(end_col, start_col, -1):
			print(m[end_row][j], end = " ")

		# up
		for j in range(end_row, start_row, -1):
			print(m[j][start_col] , end = " ")

		start_col += 1
		start_row += 1
		end_col -= 1
		end_row -= 1

	if start_col == end_col and start_row == end_row:
		print(m[start_row][start_col])
	elif start_row < end_row:
		for j in range(start_row, end_row + 1):
			print(m[j][end_col], end = " ")
	elif start_col < end_col:
		for j in range(start_col, end_col + 1):
			print(m[start_row][j], end = " ")


	print()
	print("-----------------")

def print_m(m):
	for r in m:
		print(r)




m = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]
print_m(m)
print_spriral_matrix(m)

m = [
	[1,2,3,4,5,6,7],
	[8,9,10,11,12,13,14],
	[15,16,17,18,19,20,21]
]
print_m(m)
print_spriral_matrix(m)


m=[
	[1],
	[2]
]
print_m(m)
print_spriral_matrix(m)


m = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]
print_m(m)
print_spriral_matrix(m)

m=[
	[1,2],
	[3,4]
]
print_m(m)
print_spriral_matrix(m)
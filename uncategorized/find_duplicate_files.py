'''
Given a directory, find *all* duplicate files in the directory and sub directories
For example given dirA -> dirB -> fileA
                      '-> fileB
                      '-> dirC -> fileC
                      '-> fileD
                      '-> fileE
where fileA and fileB and fileE are duplicate and fileD and fileC are duplicate, your output should look like:
[(dirA/dirB/fileA,dirA/fileB,dirA/fileE),(dirA/dirC/fileC,dirA/fileD)]
'''

import os
import os.path
import hashlib
from collections import defaultdict
input_path = '/Users/art'



# fileList = []
# resultList = []
# mydict = defaultdict(list)

# def findDuplFilesbyConts(input_path):



# # List all files in directory using pathlib
#     allFiles = getFullFileList(input_path)
#     #pdb.set_trace()
#     for file in allFiles:
#         currHash = hashlib.sha256(file.encode('utf-8')).hexdigest()
#         #currHash = hashlib.md5(file).hexdigest()
       
#         mydict[currHash].append(file)
#     currHash)


#     return mydict

# def printDuplicates(mydict):
    

#     for key, value in mydict.items():
#         if len(value) > 1:
#             print ("Several files duplicated files where found!")
#         #    print (value)
#             print(*value.split(', '), sep='\n')



# def getFullFileList(input_path):
#     # create a list of file and sub directories
#     # names in the given directory

#     listOfFile = os.listdir(input_path)

#     allFiles = list()
#     # Iterate over all the entries
#     for entry in listOfFile:
#         # Create full path
#         fullPath = os.path.join(input_path, entry)
#         # If entry is a directory then get the list of files in this directory
#         if os.path.isdir(fullPath):
#             allFiles = allFiles + getFullFileList(fullPath)
#         else:
#             allFiles.append(fullPath)

#     return allFiles
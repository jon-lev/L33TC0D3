import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
lineStr = ""
for line in sys.stdin:
    lineStr = line.strip().split(":")

numbers = lineStr[0]
positions = lineStr[-1]
#split numbers by spaces into an array
numbers = numbers.split(" ")

#Remove last space in array
numbers = numbers[:-1]

#find the position(s) by splitting at -
positions = positions.split('-')
finalPos = []

#have to deal with weird splitting problem when there is more than 1 swap
for pos in positions:
    if "," in pos:
        splits = pos.strip().split(",")
        finalPos.append(splits[0])
        finalPos.append(splits[1])
    else:
        finalPos.append(pos.strip())
 
for i in range(len(finalPos) - 1):
    index1 = int(finalPos[i])
    index2 = int(finalPos[i+1])
    #finally get to swap after parsing the input
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

print(*numbers)


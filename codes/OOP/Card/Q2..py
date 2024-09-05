x = [0 for i in range(100)]
print(x)

import random
arrayData = [[0]*10 for i in range(10)] # INTEGER
for x in range(0, 10):
    for y in range(0, 10):
        arrayData[x][y] = random.randint(1, 100)
print(arrayData)        
def printArray(arrayData):
    for x in range(0, 10):
        for y in range(0, 10):
            print(arrayData[x][y], " ", end='')
            print("")                                
print("before")
printArray(arrayData)

ArrayLength = 10
for x in range(0, ArrayLength):
    for y in range(0, ArrayLength-1):
        for z in range(0, ArrayLength-y-1):
            if (arrayData[x][z] > arrayData[x][z+1]):
                TempValue = arrayData[x][z]
                arrayData[x][z] = arrayData[x][z+1]
                arrayData[x][z+1] = TempValue
                

print("after")
printArray(arrayData) 
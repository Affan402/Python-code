#DECLARE arrayData : ARRAY [0:9] OF INTEGER
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(ValueToFind):
    global arrayData
    index = 0
    while index < 10:
        if arrayData[index] == ValueToFind:
            return True
        else:
            index = index + 1
    
    return False
    
y = linearSearch(int(input("Enter Value To Find:")))

if y == True:
    print("Value found... ")    
else:
    print("Value not Found")    
    
    
def bubbleSort():
    global arrayData
    temp  = 0
    for x in range(0, 9):
        for y in range(0, 9-x):    
            
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
                
bubbleSort()   
print(arrayData)     


#DECLARE arrayData : ARRAY [0:9] OF INTEGER
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
index = 0
def Linearsearch(newItem):
    global arrayData,index
    
    while index < 9:
        if arrayData[index] == newItem:
            return True
        else:
            index += 1
    return False

y = Linearsearch(int(input("Enter a value to search: "))) 
if y == True:
    print("Value found at", index)           
else:
    print("Value not found..")    
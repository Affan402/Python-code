StackPointer = 0
StackData = [0] *10

def printArray():
    global StackPointer, StackData
    print("StackPointer:",StackPointer)
    
    for x in range(0, 10):
        print(StackData[x])

def Push(item):
    global StackPointer, StackData
    if StackPointer == 10:
        return False
    else:
        
        StackData[StackPointer] = item
        StackPointer += 1
        return True

for x in range(0, 11):
    num = int(input("Enter number to add: "))
    if Push(num) == True:
        print("Item added")
    else:
        print("Item not added")
printArray()                  

def Pop():
    global StackData, StackPointer
    
    if StackPointer == 0:
        return -1
    else:
        x = StackData[StackPointer-1]
        StackData[StackPointer-1] =0
        StackPointer -= 1
        return x
        
Pop()
Pop()
printArray()        
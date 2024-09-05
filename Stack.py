myData = [0] * 5
tos = -1

def Push(newitem):
    global myData, tos
    
    if tos == 4:
        print("Stack is full")
        return False
    else:
        tos = tos + 1
        myData[tos] = newitem
        return True

def Display():
    
    global myData, tos
   
    for index in range(0,5):
       print(myData[index])
    print("Top of stack:",tos)

def Pop():
    
    global myData, tos
    if tos == -1:
        print("Stack is empty")
        return False
    else:
        myData[tos] = 0
        tos = tos -1
        return True                    
    
Push(5)    
Push(6)
Push(8)
Pop()

Display()
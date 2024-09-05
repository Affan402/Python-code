myData = [0] *5
head = -1
tail = -1

def Enqueue(newitem):

    global myData, head, tail
    
    if (head==0 and tail == 4) or (head == tail + 1):
        print("Queue is full ")
        return False
    else:
        if head == -1 and tail == -1:
            head = 0 
            tail = 0
        elif tail == 4:
            tail =0
        else:
            tail = tail + 1
        
        myData[tail] = newitem                                                
        return True

def Dequeue():
    
    global myData, head, tail
    
    if head == -1 and tail == -1:
        print("Queue is empty ")
        return False
    else:
        myData[head] = 0
        
        if head == tail:
            head = -1 
            tail = -1
        elif head == 4:
            head =0 
        else:
            head = head + 1
        return True
    
def Display():
    
    global myData, head, tail                
    
    for index in range(0,5):
        
        print(myData[index])
    
    print("Head", head)
    print("Tail", tail)
    
Enqueue(2)
Enqueue(9)    
Enqueue(4)
Dequeue()
Enqueue(8)
Enqueue(7)

Display()
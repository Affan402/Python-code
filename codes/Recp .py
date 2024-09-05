# DECLARE myData : ARRAY [0:9] OF INTEGER 
myData = [3, 8, 2, 9, 50, 28, 16, 25, 78, 18]

def linearSearch(Num):
    global myData
    index = 0
    found = False

    while found == False and index < 10:
        
        if Num == myData[index]:
            found = True
        else:
            index += 1

    if found == True:
        return index 
    else:
        return -1
        
x = linearSearch(78)

if x == -1 :
    print("Number not found...")
else:
    print("Number found at", x)
    
def BinarySearch(Num):
    
    global myData
    
    top = 0
    bottom = 9
    found = False
    
    while top<= bottom and found == False:
        middle = int((top+bottom)/2)
        
        if Num == myData[middle]:
            found = True
        elif Num > myData[middle]:
            top = middle + 1
        else: 
            bottom = middle -1 
    if found == True:
        return middle
    else:
        return -1
    
x = BinarySearch(50)

if x == -1:
    print("Number not found ")
else:
    print("Number found at",x)        
    

def BubbleSort():
    global myData
    
    n=9
    
    for x in range(n):
        for y in range(n-x):
            if myData[y] > myData[y+1]:
                temp = myData[y] 
                myData[y] = myData[y+1]
                myData[y+1] = temp                                     
                

print(myData)      

def InstructionSort():
    global myData
    NumberOfItmes = len(myData)
    for pointer in range(1,NumberOfItmes):
        ItemsToBeInserted = myData[pointer]
        CurrentItem = pointer -1
        
        while myData[CurrentItem] > ItemsToBeInserted and CurrentItem > -1:
            myData[CurrentItem+1] = myData[CurrentItem]
            CurrentItem = CurrentItem -1
            
        myData[CurrentItem+1] = ItemsToBeInserted
        
InstructionSort()
print (myData)   

#STACK:
# DECLARE myList :ARRAY [0:9] OF INTEGER
# DECLARE tos : INTEGER

myList = [0]*10
tos = -1

def Push(NewItem):
    global myList, tos
    if tos == 9:
        print("Stack is full...")
        return False
    else:
        tos = tos +1
        myList[tos]=NewItem
        print(NewItem,"is pushed..")
        return True
Push(7)
Push(8)
Push(5)
Push(35)
Push(77)
    
def Pop():
    global myList, tos
    if tos == -1:
        print("Stack is empty..")
        return False
    else:
        print(myList[tos],"is popped..")
        myList[tos]=0
        tos= tos -1
        return True
    
def Display():
    global myList, tos
    for index in range(10):
        print(index, "|",myList[index])
    print("Top of Stack:", tos)
Display()
def Menu():
    global myList, tos
    
    choice = 0
    
    while choice != 4:
        print("1 - Push")
        print("2 - Pop")
        print("3 - Display")            
        print("4 - Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            x = int(input("Enter a value to push:"))
            Push(x)
        elif choice == 2:
            Pop()
        elif choice == 3:
            Display()
               
Menu()

# DECLARE myList :ARRAY [0:9] OF INTEGER
# DAECLARE head, tail :INTEGER
mylist1 = [0]* 10
head = -1 
tail= -1

def EnQueue(NewItem):
    global mylist1, head, tail
    if (head == 0 and tail == 9) or (head == tail + 1):
        print("Queue is full..")
        return False
    else:
        if head == -1 and tail == -1:
            head = 0 
            tail = 0 
        elif tail == 9:
            tail = 0
        else:
            tail = tail  + 1
            
        mylist1[tail] = NewItem
        print(NewItem, "is added into the queue")
        return True
        
def Dequeue():
    global mylist1, tail, head
    
    if head == -1 and tail == -1:
        print("Queue is empty")
        return False
    else:
        print(mylist1[head],"is removed from the queue")
        mylist1[head] = 0 
        
        if head == tail:
            head = -1
            tail == -1
        elif head == 9:
            head = 0
        else:
            head = head + 1
    return True        

def Display():
    global mylist1, head, tail
    
    for index in range(10):
        print(index, "|", mylist1[index])

    print("Head Pointer:", head)
    print("Tail Pointer:", tail)
    


def Menu1():
    global mylist1, head, tail
    
    choice = 0
    
    while choice != 4:
        print("1 - Enqueue")
        print("2 - Dequeue")
        print("3 - Display")
        print("4 - Exit")
        choice = int(input("Enter choice number: "))
        if choice == 1:
            x = int(input("Enter a value to Enqueue: "))
            EnQueue(x)
        elif choice == 2:
            Dequeue()
        elif choice == 3:
            Display()
            
#Menu1()           
   

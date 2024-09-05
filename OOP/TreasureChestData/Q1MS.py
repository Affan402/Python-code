class node:
    #DECLARE Data : INTEGER
    #DECALRE nextNode : INTEGER 
    def __init__(self, d, nN):
        self.Data = d
        self.nextNode = nN

#DECLARE linkedList : ARRAY [0:9] OF node       
linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
startPointer = 0
emptyList = 5

def outputNodes(linikedList, startPointer):
    currentPointer = startPointer
    while currentPointer != -1 :
        print(linikedList[currentPointer].Data)
        currentPointer = linkedList[currentPointer].nextNode
        
outputNodes(linkedList, startPointer)        

def addNode(linkedList, startPointer, emptyList):
    if emptyList == -1:
        return False
    else:
        newItem = int(input("Enter a new value to add: "))
        temp = linkedList[emptyList].nextNode
        linkedList[emptyList] = node(newItem, -1)
        currentPointer = startPointer
        
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode   
        linkedList[previousPointer].nextNode = emptyList
        emptyList = temp
        return True             
returnValue = addNode(linkedList, startPointer, emptyList)
if returnValue == True:
    print("The item successfully added")
else:
    print("Item not added, list full")
outputNodes(linkedList, startPointer)      

def adnode(linkedlist, startPointer, emptyList):
    if emptyList == -1:
        return False
    else:
        newItem = int(input("Enter a neew value to add: "))
        temp = linkedlist[emptyList].nextNode
        linkedList[emptyList] = node(newItem, -1)
        currentPointer = startPointer
        
        while currentPointer != -1:
            previouPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
            
        linkedList[previouPointer].nextNode = emptyList
        emptyList = temp
        
        return True
returnValue = adnode(linkedList, startPointer, emptyList)
if returnValue == True:
    print("The item successfully added")
else:
    print("Item not added, list full")
outputNodes(linkedList, startPointer)      
                        
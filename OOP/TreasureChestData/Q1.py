class node:
    #DECLARE Data : INTEGER
    #DECALRE nextNode : INTEGER 
    def __init__(self, theData, nextNodeNum):
        self.Data = theData
        self.nextNode = nextNodeNum
        
linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
startPointer = 0
emptyList = 5

def outputNodes(linikedList, currentPointer):
    while currentPointer != -1 :
        print(str(linikedList[currentPointer].Data))
        currentPointer = linkedList[currentPointer].nextNode
        
outputNodes(linkedList, startPointer)        

def addNode(linkedList, currenPointer, emptyList):
    dataToAdd = input("Enter the Value to add: ")
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        newNode = node(int(dataToAdd), -1)
        linkedList[emptyList] = newNode
        previousPointer = 0
        while currenPointer != -1:
            previousPointer = currenPointer
            currenPointer = linkedList[currenPointer].nextNode
        linkedList[previousPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode
        return True


returnValue = addNode(linkedList, startPointer, emptyList)
if returnValue == True:
    print("The item successfully added")
else:
    print("Item not added, list full")
outputNodes(linkedList, startPointer)            
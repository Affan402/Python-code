myList = [50, 20, 70, 60, 10]

def bubblesort():
    
    global myList
    
    for x in range (0,4):
        for y in range (0,4-x):
            
            if myList[y] > myList[y+1]:
                
                temp = myList[y]
                myList[y] = myList[y+1]
                myList[y+1] = temp

def instuctionsort():
    
    global myList
    
    NumberOfItems = len(myList)
    
    for pointer in range(1,NumberOfItems):
        
        ItemToBeInserted = myList[pointer]
        
        CurrentItem = pointer - 1
        
        while myList[CurrentItem] > ItemToBeInserted and CurrentItem > -1:
            myList[CurrentItem + 1] = myList[CurrentItem]
            
            CurrentItem = CurrentItem -1
        
        myList[CurrentItem + 1] = ItemToBeInserted
        
instuctionsort()        
print(myList)
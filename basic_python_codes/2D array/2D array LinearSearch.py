myList = [["MINHAS" ,  5000], 
          ["RAFAY"  ,  8000], 
          ["ALI"    ,  6500], 
          ["SUNIL"  ,  7500], 
          ["SAM"    ,  9500]
          ]

def linearSearch(name):
    global myList
    index = 0
    position = -1
    
    while position == -1 and index < 5:
        if name == myList[index][0]:
            print(myList[index][0], myList[index][1])
            return index       
        else:
             index =index + 1
    
    print("Name not found...")
                 
    return position                    

linearSearch(input("Enter a name to search:"))
myList = [["MINHAS" ,  5000], 
          ["RAFAY"  ,  8000], 
          ["ALI"    ,  6500], 
          ["SUNIL"  ,  7500], 
          ["SAM"    ,  9500]
          ]

for x in range(0,4):
    for y in range(x+1,5):
        if myList[x][0] > myList[y][0]:
            
            tempName = myList[x][0]
            tempScore = myList[x][1]
            
            myList[x][0] = myList[y][0]
            myList[x][1] = myList[y][1]
            
            myList[y][0] = tempName
            myList[y][1] = tempScore
            
            
for index in range (0,5):
    print(myList[index][0], myList[index][1])
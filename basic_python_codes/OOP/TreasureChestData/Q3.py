class TreasureChest:
#part a
    # PRIVATE question : STRING
    # PRIVATE answer : INTEGER
    # PRIVATE points : INTEGER
    
    def __init__(self, q, a, p):
        self.__question = q
        self.__answer = a
        self.__points = p

#part c(i)

    def getQuestion(self):
        return self.__question    
#part c(ii)
    def checkAnswer(self, ans):
        if ans == self.__answer:
            return True
        else:
            return False
#part c(iii)        
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points) // 2
        elif attempts == 3 or attempts == 4:
            return int(self.__points) // 4
        else:
            return 0
                 

#part b
arraytreasure = [""] * 5

def readData():
    global arraytreasure
    index = 0
    myFile = open("TreasureChestData.txt", "r")
    line1 = (myFile.readline()).strip()
    
    while line1 != "":
        line2 = int((myFile.readline()).strip())
        line3 = (myFile.readline()).strip()
        
        arraytreasure[index] = TreasureChest(line1, line2, line3)
        index += 1
        
        line1 = (myFile.readline()).strip()
    myFile.close()

#part c(iv)    
readData()

qNo = int(input("Enter a question number between 1 & 5: "))

print(arraytreasure[qNo-1].getQuestion())

attempts = 1
correct = False

while correct == False:
    ans = int(input("Enter your answer:"))
    
    if arraytreasure[qNo-1].checkAnswer(ans) == True:
        correct = True
    else: 
        attempts = attempts + 1
        
print(int((arraytreasure[qNo-1]).getPoints(attempts)))

class treasurechest:
    #PRIVATE question : STRING
    #PRIVATE answer   : INTEGER
    #PRIVATE points   : INTEGER
    
    def __init__(self, q, a, p):
        self.__question = q
        self.__answer = a
        self.__points = p
        
    def getQuestion(self):
        return self.__question
    def checkAnswer(self, ans):
        if ans == self.__answer:
            return True
        else:
            return False
arrayTreasure  = [] * 5
def readata():
    global arrayTreasure
    index = 0
    myfile = open("TreasureChestData.txt", "r")    
    line1 = myfile.readline()
    
    while line1 != "":
        line2 = myfile.readline()
        line3 = myfile.readline()
        
        arrayTreasure[index] = treasurechest(line1, line2, line3)
        index+=1
        line1 = myfile.readline
        
    myfile.close()
    
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points) 
        elif attempts == 2:
            return int(self.__points) //2
        elif attempts == 3 or attempts == 4:
            return int(attempts) //4
        else:
            return 0
    
readata()
qno = int(input("Enter a question number between 1 and 5")) 

print(arrayTreasure[qno-1].getQuestion())

attempts =1
correct = False

while correct == False:
    if arrayTreasure[qno-1].checkAnswer(ans) == True:
        correct = True
    else:
        attempts += 1
        
print(arrayTreasure[qno-1].getPoints(attempts))

                
                       
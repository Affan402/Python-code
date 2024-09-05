myData = ["CS1001 Affan", "CS1002 ali", "CS1003 anus", "CS1004 hasan"]

myFile = open("filing.txt", "w")

for index in range(0,4):
    myFile.write(myData[index] + "\n")
    
myFile.close()    



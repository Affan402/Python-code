def searchfile():
    myFile = open("filing.txt", "r")

    studentID = input("Enter a StudentID: ") 

    found = False

    info = myFile.readline()

    while info != "" and found == False:
        if studentID == info[0:6]:
            found = True
        else:
            info = myFile.readline()
                
    if found == True:
        print(info)
    else: 
        print("Data not found")
        
    myFile.close()    
    
def checkID(searchID):
    fileRead = open("filing.txt", "r")
    
    info = fileRead.readline()
    while info != "":
        if searchID == info[0:6]:
            fileRead.close()
            return True
        else:
            info = fileRead.readline()
    fileRead.close()
    return False


def addRecord():
    found = True
    
    while found==True:
        studentID = input("Enter StudentID: ")
        found = checkID(studentID)
        
    name = input("Enter name: ")
    info = studentID + " " + name + "\n"
    
    myFile = open("filing.txt", "a")
    myFile.write(info)
    myFile.close()


addRecord()   

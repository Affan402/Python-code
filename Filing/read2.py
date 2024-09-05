myFile = open("filing.txt", "r")

studentID = [""] * 10 
name = [""] * 10
index = 0

info = myFile.readline()

while info != "":
    studentID[index] = info[0:6]
    name[index]  = info[7:].strip()
    index +=1
    
    info = myFile.readline()
    
myFile.close()    

print(studentID)
print(name)
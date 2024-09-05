myFile = open("filing.txt", "r")

info = myFile.readline()

while info != "":
    print(info.strip())#strip will remove \n command agli line mai print nhi karay ga
    info = myFile.readline()
    
myFile.close()    

MyArray = [] # 25 elements INTEGER
try:
    DataFile = open("Data.txt",'r')
    for Line in DataFile:
        MyArray.append(int(Line))
    DataFile.close()
except IOError:
    print("Could not find file")


def PrintArray(Myarr):
    print(Myarr)
    
PrintArray(MyArray)

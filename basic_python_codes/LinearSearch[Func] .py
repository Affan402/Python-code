# DECLARE myData : ARRAY [0:9] OF INTEGER 
myData = [3, 8, 2, 9, 50, 28, 16, 25, 78, 18]

def linearSearch(Num):
    global myData
    index = 0
    found = False

    while found == False and index < 10:
        
        if Num == myData[index]:
            found = True
        else:
            index += 1

    if found == True:
        return index 
    else:
        return -1
        
x = linearSearch(3)

if x == -1 :
    print("Number not found...")
else:
    print("Number found at", x)
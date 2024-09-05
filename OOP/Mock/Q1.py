#DECLARE ErrCode : [0:10] AS INTEGER
#DECLARE ErrText : [0:10] AS INTEGER

ErrCode = [10 ,20, 25, 30, 40, 45, 50, 60, 80, 99]
ErrText = ["Invalid identifier name", "Bracket mismatch", "Undeclared variable", "Missing colon", "Missing semicolons", "Quotation mark mistakes", "Incorrect use of operators", "Incorrect path", "Data type mismatch", ""]

found = False
def OutputError(lNum, ENum):
    global found, ErrCode, ErrText
    for index in range(10):
        if ENum == ErrCode[index]:
            print(ErrText[index],"on line", lNum)
            found = True
            index = index + 1
    if found == False:    
        print("Unknown error on line",lNum)             
            
OutputError(34, 50)       

def SortArrays():
    global ErrCode
    n = 9
    
    for x in range(n):
        for index in range(n-x):
            if ErrCode[index] > ErrCode[index + 1]:
                temp = ErrCode[index]
                ErrCode[index] = ErrCode[index + 1]
                ErrCode[index + 1] = temp
                
                                                    
#DECLARE NumberQueue : [0:8] AS INTERGER
#DECLARE StartPointer, EndPointer : INTEGER

StartPointer = -1
EndPointer = -1    

NumberQueue = [0] * 8
def AddtoQueue(Number):
    global StartPointer, EndPointer

    TempPointer = EndPointer + 1

    if TempPointer > 7:
        TempPointer = 0
    if TempPointer == StartPointer:
        return False
    else:
        EndPointer = TempPointer
        NumberQueue[EndPointer] = Number
        return True
    
AddtoQueue(10)
AddtoQueue(9)
AddtoQueue(11)
AddtoQueue(12)
AddtoQueue(19)
AddtoQueue(18)
AddtoQueue(15)
AddtoQueue(14)
AddtoQueue(8)
print(NumberQueue)    

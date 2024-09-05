myData = [ 9, 13, 22, 33, 44, 56, 64, 74, 87, 98]

def binarySearch(value):
    
    global myData
    
    top = 0
    bottom = 9
    
    while top <= bottom:
        middle = int(top+bottom/2)
        
        if value == myData[middle]:
            return middle
        elif value > myData[middle]:
            top = middle + 1
        else:
            bottom = middle - 1
    return -1

num = int(input("En           ter number to search: "))
x = binarySearch(num)
if x == -1:
    print("Number not found......")
else:
    print("Number found at", x)

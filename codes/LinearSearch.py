# DECLARE myData : ARRAY [0:9] OF INTEGER 
myData = [3, 8, 2, 9, 50, 28, 16, 25, 78, 18]

index = 0
found = False

searchValue = int(input("Enter a number to search "))

while found == False and index < 10:
    
    if searchValue == myData[index]:
        found = True
    else:
        index += 1

if found == True:
    print("Number Found at", index) 
else:
    print("Number not found...")
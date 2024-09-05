myList = [[0,0]]*5

for index in range(3):
    marks1 = int(input("Enter Test-1 marks: "))
    marks2 = int(input("Enter Test-2 marks: "))
    
    myList[index][0] = marks1
    myList[index][1] = marks2
    
print(myList)    
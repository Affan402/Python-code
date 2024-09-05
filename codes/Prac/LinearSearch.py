#Declare mylist : ARRAY [0:9] OF INTEGER
myList = [15, 26, 134, 95, 54, 62, 69, 75, 86, 96]

#Function of Linear Search
def LinearSearch(Num):
    
    global myList
    index = 0 
    #Flag
    found = False
    
    while found == False and index < 8:
        
        if Num == myList[index]:
            found = True
        else:
            index +=1 
    if found == True:
        return index
    else:
        return -1

#Calling function     
x= LinearSearch(34)

if x == -1 :
    #Display on terminal
    print("Number not found ")
else:
    #Display on terminal
    print("Number found at", x)
    

# Function of Binary Search 
def BinarySearch(Num):
    
    global myList  # Accessing the global variable myList
    
    top = 0  # Initializing the top index of the array
    bottom = 9  # Initializing the bottom index of the array
    found = False  # Initializing the found flag as False
    
    while top <= bottom and not found:  # Loop until top is less than or equal to bottom and found is False
        middle = int((top + bottom) / 2)  # Calculate the middle index of the array
        
        if Num == myList[middle]:  # If the number is found at the middle index
            found = True  # Set found flag to True
        elif Num > myList[middle]:  # If the number is greater than the middle element
            top = middle + 1  # Update the top index to search in the right half of the array
        else:  # If the number is smaller than the middle element
            bottom = middle - 1  # Update the bottom index to search in the left half of the array
            
    if found == True:  # If the number is found
        return middle  # Return the index where the number is found
    else:  # If the number is not found
        return -1  # Return -1 to indicate that the number is not found

# Calling Function
x = BinarySearch(75)  # Calling the BinarySearch function with the number 75                   
if x == -1:  # If the returned index is -1
    print("Number not found")  # Print that the number is not found
else:  # If the returned index is not -1
    print("Number found at", x)  # Print the index where the number is found


def BubbleSort():
    
    global myList
    
    n = 9
    
    for x in range(n):
        for y in range(n-x):
            if myList[y] > myList[y+1]:
                temp = myList[y]
                myList[y] = myList[y+1]
                myList[y+1] = temp
                
        

def InstructionSort():
    global myList
    Numberofitems = len(myList)
    for index in range(1,Numberofitems):
        Itemstobeinserted = myList[index]
        Currentitem = index -1
        while myList[Currentitem] > Itemstobeinserted and Currentitem > -1:
            myList[Currentitem + 1] = myList[Currentitem]
            Currentitem -= 1
            
        myList[Currentitem + 1] = Itemstobeinserted  
        
InstructionSort()
print(myList)                             
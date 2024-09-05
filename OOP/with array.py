class Students:
    #StudentID : STRING
    #Name : STRING
    #Age :  INTEGER
    #Gender : CHAR
    
    def __init__(self):
        self.__StudentID = ""
        self.__Name = ""
        self.__Age = 0
        self.__Gender = ""
        
    def SetID(self, i):
        self.__StudentID = i
        
    def SetName(self, n):
        self.__Name = n
        
    def SetAge(self, a):
        self.__Age = a
        
    def SetGender(self, g):
        self.__Gender = g
        
    def GetID(self):
        return self.__StudentID
    
    def GetName(self):
        return self.__Name
    
    def GetAge(self):
        return self.__Age
    
    def GetGender(self):
        return self.__Gender
    
    def GetDetails(self):
        print("Student ID: ",self.__StudentID)
        print("Student Name: ",self.__Name)  
        print("Student Age: ",self.__Age)
        print("Student Gender: ",self.__Gender)              
                                               

class subjects(Students):
    #PRIVATE Subject1 :INTEGER
    #PRIVATE Subject2 : INTEGER
    #PRIVATE Subject3 : INTEGER
    
    def __init__(self):
        super().__init__()
        
        self.__Subject1 = 0
        self.__Subject2 = 0
        self.__Subject3 = 0

    def SetSubjects(self, s1, s2, s3):
        self.__Subject1 = s1    
        self.__Subject2 = s2
        self.__Subject3 = s3
        
    def GetDetails(self):
        super().GetDetails()
        
        print("1st Subject:  ", self.__Subject1)
        print("2nd Subject:  ", self.__Subject2)
        print("3rd Subject:  ", self.__Subject3)

myList = [""] * 3
for index in range (3):
    myList[index] = subjects
 
    myList[index].SetID(input("Enter Student ID: "))
    myList[index].SetName(input("Enter Student Name: "))
    myList[index].SetAge(int(input("Enter Age: ")))
    myList[index].SetGender(input("Enter Gender: "))
    myList[index].SetSubjects(int(input("Enter 1st Subject: ")), int(input("Enter 2nd Subject: ")), int(input("Enter 3rd Subject: ")))        

    
for index in range(3):
    myList.GetDetails()
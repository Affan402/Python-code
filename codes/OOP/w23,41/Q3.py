class Character():
    #PRIVATE  Name : STRING
    #PRIVATE XPosition : INTEGER
    #PRIVATE YPosition : INTEGER
    
    def __init__(self, N, xpos, ypos):
        self.__Name = N
        self.__XPosition = xpos
        self.__YPosition = ypos
        
    def GetXPosition(self):
        return self.__XPosition
    
    def GetYPosition(self):
        return self.__YPosition
    
    def SetXPosition(self, NewX):
        self.__XPosition = self.__XPosition + NewX
        if self.__XPosition <0:
            self.__XPosition = 0
        elif self.__XPosition > 10000:
            self.__XPosition = 10000
            
    def SetYPosition(self, NewY):
        self.__YPosition = self.__YPosition + NewY
        if self.__YPosition <0:
            self.__YPosition = 0
        elif self.__YPosition > 10000:
            self.__YPosition = 10000
            
    def Move(self, move):
        if move == "up":
            self.SetYPosition(10)
        elif move == "down":
            self.SetYPosition(-10)
        elif move == "left":
            self.SetXPosition(-10)
        elif move == "right" :
            self.SetXPosition(10)


jack = Character("Jake", 50, 50) 


class BikeCharacter(Character):
    
    def __init__(self, N, xpos, ypos):
        super().__init__(N, xpos, ypos)
        
    def Move(self, move):
        
        if move == "up":
            super().SetYPosition(20)
        elif move == "down":
            super().SetYPosition(-20)    
        elif move == "left" :
            super().SetXPosition(-20)
        elif move == "right":
             super().SetYPosition(20)  
             
Karla = BikeCharacter("Karla", 100, 50)     

name = input("Enter a character: ").lower()
direction = input("Enter a move: ").lower()

if name == "jack":
    jack.Move(direction)
    print("Jack new position is X =", jack.GetXPosition(), "Y= ", jack.GetYPosition())
elif name == "karla":
    Karla.Move(direction)
    print("Karla new position is X =", Karla.GetXPosition(), "Y= ", Karla.GetYPosition())    
class Player:
    #PRIVATE Score : INTEGER
    #PRIVATE Category : STRING
    #PRIVATE PlayerID : STRING
    
    def __init__(self, InputPlayerID):
        self.__Score = 0
        self.__Category = "Not Qualified"
        self.__Player = InputPlayerID

    def GetScore(self):
        return self.__Score
    def GetCategory(self):
        return self.__Category
    def GetPlayer(self):
        return self.__Player

    def SetPlayerID(self):
        PlayerID = input("Enter the new PlayerID")
        
        while len(PlayerID) <=4 or len(PlayerID) >=15:
            PlayerID = input("Enter the new PlayerID")
            
        self.__PlayerID = PlayerID
        
    def SetScore(self, Score):
        if Score >= 0 and Score <= 150:
            self.__Score = Score
            return True
        else:
            print("Invalid Score")
            return False
        
    def SetCategory(self):
        if self.__Score > 120:
            self.__Category = "Advanced"
        elif self.__Score > 80 and self.__Score <= 120:
            self.Category = "Intermediate"
        elif self.__Score >= 50 and self.__Score<= 80 :
            self._Category = "Beginner"
        elif self.__Score < 50:
            self.Category = "Not Qualified"


def CreatePlayer():
    PlayerID = input("Enter a PlayerID: ")
    Score = int(input("Enter a player score: "))
    
    JoannePlayer = Player(PlayerID)
    JoannePlayer.SetScore(Score)
    JoannePlayer.SetCategory()                   
    print(JoannePlayer.GetCategory())
    
CreatePlayer()     
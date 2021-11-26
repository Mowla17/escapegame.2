class Player:
    def __init__(self):
        self.inventory = []
        self.health = 100
        self.location = "Start"              # initializers 
    def  move_player(self,location):
        self.location  = location                                            
       
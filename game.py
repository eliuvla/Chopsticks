from player import * 

class Game:
    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.turn = 1 

    def Print(self):
        print("turn of the player "+ str(self.turn))
        print("hands of the player 1:\n"+str(self.player_1.hand_1)+" "+str(self.player_1.hand_2)+"\n")
        print("hands of the player 2:\n"+str(self.player_2.hand_1)+" "+str(self.player_2.hand_2)+"\n")

    def Actions(self):
        pass

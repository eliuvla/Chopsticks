from player import * 

class Game:
    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.turn = 1 

    def Print(self):
        print("Es turno del jugador "+ str(self.turn))
        print("Mano del jugador 1:\n"+str(self.player_1.hand_1)+" "+str(self.player_1.hand_2)+"\n")
        print("Mano del jugador 2:\n"+str(self.player_2.hand_1)+" "+str(self.player_2.hand_2)+"\n")

# main script to chopsticks

from game import * 
from player import *

player_1 = Player(1,1)
player_2 = Player(1,1)


game = Game(player_1,player_2)

game.print()

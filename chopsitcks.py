# main script to chopsticks

from game import * 
from player import *

player_1 = Player(1,1)
player_2 = Player(1,1)

game = Game(player_1,player_2)

while True:
    game.print
    game.turn
    if game.turn == 1:
        game.action(player_1,player_2)
        if game.winner != None:
            break
    if game.turn == 2:
        game.action(player_2,player_1)
        if game.winner != None:
            break


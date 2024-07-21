# main script to chopsticks

from game import * 
from player import *

player_1 = Player(1,1)
player_2 = Player(1,1)

game = Game(player_1,player_2)

while True:
    game.print()
    game.turn_switch()
    if game.turn == 1:
        game.action(player_1,player_2)
        game.check_win()
        if game.winner is not None:
            game.print()
            break
    if game.turn == 2:
        game.action(player_2,player_1)
        game.check_win()
        if game.winner != None:
            game.print(1)
            break


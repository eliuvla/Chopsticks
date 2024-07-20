import numpy as np
from player import *

class Game:

  def __init__(self, player_1, player_2):
    self.player_1 = player_1
    self.player_2 = player_2
    self.turn = np.random.randint(1,3)
    self.winner = None

  def check_win(self):
    if self.player_1.hand_1 + self.player_1.hand_2 == 0:
      self.winner = 1
      print('Player 1 wins!')
    elif self.player_2.hand_1 + self.player_2.hand_2 == 0:
      self.winner = 2
      print('Player 2 wins!')

  def print(self):
      print("turn of player "+str(self.turn))
      print("hands of player 1: "+str(self.player_1.hand_1)+" "+str(self.player_1.hand_2))
      print("hands of player 2: "+str(self.player_2.hand_1)+" "+str(self.player_2.hand_2))


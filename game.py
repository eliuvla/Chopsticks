import numpy as np
from player import *

class Position:

  def __init__(self, player_1, player_2):
    self.player_1 = player_1
    self.player_2 = player_2
    self.turn = np.random.randint(0,2)
    self.winner = None

  def check_win(self):
    if self.player_1.hand_1 + self.player_1.hand_2 == 0:
      self.winner = 0
      print('Player 2 wins!')
    elif self.player_2.hand_1 + self.player_2.hand_2 == 0:
      self.winner = 1
      print('Player 1 wins!')

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

  def turn(self,other):
      self.turn = (self.turn + 1)%2 + 1
      print(f'Player {self.turn} turn')

  def action(self,player_1,player_2):   
      if player_1.hand_1 != 0 and player_1.hand_2 != 0:
        print('You can only attack')
        while True:
          print('Choose one of your hands (1 or 2)')
          hand = input()
          if hand == 1 or hand == 2:
            break
        while True:
          print("Choose one of your opponent's hand (1 or 2)")         
          hand_o = input
          if hand_o == 1 or hand_o == 2:
            break
        player_1.attack(hand, player_2, hand_o)
      elif (player_1.hand_1 == 0 or player_1.hand_2 == 0) and (player_1.hand_1 + player_2.hand_2)%2 == 0:
        while True:
          print('Choose to 1:attack or 2:spit')
          action = input()
          if action == 1 or action == 2:
            break
        if action == 1:
          while True:
            print('Choose one of your hands (1 or 2)')
            hand = input()
            if hand == 1 or hand == 2:
              break
          while True:
            print("Choose one of your opponent's hand (1 or 2)")         
            hand_o = input
            if hand_o == 1 or hand_o == 2:
              break
          player_1.attack(hand, player_2, hand_o)
        else:
          if player_1.hand_1 == 0:
            player_1.hand_1 = player_1.hand_1/2
            player_1.hand_2 = player_1.hand_1/2
          elif player_1.hand_2 == 0:
            player_1.hand_1 = player_1.hand_2/2
            player_1.hand_2 = player_1.hand_2/2


        
        


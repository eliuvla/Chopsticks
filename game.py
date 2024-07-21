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
      print("Hands of player 1: "+str(self.player_1.hand_1)+" "+str(self.player_1.hand_2))
      print("Hands of player 2: "+str(self.player_2.hand_1)+" "+str(self.player_2.hand_2))
      print("Turn of player "+str(self.turn))

  def turn_switch(self):
        self.turn = 1 if self.turn == 2 else 2

  def action(self,player_1,player_2):   
      if player_1.hand_1 != 0 and player_1.hand_2 != 0:
        print('You can only attack')
        print('Choose one of your hands (1 or 2)')
        hand = player_1.input_hand()
        if player_2.hand_2 == 0:
          hand_o = 1
        elif player_2.hand_1 == 0:
            hand_o = 2      
        else:
          print("Choose one of your opponent's hand (1 or 2)")         
          hand_o = player_2.input_hand()
        player_1.attack(hand, player_2, hand_o)
      elif (player_1.hand_1 == 0 or player_1.hand_2 == 0) and (player_1.hand_1 + player_2.hand_2)%2 == 0:
        while True:
          print('Choose to 1:attack or 2:spit')
          action = int(input())
          if action == 1 or action == 2:
            break
        if action == 1:
          if self.hand_1 == 0:
            hand = 1
          else:
            hand = 2
          if player_2.hand_1 == 0 or player_2.hand_2 == 0:
            if player_2.hand_1 == 0:
              hand_o = 2
            else:
              hand_o = 1
          else:
            print("Choose one of your opponent's hand (1 or 2)")         
            hand_o = player_2.input_hand()
            player_1.attack(hand, player_2, hand_o)
        else:
          player_1.split()
      else: 
        print('You can only attack')
        if player_1.hand_1 == 0:
          hand = 2
        else:
          hand = 1
        if player_2.hand_1 == 0 or player_2.hand_2 == 0:
          if player_2.hand_1 == 0:
            hand_o = 2
          else:
            hand_o = 1
        else:
          print("Choose one of your opponent's hand (1 or 2)")         
          hand_o = player_2.input_hand()
          player_1.attack(hand, player_2, hand_o)
        



        
        


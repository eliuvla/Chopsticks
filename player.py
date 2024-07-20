class Player:

  def __init__(self, hand_1, hand_2):
    self.hand_1 = hand_1
    self.hand_2 = hand_2

  def attack(self,hand_1, other,hand_2):
    other.hand_2 = (other.hand_2 + self.hand_1) % 5
    
  def split(self, hand_1, hand_2):
    if (hand_1 == 0 or hand_2 == 0) and (hand_1 + hand_2) % 2 == 0:
      self.hand_1 = (self.hand_1+self.hand_2)/2
      self.hand_2 = (self.hand_1+self.hand_2)/2
    else:
      print("No se puede hacer split")
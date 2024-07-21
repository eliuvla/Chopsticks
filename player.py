class Player:

  def __init__(self, hand_1, hand_2):
    self.hand_1 = hand_1
    self.hand_2 = hand_2

  def attack(self,hand, other,hand_o):
    if hand == 1 and hand_o == 1:
      other.hand_1 = (other.hand_1 + self.hand_1) % 5
    if hand == 1 and hand_o == 2:
      other.hand_2 = (other.hand_2 + self.hand_1) % 5
    if hand == 2 and hand_o == 1:
      other.hand_1 = (other.hand_1 + self.hand_2) % 5
    if hand == 2 and hand_o == 2:
      other.hand_2 = (other.hand_2 + self.hand_2) % 5


  def split(self):
    if (self.hand_1 == 0 or self.hand_2 == 0) and (self.hand_1 + self.hand_2) % 2 == 0:
      self.hand_1 = (self.hand_1+self.hand_2)/2
      self.hand_2 = (self.hand_1+self.hand_2)/2
    else:
      print("No se puede hacer split")
from suit import Suit
from rank import Rank

class Card:
  def __init__(self, suit_number, rank_number):
    self.suit = Suit(suit_number)
    self.rank = Rank(rank_number)
  
  def __str__(self):
    return str(self.suit) + "-" + str(self.rank)

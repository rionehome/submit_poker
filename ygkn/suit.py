suitsDict = {
  0: '♠',
  1: '♥',
  2: '♦',
  3: '♣'
}

class Suit:
  def __init__(self, number):
    if not (0 <= number <=4):
      raise Exception("number is out of range")
    self.number = number

  def __str__(self):
    return suitsDict.get(self.number)
    
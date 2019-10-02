rankDict = {
  '1': 'A',
  '11': 'J',
  '12': 'Q',
  '13': 'K'
}

class Rank:
  def __init__(self, number):
    if not (1 <= number <= 13):
      raise Exception("number is out of range")
    self.number = number

  def __str__(self):
    return rankDict.get(str(self.number), str(self.number))

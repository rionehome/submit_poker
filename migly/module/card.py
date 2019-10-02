class Card:
	def __init__(self, mark, number):
		self.mark = mark
		self.number = number

	def get_tuple(self):
		# type:()->tuple
		return self.mark, self.number

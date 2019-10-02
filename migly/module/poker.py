import random

from module import card
from module import player


class Poker:
	def __init__(self, play_person_number):
		self.field_cards = self.__setup_cards__()
		self.play_person_number = play_person_number
		self.play_persons = []

	@staticmethod
	def __setup_cards__():
		# type:()->list
		"""
		52枚のトランプを生成してシャッフル
		:return:
		"""
		cards = []
		for mark in ["♥", "♠", "♣", "◆"]:
			for number in range(13):
				cards.append(card.Card(mark, number + 1))
		random.shuffle(cards)
		return cards

	def card_distribute(self):
		# type:()->None
		"""
		カード分配
		:return:
		"""
		for i in range(self.play_person_number):
			self.play_persons.append(player.Player(i))
			for count_card in range(5):
				self.play_persons[-1].carrying_cards.append(self.field_cards.pop(0))

	def display(self, player_id):
		# type:(int)->None
		"""
		カードの状態を表示する
		:param player_id:
		:return:
		"""
		card_id = 1
		print("あなたのカードはこちらです。")
		for select_card in self.play_persons[player_id].carrying_cards:
			print(card_id, select_card.get_tuple())
			card_id += 1

	def card_change(self, player_id, replacing_card_ids):
		# type:(int,list)->None
		"""
		カードを入れ替える
		:return:
		"""
		players_card = self.play_persons[player_id].carrying_cards
		for replacing_card_id in replacing_card_ids:
			players_card[replacing_card_id - 1] = self.field_cards.pop(0)

	def role_matching(self, player_id):
		# type:(int)->int
		"""
		役の判断
		:param player_id:
		:return:
		"""
		players_card = self.play_persons[player_id].carrying_cards
		mark_index = {"♥": 0, "♠": 1, "♣": 2, "◆": 3}
		count_mark = [0, 0, 0, 0]
		count_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for select_card in players_card:
			count_mark[mark_index[select_card.mark]] += 1
			count_number[select_card.number - 1] += 1

		flash = False
		straight = 0
		a_straight = False

		if count_mark.count(5) == 1:
			flash = True

		for target in range(9):
			straight_check = 1
			for i in range(5):
				straight_check *= count_number[target + i]
			if straight_check == 1:
				straight = target
		if count_number[0] * count_number[12] * count_number[11] * count_number[10] * count_number[9] == 1:
			a_straight = True

		if a_straight and flash:
			print("ロイヤル・ストレート・フラッシュ")
			return 1000
		if straight != 0 and flash:
			print("ストレート・フラッシュ")
			return 900 + straight
		if count_number.count(4) == 1:
			print("フォー・オブ・ア・カインド")
			return 800 + count_number.index(4)
		if count_number.count(2) == 1 and count_number.count(3) == 1:
			print("フルハウス")
			return 700
		if flash:
			print("フラッシュ")
			return 600
		if straight != 0:
			print("ストレート")
			return 500 + straight
		if count_number.count(3) == 1:
			print("スリー・オブ・ア・カインド")
			return 400 + count_number.index(3)
		if count_number.count(2) == 2:
			print("ツーペア")
			return 300
		if count_number.count(2) == 1:
			print("ワンペア")
			return 200 + count_number.index(2)
		print("ブタ")
		return 100

	def judge(self):
		score = []
		for select_player in self.play_persons:
			score.append(self.role_matching(select_player.id))
		best_score = max(score)
		if not score.count(best_score) == 1:
			print("引き分け！")
		else:
			print("勝者プレーヤー{}！".format(score.index(best_score) + 1))

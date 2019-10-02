from module import poker

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import qos_profile_sensor_data

rclpy.init()
node = Node("poker")
pub = node.create_publisher(String, "/poker/card", qos_profile_sensor_data)


def play_person_count():
	# type:()->int
	"""
	参加人数の決定
	:return:
	"""
	while True:
		__input__ = input("何人でやりますか？(２〜５人)->")
		try:
			if 2 <= int(__input__) <= 5:
				break
		except ValueError:
			print("整数で入力してください。")
			continue
		print("２〜５の整数で入力してください。")
	return int(__input__)


def card_change(target_player_id):
	# type:(int)->None
	game.display(target_player_id)
	print("交換するカードを１つずつ指定してください。")
	print("指定終了する場合は0を入力してください。")
	result = []
	while True:
		__input__ = input(">")
		try:
			if not 0 <= int(__input__) <= 5:
				print("０〜５の整数で入力してください。")
				continue
		except ValueError:
			print("整数で入力してください。")
			continue
		if int(__input__) == 0:
			break
		result.append(int(__input__))
		result = list(set(result))
		if len(result) == 5:
			break
	game.card_change(target_player_id, result)
	game.display(target_player_id)
	display_client(pub, game.play_persons[target_player_id])


def display_client(pub, target_player):
	"""
	ROS2を用いたカード表示
	:return:
	"""
	message = ""
	for select_card in target_player.carrying_cards:
		message += select_card.mark + "-" + str(select_card.number) + ","

	pub.publish(String(data=message[:-1]))


if __name__ == '__main__':
	while True:
		game = poker.Poker(play_person_count())
		game.card_distribute()

		for player_id in range(game.play_person_number):
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print("プレイヤー{}#############################################".format(player_id))
			card_change(player_id)
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

		game.judge()
		continue_input = input("続けますか？(y/n)>")
		if continue_input == "y":
			continue
		break

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from std_msgs.msg import String
import itertools
import collections


def callback(msg):
	# type:(String)->None
	card_data = msg.data.split(",")
	for card in card_data:
		print(card.split("-")[0], card.split("-")[1])
	print("############################################")


if __name__ == '__main__':
	rclpy.init()
	node = Node("listener")
	node.create_subscription(String, "/poker/card", callback)
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()

# 人数の送信データ
class peoplenumber(Node):
    def __init__(self):
        super().__init__('pnumber')
        self.publisher = self.create_publisher(string, 'chatter')
if __name__ == '__main__':
#pythonクライアントライブラリの初期化  
    rclpy.init(args = args)
#publisherの作成
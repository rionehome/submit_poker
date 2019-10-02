from porker import Porker

print("プレイヤーの数を入力")
numberOfPlayers = int(input())
porker = Porker(numberOfPlayers)

for i in range(numberOfPlayers):
  while(True):
    print(
      str(i + 1) + '番目の人．' +
      'あなたのカードです．ドローしますか？\n' + 
      'ドローするなら何番目かの数字を，しないなら入力せずEnterを押して下さい\n' +
      porker.cardsStr(i))
    inputStr = input()
    if(inputStr == ''):
      break
    porker.draw(i, int(inputStr) - 1)



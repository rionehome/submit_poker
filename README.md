# gitコマンドのまとめ  
## 初期設定（一度だけ必要  
git config --global user.email "<GitHubのアカウントで設定したメールアドレス>"  
git config --global user.name "<GitHubのアカウント名>"  

## 自分の作ったプログラムを上げる時  
git clone https://github.com/rionehome/submit_poker.git //githubからデータを落としてくる  
cd submit_porker //落としてきたデータの中に移動  
  
● ここで、ポーカーのプログラムは「/home/migly/poker/migly」という名前のディレクトリの中に入っているとします。  
`cp /home/migly/poker/migly .` //自分のポーカーのプログラムを、submit_pokerの中にコピーする。もちろんマウスでコピーアンドペーストでも可。  
`git add migly/`  
`git commit -m "\[add\]miglyのポーカープログラム追加"`  
`git push origin master`  


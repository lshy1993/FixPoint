File info:
main.py メインプログラム
Q1.py　設問１のコード
Q2.py　設問２のコード
Q3.py　設問３のコード
Q4.py　設問４のコード
test.txt　監視ログ
testGen.py　テスト用例を生成するツール

How to use:
Python main.py -argv
設問１の場合：-argvに 1 を入力
例：
Python main.py 1
設問２３４の場合：N m tを順番で入力（入力せずもOK、main.pyデフォルト値ある）
例：
Python main.py 2 3
Python main.py 3 2 3 200
Python main.py 4 5

テスト用例
testGen.pyのParam部分を変更して、
実行すればtest.txtの中に生成する

簡単説明：
Q1.py ログを時間順に読み取り、Dictionay<IPアドレス,タイムアウトの最初の時間>、タイムアウトから回復したら、今の時間とDictの記録値を出力。

Q2.py Dictionay<IPアドレス,[タイムアウトの最初の時間,タイムアウト回数]>、回復して && 回数>N なら、Dictの記録値を出力。

Q3.py Ping平均値を計算する Dict<ip, <[[ping1,ping2,...],date]> >を追加した。
m個のPingデータの移動平均がt以上なら、時間を記録し。
移動平均がt以下なら、Dictの記録値を出力。タイムアウトの場合、記録をリセットする。

Q4.py ネットワークプレフィックス長から、サブネットを計算し。
サブネットの状態を記録する Dict<subnetIP, Dict<serverIP,[date, タイムアウト回数, 回復したか]> >　を追加した。
任意のサーバーがタイムアウトから回復した時、同じサブネットの全サーバーのステータスを検査し、
条件を満たしたら、出力する。
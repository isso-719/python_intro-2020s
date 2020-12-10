# モジュールの読み込み
import math

# (1). 辞書を用いて価格表の生成

fruits = {"りんご": 100,
          "オレンジ": 200,
          "ぶどう": 300}

print(
    f'【価格表】\n りんご: {fruits["りんご"]}円\n オレンジ: {fruits["オレンジ"]}円\n ぶどう: {fruits["ぶどう"]}円\n')

# (2). Aさん, Bさん, Cさんの購入金額を税別、税込で表示

tax = 1.1

price_A = fruits["りんご"] * 1 + fruits["オレンジ"] * 2 + fruits["ぶどう"] * 3
price_B = fruits["オレンジ"] * 2 + fruits["ぶどう"] * 3
price_C = fruits["りんご"] * 2 + fruits["オレンジ"] * 4

total_A = math.floor(price_A * tax)
total_B = math.floor(price_B * tax)
total_C = math.floor(price_C * tax)

print('【購入金額】')
print(f' Aさん\n 税抜: {price_A}円\n 税込: {total_A}円')
print(f' Bさん\n 税抜: {price_B}円\n 税込: {total_B}円')
print(f' Cさん\n 税抜: {price_C}円\n 税込: {total_C}円\n')

# (3).Pythonの「辞書」を(1), (2)を例に説明

print('''【辞書の説明】
Pythonの「辞書」とは、キーと値を紐付けし、データをしまっておくものである。
問題4の例では"fruits"という名前の辞書に"りんご"と"100"、"オレンジ"と"200"、"ぶどう"と"300"をそれぞれ紐付けして保存されている。
"fruits[<キー>]"を指定することでキーと紐付けされた値を取り出すことができる。
さらにここでは、取り出した値を用いてAさん、Bさん、Cさんそれぞれの購入金額の税抜、税込を計算している。''')

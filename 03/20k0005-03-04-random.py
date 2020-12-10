# モジュールをインポートする
import random

# 名前の入力を促す
name = input("あなたの名前を入力しよう!\n@")

# 本田圭佑と挨拶表示
print(f"本田圭佑です。\nあなたの名前は@{name}っていうのか、ほなよろしくな!\n")

# body文表示
body = "2020年もっとおいしくなったペプシジャパンコーラ。\n飲んでみたくないですか?\n僕にジャンケンで勝ったら、一本あげますよ。\nじゃ〜んけん..."
print(body)

# ジャンケンの入力を促し、入力された値をm_handに代入
inp = "あなたは何を出す?(数字を入力)\n 0: Tweet #本田にグーで勝つ\n 1: Tweet #本田にチョキで勝つ\n 2: Tweet #本田にパーで勝つ\n\n"
m_hand = int(input(inp))

# m_handが有効かどうかを検証
if m_hand >= 0 and m_hand <= 2:

    # ジャンケン結果用テキスト
    lose = "ジャンケンポン\n[YOU LOSE]\n俺の勝ち、1年間何やってたんですか?\nジャンケンに対する意識の差です\nほな、注ぎます\n明日も挑戦!"
    win = "ジャンケンポン\n[YOU WIN]\n俺の負け、今日は負けを認めます\nただ、勝ち逃げは許しませんよ\nほな、注ぎます\n明日もここでまってますよ!"

    # ジャンケンの手のリストを作成
    hands = ["グー", "チョキ", "パー"]

    # 0から2のランダムな数を生成して、変数に代入する
    h_hand = random.randint(0, 2)

    # h_handの値で勝敗を決定する(リストに合わせて0がグー, 1がチョキ, 2がパー)
    if h_hand == 0 and m_hand == 2:
        print(f"私の手: パー\n本田の手: グー\n")
        print(win)

    elif h_hand == 1 and m_hand == 0:
        print(f"私の手: グー\n本田の手: チョキ\n")
        print(win)

    elif h_hand == 2 and m_hand == 1:
        print(f"私の手: チョキ\n本田の手: パー\n")
        print(win)

    elif h_hand == m_hand:
        print(f"私の手: {hands[m_hand]}\n本田の手: {hands[h_hand]}\n")
        print("勝たないともらえないのであいこは負け!")
        print(lose)

    else:
        print(f"私の手: {hands[m_hand]}\n本田の手: {hands[h_hand]}\n")
        print(lose)

else:
    print("入力された数値は無効です\nゲームを中断します")

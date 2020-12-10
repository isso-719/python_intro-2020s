import random

p = 3

while True:
    if p == 0:
        print("あなたはポイントを持っていません。地下行きです。")
        break

    rate = random.randint(1, 10)
    print(f"現在のレート: {rate}")
    print(f"あなたは {p} ポイント持っています。\nゲームを行いますか?")
    contract = input("Yes / No を入力>>")
    if contract == "Yes" or contract == "yes" or contract == "y":

        bet = int(input("賭けるポイントを入力>>"))
        if bet > p:
            print("嘘をついたのでポイントは全て没収、よって地下行きです。")
            break

        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        r = r1 + r2

        ans = input("丁,半を選択して下さい。\n丁: c, 半: h を入力>>")

        if r % 2 == 0 and ans == "c":
            print(f"サイコロ1: {r1}\nサイコロ2: {r2}\n合計: {r}\n丁でした。")
            p = p + bet * rate
            print(
                f"賭けたポイント: {bet} × 現在のレート: {rate} = {bet * rate} を加算し、 {p} ポイントとなりました。")

        elif r % 2 == 1 and ans == "h":
            print(f"サイコロ1: {r1}\nサイコロ2: {r2}\n合計: {r}\n半でした。")
            p = p + bet * rate
            print(
                f"賭けたポイント: {bet} × 現在のレート: {rate} = {bet * rate} を加算し、 {p} ポイントとなりました。")

        elif ans == "c":
            print(f"サイコロ1: {r1}\nサイコロ2: {r2}\n合計: {r}\n半でした。")
            p = p - bet
            print(f"賭けた {bet} ポイントは没収され、 {p} ポイントとなりました。")

        elif ans == "h":
            print(f"サイコロ1: {r1}\nサイコロ2: {r2}\n合計: {r}\n丁でした。")
            p = p - bet
            print(f"賭けたポイント {bet} ポイントは没収され、 {p} ポイントとなりました。")

        else:
            print("このゲームは遊びではありません。よってポイントは全て没収です。")
            p = 0

    elif contract == "No" or contract == "no" or contract == "n":
        print(f"プログラムを終了します。\nあなたのポイントは {p} ポイントでした。")
        break
    else:
        print("適切な値を入力してください。\n")

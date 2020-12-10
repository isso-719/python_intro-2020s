# 問題1の問題と選択肢を定義
question1 = "問題1: いつもの磯貝和希の睡眠時間は?"
selection1 = "a: 5時間未満, b:5時間以上8時間未満, c:8時間以上"

# 問題の表示
print(question1 + "\n" + selection1)

# 入力された値を変数answer1に代入する
answer1 = input()

# 入力された答えよってレスポンスを返す
if answer1 == "a":
    print("入力された選択肢aは正解です!")
elif answer1 == "b" or answer1 == "c":
    print(f"入力された選択肢{answer1}は不正解です!")
else:
    print(f"入力された選択肢{answer1}は正しくありません!")

# 問題2の問題と選択肢を定義
question2 = "問題2: いつもの磯貝和希の晩ご飯の時間は?"
selection2 = "a: 18時, b:19時, c:20時"
print("\n" + question2 + "\n" + selection2)
answer2 = input()

# 入力された答えよってレスポンスを返す
if answer2 == "b":
    print("入力された選択肢bは正解です!")
elif answer2 == "a" or answer2 == "c":
    print(f"入力された選択肢{answer2}は不正解です!")
else:
    print(f"入力された選択肢{answer2}は正しくありません!")

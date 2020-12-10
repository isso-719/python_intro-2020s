print("試験の得点を入力")

score = int(input())

if 0 <= score and score <= 100:
    print("正常")
else:
    print("異常")

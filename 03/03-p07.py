print('''「以上はどれ?」
1. ==
2. <=
3. >= ''')

ans = int(input())

if ans == 2:
    print("正解")
elif ans == 1 or ans == 3:
    print("不正解")
else:
    print("無効")

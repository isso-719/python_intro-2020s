# tmp(temperature)リストに気温を入力させる
tmp = eval(input('気温のリストを入力'))

# 最小値、最大値を求めるプログラム
print(f"最小値は{min(tmp)}、最大値は{max(tmp)}")

# 平均値を求めるプログラム
aver = sum(tmp) / len(tmp)
print(f"平均値は{aver}")

for x in tmp:
    print('*' * int(x) + ' ' + str(x))

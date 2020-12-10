pat0 = "ーー＋＋" * 8
pat1 = "＋＋ーー" * 8

tmp0 = pat0 + "\n" + pat0
tmp1 = pat1 + "\n" + pat1

tmp2 = tmp0 + "\n" + tmp1

flag = (tmp2 + "\n") * 3 + tmp2

print(flag)

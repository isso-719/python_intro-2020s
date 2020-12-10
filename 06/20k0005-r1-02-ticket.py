sta = ['静岡', '名古屋', '京都', '新大阪']
fare = {'静岡': 3350, '名古屋': 6260, '京都': 8210, '新大阪': 8750}
exp = {'静岡': 3300, '名古屋': 4620, '京都': 5390, '新大阪': 5390}

print('東京駅自動券売機システムへようこそ!')

go = int(input('降車駅を選んでください\n (1)静岡、(2)名古屋、(3)京都、(4) 新大阪\n>'))

if go >= 1 and go <= 4:

    kind = int(input('特急券の種別を選んでください\n (1)指定席(2)自由席 (3)今は購入しない\n>'))

    if kind == 1:
        print(f'東京駅から{sta[go - 1]}まで')
        print(f'運賃{fare[sta[go - 1]]}円')
        print(f'特急券(指定席){exp[sta[go - 1]]}円')
        print(f'合計{fare[sta[go - 1]] + exp[sta[go - 1]]}円')

    elif kind == 2:
        print(f'東京駅から{sta[go - 1]}まで')
        print(f'運賃{fare[sta[go - 1]]}円')
        print(f'合計{fare[sta[go - 1]]}円')

    elif kind == 3:
        print('またのご利用をお待ちしております')

    else:
        print('無効な値が入力されました')

else:
    print('無効な値が入力されました')

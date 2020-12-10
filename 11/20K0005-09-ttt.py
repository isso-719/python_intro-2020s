import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = []
cpu = []
turn = ""


def showBoard():
    for x in range(3):
        left = 3 * x
        mid = 3 * x + 1
        right = 3 * x + 2
        print(f"{board[left]} | {board[mid]} | {board[right]}")


def playerSelect():
    stats = False
    while stats == False:

        print(f"プレイヤー(○)のターン")
        select = int(input("どの数字を選択しますか?>>"))

        for x in board:
            if select == x:
                stats = True

    write = select - 1
    board[write] = "○"

    player.append(select)

    showBoard()


def cpuSelect():
    print(f"CPU(×)のターン")
    stats = False
    while stats == False:
        select = random.randint(1, 9)
        for x in board:
            if select == x:
                stats = True

    write = select - 1
    board[write] = "×"

    cpu.append(select)

    showBoard()


showBoard()
while True:
    turn = "プレイヤー"
    playerSelect()

    # プレイヤーが勝ちか判定
    if 1 in player and 2 in player and 3 in player:
        break
    if 4 in player and 5 in player and 6 in player:
        break
    if 7 in player and 8 in player and 9 in player:
        break
    if 1 in player and 4 in player and 7 in player:
        break
    if 2 in player and 5 in player and 8 in player:
        break
    if 3 in player and 6 in player and 9 in player:
        break
    if 1 in player and 5 in player and 9 in player:
        break
    if 3 in player and 5 in player and 7 in player:
        break

    # 引き分け判定
    empty = True
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x in board:
            empty = False
    if empty == True:
        break

    turn = "CPU"
    cpuSelect()

    # CPUが勝ちか判定
    if 1 in cpu and 2 in cpu and 3 in cpu:
        break
    if 4 in cpu and 5 in cpu and 6 in cpu:
        break
    if 7 in cpu and 8 in cpu and 9 in cpu:
        break
    if 1 in cpu and 4 in cpu and 7 in cpu:
        break
    if 2 in cpu and 5 in cpu and 8 in cpu:
        break
    if 3 in cpu and 6 in cpu and 9 in cpu:
        break
    if 1 in cpu and 5 in cpu and 9 in cpu:
        break
    if 3 in cpu and 5 in cpu and 7 in cpu:
        break

    # 引き分け判定
    empty = True
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x in board:
            empty = False
    if empty == True:
        break


if empty == True:
    print("ゲーム終了。引き分けです。")
else:
    print(f"ゲーム終了。勝者は{turn}です!")

import random

from dataclasses import *
@dataclass
class Card:
    suit: str
    rank: int


def new_stock():
    stock = []
    for suit in ["spade", "heart", "diamond", "club"]:
        for rank in range(1, 14):
            card = Card(suit, rank)
            stock.append(card)
            random.shuffle(stock)
    return stock


def new_hand(stock, sheets):
    cards = []
    for x in range(sheets):
        card = stock.pop()
        cards.append(card)
    return cards


def change(stock, hand, index):
    for x in index:
        card = stock.pop()
        hand.append(card)
        hand[x] = hand.pop()


stock = new_stock()
print(f"残り: {len(stock)}")
hand = new_hand(stock, 5)
print(f"手札: {hand}")
print(f"残り: {len(stock)}")

changeIndex = input("チェンジするカード番号(0~4)を配列で入力>>")
changeIndex = eval(changeIndex)

change(stock, hand, changeIndex)
print(f"チェンジ後{hand}")

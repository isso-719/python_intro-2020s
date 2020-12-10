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


def new_hand(stock):
    cards = []
    for x in range(5):
        card = stock.pop()
        cards.append(card)
    return cards


def change_heart(hand):
    for card in hand:
        card.suit = "heart"


stock = new_stock()
hand = new_hand(stock)
print(f"手札: {hand}")
print(f"残り: {len(stock)}")

change_heart(hand)
print(f"その後{hand}")

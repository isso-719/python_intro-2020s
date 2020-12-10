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


print(new_stock())

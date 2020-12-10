from dataclasses import *
@dataclass
class Product:
    name: str
    price: int
    tax: int


def calc(price, tax):
    total = float(price * (tax + 1))
    return total


products = [Product("りんご", 400, 0.08), Product("冷蔵庫", 40000, 0.1)]

for i in products:
    print(f"商品名: {i.name}")
    print(f"本体価格: {i.price}円")
    print(f"税込: {calc(i.price, i.tax)}円")

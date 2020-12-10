import math

apple = 100
orange = 200
grape = 300

a_price = apple * 1 + orange * 2 + grape * 3
b_price = orange * 2 + grape * 3
c_price = apple * 2 + orange * 4

tax = 1.08

a_total = math.floor(a_price * tax)
b_total = math.floor(b_price * tax)
c_total = math.floor(c_price * tax)

print(f'''Aさん
　税別: {a_price}円
　税込: {a_total}円''')

print(f'''Bさん
　税別: {b_price}円
　税込: {b_total}円''')

print(f'''Cさん
　税別: {c_price}円
　税込: {c_total}円''')

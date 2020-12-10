price = 198
qty = 12
tax = 0.1

total = price * qty

print(f"　小計: {total:.0f}円")
print(f"消費税: {total * tax:.0f}円")
print(f"　合計: {total * (1 + tax):.0f}円")

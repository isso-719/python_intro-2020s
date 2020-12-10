price = 198
qty = 12
tax = 0.08

total = price * qty

print(f"　小計: {total}円")
print(f"消費税: {total * tax}円")
print(f"　合計: {total * (1 + tax)}円")

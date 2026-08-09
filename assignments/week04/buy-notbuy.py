prices = []

# รับราคาสินค้า 6 รายการ
print("Enter prices of 6 items:")

for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)

# รับงบประมาณรวม
budget = int(input("\nEnter total budget: "))

print()

current_total = 0
bought_items = []

# ตรวจสอบสินค้าตามลำดับ
for i in range(6):
    if current_total + prices[i] <= budget:
        print(f"Item {i + 1} = {prices[i]} -> buy")

        current_total += prices[i]
        bought_items.append(prices[i])

        print(f"Current total = {current_total}")
    else:
        print(f"Item {i + 1} = {prices[i]} -> cannot buy")

        print(f"Current total = {current_total}")

    print()

# แสดงผลสรุป
print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {budget - current_total}")
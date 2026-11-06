def calculate_change(paid, price):
    change = paid - price
    return change
snack_price = 25
print("--SNACK VENDING MACHINE--")
print(f"The price of the snack is {snack_price}")
print("coins accepted: 1, 5, 10, 25\n")

total_money_inserted = 0
coins_inserted = 0

while True:
    coins = int(input("enter the coin(1,5,10 or 25):"))
    if coins != 1 and coins!= 5 and coins!=10 and coins != 25:
        print("invalid coin selected")
        continue

    total_money_inserted = total_money_inserted + coins
    coins_inserted = coins_inserted + 1
    print(f"inserted {total_money_inserted}")

    if total_money_inserted >= snack_price:
        break

change = calculate_change(total_money_inserted, snack_price)

if change == 0:
    pass
else:
    print(f"the change is {change}")

print(f"---SUMMARY---")
print(f"snack price: {snack_price}")
print(f"total money inserted: {total_money_inserted}")
print(f"total coins inserted: {coins_inserted}")
print(f"change amount: {change}")



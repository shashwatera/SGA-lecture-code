stock = {}
bills = []

print("Let's set up the shop's stock first.")
n = int(input("How many different items does the shop have? "))
for i in range(n):
    item = input("Enter item name: ")
    qty = int(input("Enter starting quantity for " + item + ": "))
    stock[item] = qty

print("\nStock is ready:", stock)

while True:
    print("\n1. Buy an item")
    print("2. Show total bill and exit")
    choice = input("Enter choice: ")

    if choice == '1':
        item = input("Enter item name to buy: ")

        if item not in stock:
            print("This item is not in stock list.")
        else:
            qty_wanted = int(input("Enter quantity you want: "))

            if qty_wanted > stock[item]:
                print("Not enough stock. Only", stock[item], "available.")
            else:
                price = float(input("Enter price per unit: "))
                bills.append((item, qty_wanted, price))
                stock[item] = stock[item] - qty_wanted
                print("Added to bill:", item, "x", qty_wanted, "at", price, "each")

    elif choice == '2':
        break

    else:
        print("Invalid choice.")

print("\nFINAL BILL")
grand_total = 0

for entry in bills:
    item_name = entry[0]
    quantity = entry[1]
    price = entry[2]
    line_total = quantity * price
    grand_total = grand_total + line_total
    print(item_name, "x", quantity, "@", price, "=", line_total)

print("Grand Total:", grand_total)
print("\nRemaining stock:", stock)
order = ["Burger", "Juice", "Coffee"]

order[1] = input("We don't have juice at the moment what would you like in place of that?\n")
order.append(input("What else would you like?\n"))
order.sort()
print("Complete Order:", order)
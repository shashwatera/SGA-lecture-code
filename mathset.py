food = {"Food", "Beverage", "Dessert"}
print(food)
print("Number of unique food:", len(food))
if "Food" in food:
    print("Food is present in the set")
food.add("Starter")
food.remove("Beverage")
food.add("Food")
print(food)

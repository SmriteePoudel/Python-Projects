coffee': 150,
    'momo': 90,
}

print("Welcome to my hotel")
print("Have a look at the menu")
for item, price in menu.items():
    print(f"{item.capitalize()}: {price}")

order_total = 0.0

item_1 = input("Enter the name of item you want to order: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1.capitalize()} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2.capitalize()} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount of items to pay is: {order_total:.2f}")

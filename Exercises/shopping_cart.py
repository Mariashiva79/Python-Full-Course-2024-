# Create a shopping cart program

item = input("What item would you like to buy?: ")
prize = float(input("How much is the item?: "))
quantity = int(input("How many would you like?: "))
total = prize * quantity

print(f"You bought {quantity} {item} for ${total}")
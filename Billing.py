print("Welcome to the Billing System with 13% VAT")
print("-" * 50)

while True:
    try:
        item_count = int(input("How many different items? (example: 2): "))
        if item_count > 0:
            break
        print("Please enter a number greater than 0.")
    except ValueError:
        print("Enter a number like 1 or 2, not an item name.")

items = []
subtotal = 0

for i in range(item_count):
    print("\nItem", i + 1)

    name = input("Enter item name: ")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Enter a whole number like 2 or 3.")

    while True:
        try:
            price = float(input("Enter price per piece in Rs: "))
            if price >= 0:
                break
            print("Price cannot be negative.")
        except ValueError:
            print("Enter only the price, like 25 or 25.50.")

    amount = quantity * price
    subtotal = subtotal + amount
    items.append([name, quantity, price, amount])

vat = subtotal * 0.13
total = subtotal + vat

print("\n--- Final Bill ---")

for i in range(len(items)):
    name, quantity, price, amount = items[i]
    print(f"{i + 1}. {name}: {quantity} pcs x Rs.{price:.2f} = Rs.{amount:.2f}")

print("-" * 50)
print(f"Subtotal: Rs.{subtotal:.2f}")
print(f"13% VAT: Rs.{vat:.2f}")
print(f"Total Amount to Pay: Rs.{total:.2f}")
print("Thank you for shopping!")

print("Welcome to the Billing System with 13% VAT")
print("-" * 50)

item_count = int(input("Enter the number of different item types: "))

items = []
total_without_vat = 0

for i in range(item_count):
    print("\nItem", i + 1)

    item_name = input("Enter item name (e.g., Biscuit, Oats): ")
    quantity = int(input("Enter quantity of " + item_name + ": "))
    price_per_unit = float(input("Enter price per 1 piece of " + item_name + ": "))

    amount = quantity * price_per_unit
    total_without_vat = total_without_vat + amount

    items.append([item_name, quantity, price_per_unit, amount])

vat = total_without_vat * 0.13
total_with_vat = total_without_vat + vat

print("\n--- Final Bill ---")

for i in range(len(items)):
    name = items[i][0]
    quantity = items[i][1]
    price = items[i][2]
    amount = items[i][3]

    print(str(i + 1) + ". " + name + ": " + str(quantity) + " pcs x Rs." + str(price) + " = Rs." + str(amount))

print("-" * 50)
print("Subtotal (without VAT): Rs." + str(total_without_vat))
print("13% VAT: Rs." + str(vat))
print("Total Amount to Pay: Rs." + str(total_with_vat))
print("Thank you for shopping!")

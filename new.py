item_price_text = "250.50"
quantity_text = "3"

item_price = float(item_price_text)
quantity = int(quantity_text)

subtotal = item_price * quantity
tax = subtotal * 0.05
total = subtotal + tax

print("Subtotal:", round(subtotal, 2))
print("Tax:", round(tax, 2))
print("Total bill:", round(total, 2))

final_message = "Your total bill is Rs. " + str(round(total, 2))
print(final_message)
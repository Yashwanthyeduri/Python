def calculate_subtotal(price, quantity):
    """
    it calculates the subtotal by multiplying price and quantity
    """
    return price * quantity

def calculate_discount(subtotal, discount_percent):
    """
    it calculates discounts by solving subtotal multiplies parantesis       of discount_percentages by 100
    """
    return subtotal * (discount_percent / 100)

def calculate_final_total(subtotal, discount):
    return subtotal - discount

price = 250
quantity = 4
discount_percent = 10

subtotal = calculate_subtotal(price, quantity)
discount = calculate_discount(subtotal, discount_percent)
final_total = calculate_final_total(subtotal, discount)

print(f"Subtotal: Rs. {subtotal}")
print(f"Discount: Rs. {discount}")
print(f"Final total: Rs. {final_total}")


help(calculate_subtotal)
help(calculate_discount)
a=10.394847382888
result = 9.1 + 2.9
print(result)  # Prints 11.9

rounded_result = round(result, 2)
print(rounded_result)  # Prints 11.9
item_count = 5
price_per_item = 99.99
print(type(item_count))
print(type(price_per_item))
print(type(a))


item_prices = [19.99, 5.49, 12.25]

total = 0
for price in item_prices:
    total = total + price

print("Raw total:", total)
print("Rounded total:", round(total, 2))

item_count = len(item_prices)
average_price = total / item_count
print("Average item price:", round(average_price, 2))
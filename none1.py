product_prices = {
    "laptop": 55000,
    "mouse": 500,
    "keyboard": 1200,
}

def find_price(product_name):
    if product_name in product_prices:
        return product_prices[product_name]
    else:
        return None

price_of_laptop = find_price("laptop")
price_of_monitor = find_price("monitor")

if price_of_laptop is None:
    print("Laptop price not found")
else:
    print("Laptop price:", price_of_laptop)

if price_of_monitor is None:
    print("Monitor price not found")
else:
    print("Monitor price:", price_of_monitor)
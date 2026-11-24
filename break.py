customers = [
    {"name": "Aarav", "email": "aarav@example.com"},
    {"name": "Priya", "email": "priya@example.com"},
    {"name": "Rohan", "email": "rohan@example.com"},
]

target_email = "priya@example.com"
found_customer = None

for customer in customers:
    print("Checking:", customer["name"])
    if customer["email"] == target_email:
        found_customer = customer
        break

if found_customer:
    print("Found:", found_customer["name"])
else:
    print("No matching customer found")
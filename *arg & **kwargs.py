def describe_product(name, *tags, **specs):
    print(f"Product: {name}")
    if tags:
        print(f"Tags: {', '.join(tags)}")
    if specs:
        print("Specifications:")
        for key, value in specs.items():
            print(f"  {key}: {value}")
    print("-" * 30)

describe_product("Laptop", "electronics", "premium", ram="16GB", storage="512GB SSD")
describe_product("Notebook", "stationery", pages=200)
describe_product("Water Bottle")
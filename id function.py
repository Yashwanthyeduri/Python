# Immutable example: a string
text = "hello"
print("Original id:", id(text))
text = text + " world"
print("New id after change:", id(text))
print("Notice the id changed, a brand new string was created")

print()

# Mutable example: a list
numbers = [1, 2, 3]
print("Original id:", id(numbers))
numbers.append(5)
print(numbers)
print("Id after change:", id(numbers))
print("Notice the id stayed the same, the same list was changed in place")
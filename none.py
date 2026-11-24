result = None

# ✅ Correct: Checks object identity
if result is None:
    print("No value found")

if result is not None:
    print("Value exists")

# ❌ Avoid: Checks equality, which can be overloaded
if result == None:
    pass
print("pass")
print(type(None))



first_name = "Yeduri"
middle_name = "Yaswanth"
last_name = "kumar"

if middle_name is None:
    full_name = first_name + " " + last_name
else:
    full_name = first_name + " " + middle_name + " " + last_name

print(full_name)
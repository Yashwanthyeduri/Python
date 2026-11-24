name = "amit"
# name[0] = "J"  # This line would raise a TypeError
fixed_name = "J" + name[0:]
print(fixed_name)  # Jamit

# A quick preview of a mutable list, covered fully in Module 8
fruits = ["apple", "banana"]
fruits[0] = "mango"
print(fruits)  # ['mango', 'banana'], changed in place successfully
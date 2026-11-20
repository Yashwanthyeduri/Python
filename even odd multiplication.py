number= int(input("enter the multhiplication number: "))
print(sep="\n")
for i in range(0,13):
  result= number*i
  print(f"{number} * {i} = {result}")
  print(sep="\n")

print(f"{number} number even multiplications are:")
print(sep="\n")
for i in range(0,25,2):
  result= number*i
  print(f"{number} * {i} = {result}")
  print(sep="\n")
  

print(f"{number} number odd multhiplication are:")
print(sep="\n")
for i in range(1,25,2):
  result= number*i
  print(f"{number} * {i} = {result}")
  print(sep="\n")
  

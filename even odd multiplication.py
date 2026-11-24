number= int(input("enter the multhiplication number: "))
for i in range(0,13):
  result= number*i
  print(f"\n{number} * {i} = {result}")

print(f"\n{number} number even multiplications are:")
for i in range(0,25,2):
  result= number*i
  print(f"\n{number} * {i} = {result}")
  

print(f"\n{number} number odd multhiplication are:")
for i in range(1,25,2):
  result= number*i
  print(f"\n{number} * {i} = {result}")

  

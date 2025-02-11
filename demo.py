#Creating a better calculator than above
num1 = float(input("Please choose a number.."))
num2 = float(input("Please choose another number..."))

#num1, num2 = 25, 30
op = input("Please choose an operation! ")
#operation = ['divide', 'multiply', 'add', 'subtract']

if op == 'divide':
  if num2 == 0:
    print("Error. Division by zero")
  else:
      print(num1 / num2)
elif op == 'add':
    print(num1 + num2)
elif op == 'subtract':
    print(num1 - num2)
elif op == 'multiply':
    print(num1*num2)
  


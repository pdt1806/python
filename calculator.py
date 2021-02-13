while True:
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  opt=int(input("Your option (1/2/3/4): "))

  if opt == 1:
    x=float(input("Enter the first number: "))
    y=float(input("Enter the second number: "))
    result=x+y
    lastresult=x+y
    print("Result is:",result)
  if opt == 2:
    x=float(input("Enter the first number: "))
    y=float(input("Enter the second number: "))
    result=x-y
    lastresult=x-y
    print("Result is:",result)
  if opt == 3:
    x=float(input("Enter the first number: "))
    y=float(input("Enter the second number: "))
    result=x*y
    lastresult=x*y
    print("Result is:",result)
  if opt == 4:
    x=float(input("Enter the first number: "))
    y=float(input("Enter the second number: "))
    if y == 0:
        print("Can't divide by zero.")
    else:
        result=x/y
        lastresult=x/y
        print("Result is:",result)
  if opt > 4:
    print("Enter only 1/2/3/4")
  if opt <= 0:
    print("Enter only 1/2/3/4")
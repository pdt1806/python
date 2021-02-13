import math
print("1.Calculate the circumference of the circle")
print("2.Calculate the area of the circle")
print("3.Calculate the perimeter of the square")
print("4.Calculate the area of the square")
print("5.Calculate the perimeter of the rectangle")
print("6.Calculate the area of the rectangle")
ui=int(input("Your option (1/2/3/4/5/6): "))

if ui == 1:
	x=float(input("Enter the diameter: "))
	result = x * math.pi
	print("Result is: ",result)

elif ui == 2:
	x=float(input("Enter the radius: "))
	result = x ** 2 * math.pi
	print("Result is: ",result)

elif ui==3:
	x=float(input("Enter the length of the side: "))
	result = x * 4
	print("Result is: ",result)

elif ui==4:
	x=float(input("Enter the length of the side: "))
	result = x * x
	print("Result is: ",result)

elif ui==5:
	x=float(input("Enter the length of the base: "))
	y=float(input("Enter the length of the height: "))
	result = (x+y)*2
	print("Result is: ",result)

elif ui==6:
	x=float(input("Enter the length of the base: "))
	y=float(input("Enter the length of the height: "))
	result = x*y
	print("Result is: ",result)

else:
	print("Just enter 1/2/3/4/5/6 only.")
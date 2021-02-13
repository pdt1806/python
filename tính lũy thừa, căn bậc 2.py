import math
while True:
	print("1. Tính bình phương của một số")
	print("2. Tính lập phương của một số")
	print("3. Tính lũy thừa khác của một số")
	print("4. Tìm căn bậc 2 của một số")
	inputofuser = int(input("Nhập lựa chọn (1/2/3/4): "))

	if inputofuser == 1:
		x = int(input("Nhập cơ số: "))
		result = x**2
		print("Kết quả là:",result)
	if inputofuser == 2:
		x = int(input("Nhập cơ số: "))
		result = x**3
		print("Kết quả là:",result)
	if inputofuser == 3:
		x = int(input("Nhập cơ số: "))
		y = int(input("Nhập số mũ: "))
		result = x**y
		print("Kết quả là:",result)
	if inputofuser == 4:
		x = int(input("Nhập số: "))
		result = math.sqrt(x)
		print("Kết quả là:",result)
	
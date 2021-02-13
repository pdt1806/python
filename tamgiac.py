import math
try:
    x = float(input("Chiều dài 1 cạnh của tam giác (1): "))
    y = float(input("Chiều dài 1 cạnh của tam giác (2): "))
    z = float(input("Chiều dài 1 cạnh của tam giác (3): "))

    if x == y == z:
        print("Tam giác này là tam giác đều")

    if x == y or x == z or y == z:
        print("Tam giác này là tam giác cân")

    if (x**2 + y**2 == z**2) or (y**2 + z**2 == x**2) or (z**2 + x**2 == y**2):
        print("Tam giác này là tam giác vuông")

    if ((x**2 + y**2 == z**2) or (y**2 + z**2 == x**2) or (z**2 + x**2 == y**2)) and ((x == y) or (x == z) or (y == z)):
        print("Tam giác này là tam giác vuông cân")
except:
    print("Nhập sai dạng dữ liệu")

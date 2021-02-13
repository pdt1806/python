try:
    cc = float(input("Nhập chiều cao của bạn: "))
    cn = float(input("Nhập cân nặng của bạn: "))

    if cc >= 175 and cn >= 60:
        print("Bạn thích hợp để làm thủ môn")
    if cc < 175 and cn < 60:
        print("Bạn thích hợp để làm cầu thủ")
except:
    print("Nhập số chứ không nhập chữ ok!?")
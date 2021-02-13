import time
import asyncio
loop = asyncio.get_event_loop()
password = input("Nhập mật khẩu: ")

if password == "mynewpassport":
    print("""
CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM - SOCIALIST REPUBLIC OF VIETNAM
-----------------------------------------------------------------------------
HỘ CHIẾU/PASSPORT  Loại/Type  Mã số/Code  Số hộ chiếu/Passport No
                       P          VNM       C7510746
                   
                   Họ và tên/Full name: 
                   NGUYỄN MINH PHÚC
                   
                   Quốc tịch/Nationality      VIỆT NAM/VIETNAMESE
                   
                   Ngày sinh/Date of birth    Nơi sinh/Place of birth
                   18/06/2008                 TP. HỒ CHÍ MINH
                   
                   Giới tính/Sex              Số GCMND/ID card No
                   NAM/M                      
                   
                   Ngày cấp/Date of issue     Có giá trị đến/Date of expiry
                   04/06/2019                 04/06/2024
                   
                   Nơi cấp/Place of issue
                   Cục Quản lý xuất nhập cảnh
-----------------------------------------------------------------------------
P<VNMNGUYEN<<MINH<PHUC<<<<<<<<<<<<<<<<<<<<<<
C7510746<0VNM0806187M2406042<<<<<<<<<<<<<<<4
    """)
    loop.run_forever()

else:
    print("Sai mật khẩu!")
    time.sleep(1)
    exit()
import time

x = 0
x_str = str(x)
x2 = x_str.zfill(2)

y = 0
y_str = str(y)
y2 = y_str.zfill(2)

z = 0
z_str = str(z)
z2 = z_str.zfill(2)

while True:
    print(z2 + ":" + y2 + ":" + x2)
    x = x+1
    x_str = str(x)
    x2 = x_str.zfill(2)
    time.sleep(1)
    if x == 60:
        x = 0
        x_str = str(x)
        x2 = x_str.zfill(2)
        y = y+1
        y_str = str(y)
        y2 = y_str.zfill(2)
        print(z2 + ":" + y2 + ":" + x2)
        x = x+1
        x_str = str(x)
        x2 = x_str.zfill(2)
        time.sleep(1)
        if y == 60:
            x = 0
            x_str = str(x)
            x2 = x_str.zfill(2)
            y = 0
            y_str = str(y)
            y2 = y_str.zfill(2)
            z = z+1
            z_str = str(y)
            z2 = z_str.zfill(2)
            print(z2 + ":" + y2 + ":" + x2)
            x = x+1
            x_str = str(x)
            x2 = x_str.zfill(2)
            time.sleep(1)
            if z == 24:
                break
print("24 hours completed.")

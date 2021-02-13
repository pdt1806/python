print("PI Command Prompt [Version 1.0]")
print("(c) 2020 PhucIron Studios. All rights reserved.")
print(" ")

def Convert(string):
	li = list(string.split(" "))
	return li

while True:
    ui1 = input("Command: ")
    ui2 = Convert(ui1)

    if "info" in ui2 or "information" in ui2:
        print("""
Full name: Nguyen Minh Phuc
D.O.B: 18/06/2008 (DD/MM/YYYY)
Nationality: Vietnam
Phone number: 0765559766
Email: phuciron@gmail.com
2nd email: nmphuc1806@gmail.com
        """)
    else:
        print("'"+ui1+"'"+" is not a command.")
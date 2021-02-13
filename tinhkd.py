print("Enter the number of match(es) you played:")
matches_played = float(input())
print("Enter your current kill(s):")
current_kill = float(input())
print("Enter the next K/D you want after the next match:")
next_kd = float(input())

def tinhkd(matches_played, next_kd, current_kill):
	x = (matches_played + 1) * next_kd - current_kill
	print("You need to kill "+str(x)+" players in the next match to get the K/D of "+str(next_kd))

tinhkd(matches_played, next_kd, current_kill)
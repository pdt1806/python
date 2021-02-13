import random
guessesTaken = 0
number = random.randint(1, 20)

print("Hello! I'm Python. What is your name?")
name = str(input("Your name: "))

print("Hello",name,", I'm thinking of a number between 1 and 20")
print("You got 6 chances to guess.")
for guessesTaken in range(6):
	print("Take a guess.")
	guess = input()
	guess = int(guess)

	if guess < number:
		print("Your guess is lower than the number.")
	if guess > number:
		print("Your guess is bigger than the number.")
	if guess == number:
		break

if guess == number:
	if guessesTaken > 1:
		guessTaken = str(guessesTaken + 1)
		print("Good job. You guessed the right number after ",guessTaken,"guesses.")
	elif guessesTaken == 1:
		guessTaken = str(guessesTaken + 1)
		print("Good job. You guessed the right number after ",guessTaken,"guess.")

if guess != number:
	number = str(number)
	print("The number I was thinking of was",number,".")
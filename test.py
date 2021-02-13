while True:
	import speech_recognition
	import datetime

	name ="PhucIron"
	today = datetime.date.today()
	yesterday = today - datetime.timedelta(days = 1)
	tomorrow = today + datetime.timedelta(days = 1) 

	robot_ear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening...")
		audio = robot_ear.listen(mic)

	try:
		you = robot_ear.recognize_google(audio)

		print("You: " + you)

		if "hello" in you:
			print("Hello "+name+"!")
	
		if "yesterday" in you:
			print("Yesterday : "+ str(yesterday))

		if "today" in you:
			print("Today : "+ str(today))
	
		if "tomorrow" in you:
			print("Tomorrow : "+ str(tomorrow))

		if "your name" in you:
			print("My name is Sirilexatanaby.")

		if "name" == you:
			print("Your name is PhucIron.")

		if "my name" in you:
			print("Your name is PhucIron.")
	
	except:
		print("Robot: I didn't hear anything.")






while True:
	import speech_recognition
	import datetime

	name = "PhucIron"
	phuciron_gender = "male"
	phuciron_birthplace = "Ho Chi Minh City, Vietnam"
	now = datetime.datetime.now()
	today = datetime.date.today()
	yesterday = today - datetime.timedelta(days = 1)
	tomorrow = today + datetime.timedelta(days = 1)
	phuciron_age = now.year - 2008
	robot_age = now.year - 2020

	def Convert(string):
		li = list(string.split(" "))
		return li

	robot_ear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print("BoTyler: I'm listening...")
		audio = robot_ear.listen(mic)

	try:
		you = robot_ear.recognize_google(audio)
		you2 = Convert(you)
		print("You: " + you)

		if "hello" in you2:
			print("BoTyler: Hello "+name+"!")
		if "good morning" in you:
			print("BoTyler: Good morning, "+name+"!")
		if "good afternoon" in you:
			print("BoTyler: Good afternoon, "+name+"!")
		if "good evening" in you:
			print("BoTyler: Good evening, "+name+"!")
		if "good night" in you:
			print("BoTyler: Good night, "+name+"!")
		if "date" == you2:
			print("BoTyler: Today : " + str(today))
		if "yesterday" in you:
			print("BoTyler: Yesterday : "+ str(yesterday))
		if "today" in you2:
			print("BoTyler: Today : "+ str(today))
		if "tomorrow" in you2:
			print("BoTyler: Tomorrow : "+ str(tomorrow))
		if "your name" in you2:
			print("BoTyler: My name is BoTyler.")
		if "name" == you2:
			print("BoTyler: Your name is PhucIron.")
		if "my name" in you2:
			print("BoTyler: Your name is PhucIron.")
		if "old" in you2 and "you" in you2:
			print("BoTyler: I was created in 2020, so I am "+str(robot_age)+" years old")
		if "old" in you2 and "I" in you2:
			print("BoTyler: You were born in 2008, so you are "+str(phuciron_age)+" years old")
		if "gender" == you2:
			print("BoTyler: You are "+str(phuciron_gender))
		if "gender" and "my" in you2:
			print("BoTyler: You are "+str(phuciron_gender))
		if "gender" and "your" in you2:
			print("BoTyler: I belong to all genders.")
		if "who" in you2 and "you" in you2 and "created" in you2 or "create" in you2:
			print("BoTyler: I heard that I was picked up from the garbage, but I don't know if that was true or not :)")
		if "where" in you2 and "you" in you2 and "were" in you2 and "born" in you2:
			print("BoTyler: I heard that I was picked up from the garbage, but I don't know if that was true or not :)")
		if "where" in you2 and "you" in you2 and "come" in you2 and "from" in you2 or "your" in you2:
			print("BoTyler: I heard that I was picked up from the garbage, but I don't know if that was true or not :)")
		if "who" in you2 and "are" in you2 and "your" in you2 and "parents" in you2 in you2:
			print("BoTyler: I heard that I was picked up from the garbage, but I don't know if that was true or not :)")
		if "where" in you2 and "I" in you2 and "come" in you2 and "from" in you2:
			print("BoTyler: You come from "+str(phuciron_birthplace)+".")
		if "where" in you2 and "I" in you2 and "was" in you2 and "born" in you2:
			print("BoTyler: You come from "+str(phuciron_birthplace)+".")
		if "who" in you2 and "me" in you2 and "created" in you2 or "create" in you2:
			print("BoTyler: Your mom and dad, of course.")
		if "am" in you2 and "I" in you2 and "handsome" in you2:
			print('BoTyler: I have just looked up the dictionary, they always use your image in the definition of "good looks" so the answer is definitely yes')
		if "am" in you2 and "I" in you2 and "beautiful" in you2:
			print('BoTyler: I have just looked up the dictionary, they always use your image in the definition of "good looks" so the answer is definitely yes')

	except speech_recognition.UnknownValueError:
		print("BoTyler: I didn't hear or couldn't hear anything")
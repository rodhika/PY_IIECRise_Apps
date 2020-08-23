# Program to command OS to start applications!!
# Author - Rodhika
# Training by IIEC Rise

import os
import pyttsx3

 
pyttsx3.speak("Welcome to the World of Python.")
print()

while True:
	
	print("Provide your choice else type exit/quit to end: ", end='')
	txt=input()
	x=txt.lower()

	# Do not do anything if keyword 'don't' with the input
	if( "don't" in x  or ("do" in x and "not" in x ) or "dont" in x):
		pyttsx3.speak("Let me know what you want me to do.")
	
	# Check for multiple application request 
	elif((("media" in x or "player" in x) and "notepad" in x ) or ("chrome" in x and ("media" in x or "player" in x)) ) or ("chrome" in x and "notepad" in x):
		pyttsx3.speak("You can access one program at a time") 
	
	# Open Media Player
	elif(("run" in x or "open" in x) and ("media" in x or "player" in x)):
		os.system("wmplayer")

	# Open Chrome browser
	elif(("chrome" in x or "browser" in x) and ("run" in x or "open" in x) ):
		os.system("chrome")
	
	# Open Text Editor
	elif(("notepad" in x or "textpad" in x or "editor" in x)and ("run" in x or "open" in x)):
		os.system("notepad")

	# Exit from program
	elif("exit" in x  or "quit" in x):
		pyttsx3.speak('Ending now. Thank you!')
		break
	else:
		print("Not Supported.")

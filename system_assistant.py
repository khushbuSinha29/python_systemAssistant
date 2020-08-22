import pyttsx3
import os
from datetime import date

print("====================================================================================================================================================================")
print("                                                            Your System Assistant                                                                  ")
print("====================================================================================================================================================================")
pyttsx3.speak("Welcome, How can I assist you?")

while(True):
	print("List of functions supported:")
	print("1.chrome")
	print("2.notepad")
	print("3.paint")
	print("4.wps office")
	print("5.Gmail")
	print("6.date\n")
	
	print("What command to execute:  ", end='')
	pyttsx3.speak("What command to execute:")
	
	val=input().lower()
	
	
	
	print()
	if(('dont' in val and 'chrome' in val) or ('do not' in val and 'chrome' in val) or ('do not' in val and 'chrome' in val and 'open' in val) or 
	('don\'t' in val and 'chrome' in val and 'open' in val) or ('don\'t' in val and 'run' in val and 'chrome' in val) or 
	('do not' in val and 'run' in val and 'chrome' in val) or ('not' in val and 'open' in val and 'chrome' in val)):
		pyttsx3.speak("Okay, not opening chrome")
		continue
		
	elif(('dont' in val and 'notepad' in val) or ('do not' in val and 'notepad' in val) or ('do not' in val and 'notepad' in val and 'open' in val) or
	('don\'t' in val and 'notepad' in val and 'open' in val) or 
	('don\'t' in val and 'run' in val and 'notepad' in val) or ('do not' in val and 'run' in val and 'notepad' in val)):
		pyttsx3.speak("Okay, not opening notepad")
		continue
		
	elif(('dont' in val and 'paint' in val) or ('do not' in val and 'paint' in val) or ('do not' in val and 'paint' in val and 'open' in val) or
	('don\'t' in val and 'paint' in val and 'open' in val) or ('don\'t' in val and 'run' in val and 'paint' in val) or 
	('do not' in val and 'run' in val and 'chrome' in val)):
		pyttsx3.speak("Okay, not opening paint")
		continue
		
	elif(('dont' in val and 'wps office' in val) or ('do not' in val and 'wps office' in val) or ('do not' in val and 'wps office' in val and 'open' in val) or
    ('don\'t' in val and 'wps office' in val and 'open' in val) or ('don\'t' in val and 'run' in val and 'wps office' in val) or 
    ('do not' in val and 'run' in val and 'chrome' in val)):
		pyttsx3.speak("Okay, not opening wps office")
		continue
		
	elif(('dont' in val and 'gmail' in val) or ('do not' in val and 'gmail' in val) or ('do not' in val and 'gmail' in val and 'open' in val) or
    ('don\'t' in val and 'gmail' in val and 'open' in val) or ('don\'t' in val and 'run' in val and 'gmail' in val) or 
    ('do not' in val and 'run' in val and 'gmail' in val)):
		pyttsx3.speak("Okay, not opening gmail")
		continue

		
	elif(('chrome' in val)):
		pyttsx3.speak("Opening chrome")
		os.system("chrome")
		
	elif('notepad' in val):
		pyttsx3.speak("opening notepad")
		os.system("notepad")
	elif((('run' in val)and ('date' in val)) or (('open' in val) and('date' in val)) or ('date' in val)):
		dd=date.today()
		print(dd)
		pyttsx3.speak(dd)
	elif('paint' in val):
		pyttsx3.speak('opening paint')
		os.system("mspaint")
	elif('wps office' in val or 'wps' in val):
		pyttsx3.speak("opening wps office")
		os.system('ksolaunch')
	elif('gmail' in val):
		pyttsx3.speak("opening gmail")
		os.system('chrome www.gmail.com')
		
	elif(("exit" in val) or ('close' in val) or ('turn off' in val)):
		pyttsx3.speak("Thank you for using our services , Hope you like it")
		break
	else:
		pyttsx3.speak("This program is not supported")
		print("Program is not supported")	
#Mechanical Switch that waits for a signal to turn on fan
#Currently using raw input

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

RELAIS_1_GPIO = 17 #GPIO 17



while(1):
	x = raw_input()  
		
	if x=='s':
		print("high")
		GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
		GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
		GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) 	  
	  
	elif x=='e':
	 GPIO.cleanup()
	
	
	 
	else:
		print("<<<wrong data >> ")
		print("please enter the defined data to continue....")	

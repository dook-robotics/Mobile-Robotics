#Author: <Zoyla Orellana> Date: <09/09/19>
#
#For testing an input will be requested.
#This way we can find the exact rotation for final.
#
#Rotation Input options:
# up:      2.5 - 2
# center:  7.5-8
# down:    12.5-13
#
# Range: 3-13 (right to left; included decimal values)
#-----------------------------------------------------

import RPi.GPIO as GPIO
import time
#------GPIO Inputs------
servo1 = 12 #--GPIO18
servo2 = 11 #--GPIO17

#------Variables--------
center = 8
right = 3
left = 13

#----Setup--------------

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo1, GPIO.OUT)
GPIO.setup(servo2, GPIO.OUT)

p = GPIO.PWM(servo1, 50)
p2 = GPIO.PWM(servo2, 50)

p.start(0)
p2.start(0)
#--Functions--
def re():
	time.sleep(1)
	p.ChangeDutyCycle(0)
	p2.ChangeDutyCycle(0)
	return re
#-----start----------------

print("Input options are the following:")
print(" - up, down, center")
print(" - values in the range of 3-13(including dec)")
print("__________________________________________________")

try:
	while True:

		print ("Please input desired turn rotation:")
		x = raw_input()

		if(x == 'down'):
			p.ChangeDutyCycle(float(left))
			p2.ChangeDutyCycle(float(left))
			re()
		elif(x == 'center'):
			p.ChangeDutyCycle(float(center))
			p2.ChangeDutyCycle(float(center))
			re()
		elif(x=='up'):
			p.ChangeDutyCycle(float(right))
			p2.ChangeDutyCycle(float(right))
			re()
		else:
			p.ChangeDutyCycle(float(x))
			p2.ChangeDutyCycle(float(x))
			re()


except KeyboardInterrupt:
    p.stop()
    p2.stop()
    GPIO.cleanup()

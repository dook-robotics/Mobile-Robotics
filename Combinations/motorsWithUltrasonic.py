import RPi.GPIO as GPIO                    #Import GPIO library
import time

#Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    # programming the GPIO by BCM pin numbers

TRIG = 18
ECHO = 27

PWM1=17
DIR1=22
PWM2=23
DIR2=24

GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input
              

GPIO.setup(DIR1,GPIO.OUT)
GPIO.setup(PWM1,GPIO.OUT)
GPIO.setup(DIR2,GPIO.OUT)
GPIO.setup(PWM2,GPIO.OUT)

pwm=GPIO.PWM(PWM1,100)
pwm2=GPIO.PWM(PWM2,100)
pwm.start(0)
pwm2.start(0)

time.sleep(5)

def stop():
    print "stop"
    GPIO.output(PWM1,GPIO.LOW)
    GPIO.output(DIR1,GPIO.LOW)
    GPIO.output(PWM2,GPIO.LOW)
    GPIO.output(DIR2,GPIO.LOW)

def forward():
    pwm.ChangeDutyCycle(25)
    pwm2.ChangeDutyCycle(25)
    GPIO.output(PWM1,GPIO.HIGH)
    GPIO.output(DIR1,GPIO.LOW)
    GPIO.output(PWM2,GPIO.HIGH)
    GPIO.output(DIR2,GPIO.LOW)
    print "Forward"

def back():
    pwm.ChangeDutyCycle(25)
    pwm2.ChangeDutyCycle(25)
    GPIO.output(PWM1,GPIO.LOW)
    GPIO.output(DIR1,GPIO.HIGH)
    GPIO.output(PWM2,GPIO.LOW)
    GPIO.output(DIR2,GPIO.HIGH)
    print "back"

def left():
    pwm.ChangeDutyCycle(25)
    GPIO.output(PWM1,GPIO.HIGH)
    GPIO.output(DIR1,GPIO.LOW)
    GPIO.output(PWM2,GPIO.LOW)
    GPIO.output(DIR2,GPIO.LOW)
    print "left"

def right():
    pwm2.ChangeDutyCycle(25)
    GPIO.output(PWM1,GPIO.LOW)
    GPIO.output(DIR1,GPIO.LOW)
    GPIO.output(PWM2,GPIO.HIGH)
    GPIO.output(DIR2,GPIO.LOW)
    print "right"

stop()
count=0
while True:
 i=0
 avgDistance=0
 for i in range(5):
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  time.sleep(0.1)                                   #Delay

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                           #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
            
        pulse_start = time.time()

  while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH

        pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
  distance = round(distance,2)                 #Round to two decimal points
  avgDistance=avgDistance+distance

 avgDistance=avgDistance/5
 print avgDistance
 flag=0
 
       
 if avgDistance < 45:      #Check whether the distance is within 45 cm range
    count=count+1
    stop()
    time.sleep(1)
    back()
    time.sleep(1.5)
    if (count%3 ==1) & (flag==0):
     right()
     flag=1
    else:
     left()
     flag=0
    time.sleep(1.5)
    stop()
    time.sleep(1)
 else:
    forward()
    flag=0

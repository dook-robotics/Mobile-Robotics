#!/usr/bin/python
#-------------------------------------------------------------------------------
#
#
#
#
#
#   
#-------------------------------------------------------------------------------

import RPi.GPIO as GPIO
from time import sleep
import time

# Global constants & variables
# Constants

global counter # starting point for the running directional counter

# GPIO Ports
Enc_A = 13  # Encoder1 input A: input GPIO 13 (active high)
#Enc_B = 6  # Encoder1 input B: input GPIO 6 (active high)
Enc_A2 = 16  # Encoder2 input A: input GPIO 16 (active high)
#Enc_B2 = 12  # Encoder2 input B: input GPIO 12 (active high)
PWM1=17
DIR1=22
PWM2=23
DIR2=24
temp1=1
Revs=0

counter=0


print ("Rotary Encoder Test Program")

GPIO.setwarnings(True)

# Use the Raspberry Pi BCM pins
GPIO.setmode(GPIO.BCM)

#define the Motor pins
GPIO.setup(DIR1,GPIO.OUT)
GPIO.setup(PWM1,GPIO.OUT)
GPIO.setup(DIR2,GPIO.OUT)
GPIO.setup(PWM2,GPIO.OUT)


# define the Encoder switch inputs
GPIO.setup(Enc_A, GPIO.IN) # pull-ups are too weak, they introduce noise
#GPIO.setup(Enc_B, GPIO.IN)
GPIO.setup(Enc_A2, GPIO.IN) # pull-ups are too weak, they introduce noise
#GPIO.setup(Enc_B2, GPIO.IN)
    
    
pwm=GPIO.PWM(PWM1,100)
pwm2=GPIO.PWM(PWM2,100)
pwm.start(0)
pwm2.start(0)


def init():
    '''
    Initializes a number of settings and prepares the environment
    before we start the main program.
    '''
  
    


    # setup an event detection thread for the A encoder switch
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=2) # bouncetime in mSec
    GPIO.add_event_detect(Enc_A2, GPIO.RISING, callback=rotation_decode2, bouncetime=2) # bouncetime in mSec

    print("here")
    return



def rotation_decode(Enc_A):
    '''
    This function decodes the direction of a rotary encoder and in- or
    decrements a counter.

    The code works from the "early detection" principle that when turning the
    encoder clockwise, the A-switch gets activated before the B-switch.
    When the encoder is rotated anti-clockwise, the B-switch gets activated
    before the A-switch. The timing is depending on the mechanical design of
    the switch, and the rotational speed of the knob.

    This function gets activated when the A-switch goes high. The code then
    looks at the level of the B-switch. If the B switch is (still) low, then
    the direction must be clockwise. If the B input is (still) high, the
    direction must be anti-clockwise.

    All other conditions (both high, both low or A=0 and B=1) are filtered out.

    To complete the click-cycle, after the direction has been determined, the
    code waits for the full cycle (from indent to indent) to finish.

    '''

    global counter
    #global Revs
    
    
    


    sleep(0.002) # extra 2 mSec de-bounce time

    # read both of the switches
    Switch_A = GPIO.input(Enc_A)
    #Switch_B = GPIO.input(Enc_B)
    #Switch_A2 = GPIO.input(Enc_A2)
    #Switch_B2 = GPIO.input(Enc_B2)
    print("here")
    
    
    #if (Switch_A == 1) and (Switch_B == 0) : # A then B ->
     #   counter += 1
        
      #  print "direction -> ", counter
   
        # at this point, B may still need to go high, wait for it
       # while Switch_B == 0:
            #Switch_B = GPIO.input(Enc_B)
           
        #print("while1")
        # now wait for B to drop to end the click cycle
        #while Switch_B == 1:
           # Switch_B = GPIO.input(Enc_B)
        #print("while2")
           
        #return

    #elif (Switch_A == 1) and (Switch_B == 1): # B then A <-
    counter -= 1
    print ("direction <- ", counter)
    Revs=(abs(counter)/374)
    print("revolutions: ",Revs)
    if (Revs==1):
       print("revolutions: ",Revs)
       counter=0
       pwm.ChangeDutyCycle(0)
       pwm2.ChangeDutyCycle(0)

        

       # A is already high, wait for A to drop to end the click cycle
       while Switch_A == 1: #and Switch_A2 == 1:
             Switch_A = GPIO.input(Enc_A)
#             Switch_A2 = GPIO.input(Enc_A2)
            
             return

    #else: # discard all other combinations
       print("working")
       return

def rotation_decode2(Enc_A2):
    '''
    This function decodes the direction of a rotary encoder and in- or
    decrements a counter.

    The code works from the "early detection" principle that when turning the
    encoder clockwise, the A-switch gets activated before the B-switch.
    When the encoder is rotated anti-clockwise, the B-switch gets activated
    before the A-switch. The timing is depending on the mechanical design of
    the switch, and the rotational speed of the knob.

    This function gets activated when the A-switch goes high. The code then
    looks at the level of the B-switch. If the B switch is (still) low, then
    the direction must be clockwise. If the B input is (still) high, the
    direction must be anti-clockwise.

    All other conditions (both high, both low or A=0 and B=1) are filtered out.

    To complete the click-cycle, after the direction has been determined, the
    code waits for the full cycle (from indent to indent) to finish.

    '''

    global counter
    #global Revs
    
    
    


    sleep(0.002) # extra 2 mSec de-bounce time

    # read both of the switches
    #Switch_A = GPIO.input(Enc_A)
    #Switch_B = GPIO.input(Enc_B)
    Switch_A2 = GPIO.input(Enc_A2)
    #Switch_B2 = GPIO.input(Enc_B2)
    print("here")
    
    #Commented out for future reference if needed
    #if (Switch_A == 1) and (Switch_B == 0) : # A then B ->
     #   counter += 1
        
      #  print "direction -> ", counter
   
        # at this point, B may still need to go high, wait for it
       # while Switch_B == 0:
            #Switch_B = GPIO.input(Enc_B)
           
        #print("while1")
        # now wait for B to drop to end the click cycle
        #while Switch_B == 1:
           # Switch_B = GPIO.input(Enc_B)
        #print("while2")
           
        #return

    #elif (Switch_A == 1) and (Switch_B == 1): # B then A <-
    counter -= 1
    print ("direction <- ", counter)
    Revs=(abs(counter)/374)
    print("revolutions: ",Revs)
    if (Revs==1):
       print("revolutions: ",Revs)
       counter=0
       pwm.ChangeDutyCycle(0)
       pwm2.ChangeDutyCycle(0)

        

       # A is already high, wait for A to drop to end the click cycle
       while Switch_A2 == 1:  #and Switch_A2 == 1:
             #Switch_A = GPIO.input(Enc_A)
             Switch_A2 = GPIO.input(Enc_A2)
            
             return

    #else: # discard all other combinations
    print("working")
    return

def main():
    '''
    The main routine. 
    Here we will call out init() function which will then begin 
    the rest of our program.We also recieve our input values here 
    that function as our controller.

    '''
    
    
    try:

        init()
        while True:
            x=raw_input()
            
            if x=='s':
               print("stop")
               GPIO.output(PWM1,GPIO.LOW)
               GPIO.output(DIR1,GPIO.LOW)
               GPIO.output(PWM2,GPIO.LOW)
               GPIO.output(DIR2,GPIO.LOW)
               
               x='z'

            elif x=='f':
                print("forward")
                pwm.ChangeDutyCycle(25)
                pwm2.ChangeDutyCycle(25)
                GPIO.output(PWM1,GPIO.HIGH)
                GPIO.output(DIR1,GPIO.LOW)
                GPIO.output(PWM2,GPIO.HIGH)
                GPIO.output(DIR2,GPIO.LOW)
                temp1=1
                x='z'

            elif x=='b':
                print("backward")
                pwm.ChangeDutyCycle(25)
                pwm2.ChangeDutyCycle(25)
                GPIO.output(PWM1,GPIO.LOW)
                GPIO.output(DIR1,GPIO.HIGH)
                GPIO.output(PWM2,GPIO.LOW)
                GPIO.output(DIR2,GPIO.HIGH)
                temp1=0
                x='z'
                
            elif x== 'left':
                print("left")
                pwm.ChangeDutyCycle(25)
                GPIO.output(PWM1,GPIO.HIGH)
                GPIO.output(DIR1,GPIO.LOW)
                GPIO.output(PWM2,GPIO.LOW)
                GPIO.output(DIR2,GPIO.LOW)
                temp1=0
                x='z'
            elif x=='right':
                print("right")
                pwm2.ChangeDutyCycle(25)
                GPIO.output(PWM1,GPIO.LOW)
                GPIO.output(DIR1,GPIO.LOW)
                GPIO.output(PWM2,GPIO.HIGH)
                GPIO.output(DIR2,GPIO.LOW)
                temp1=1
                x='z'   
            elif x== 'cw':
                 pwm.ChangeDutyCycle(25)
                 pwm2.ChangeDutyCycle(25)
                 GPIO.output(PWM1,GPIO.HIGH)
                 GPIO.output(DIR1,GPIO.LOW)
                 GPIO.output(PWM2,GPIO.LOW)
                 GPIO.output(DIR2,GPIO.HIGH)
                 temp1=0
                 x='z'
            elif x== 'ccw':
                 pwm.ChangeDutyCycle(25)
                 pwm2.ChangeDutyCycle(25)
                 GPIO.output(PWM1,GPIO.LOW)
                 GPIO.output(DIR1,GPIO.HIGH)
                 GPIO.output(PWM2,GPIO.HIGH)
                 GPIO.output(DIR2,GPIO.LOW)
                 temp1=0
                 x='z'
            elif x=='l':
               print("low")
               pwm.ChangeDutyCycle(25)
               pwm2.ChangeDutyCycle(25)
               x='z'

            elif x=='m':
                 print("medium")
                 pwm.ChangeDutyCycle(50)
                 pwm2.ChangeDutyCycle(50)
                 x='z'

            elif x=='h':
                 print("high")
                 pwm.ChangeDutyCycle(75)
                 pwm2.ChangeDutyCycle(75)
                 x='z'
                 
            elif x=='e':
                 GPIO.cleanup()
                 break
            
            # wait for an encoder click
            sleep(1)
            
            

    except KeyboardInterrupt: # Ctrl-C to terminate the program
        GPIO.cleanup()


if __name__ == '__main__':
    main()


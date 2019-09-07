# Load library functions we want
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import pygame

# Set which GPIO pins the drive outputs are connected to
DRIVE_1 = 17
DRIVE_2 = 22
DRIVE_3 = 24
DRIVE_4 = 23

# Set all of the drive pins as output pins
GPIO.setup(DRIVE_1, GPIO.OUT)
GPIO.setup(DRIVE_2, GPIO.OUT)
GPIO.setup(DRIVE_3, GPIO.OUT)
GPIO.setup(DRIVE_4, GPIO.OUT)

GPIO.output(DRIVE_1, GPIO.LOW)
GPIO.output(DRIVE_4, GPIO.LOW)

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 3                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
interval = 0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time
moveUp = False
moveDown = False
moveLeft = False
moveRight = False

try:
    print 'Press [ESC] to quit'
    # Loop indefinitely
    leftState = GPIO.LOW
    rightState = GPIO.LOW
    while True:
        # Get the currently pressed keys on the keyboard
        events = pygame.event.get()
        for event in events:
            # Keys have changed, generate the command list based on keys
            if event.type == pygame.JOYBUTTONDOWN:
				if j.get_button(0):
					print("Pressed: X")
				elif j.get_button(1):
					print("Pressed: Circle")
				elif j.get_button(2):
					print("Pressed: Triangle")
				elif j.get_button(3):
					print("Pressed: Square")
				elif j.get_button(4):
					print("Pressed: L1")
				elif j.get_button(5):
					print("Pressed: R1")
				elif j.get_button(6):
					print("Pressed: L2")
				elif j.get_button(7):
					print("Pressed: R2")
                elif j.get_button(8):
					print("Pressed: SHARE")
                elif j.get_button(9):
					print("Pressed: OPTIONS")
                elif j.get_button(10):
					print("Pressed: PS Button")
                elif j.get_button(11):
					print("Pressed: Left Analog")
                elif j.get_button(12):
					print("Pressed: Right Analog")
            elif event.type == pygame.JOYBUTTONUP:
                if j.get_button(0):
					print("Released: X")
				elif j.get_button(1):
					print("Released: Circle")
				elif j.get_button(2):
					print("Released: Triangle")
				elif j.get_button(3):
					print("Released: Square")
				elif j.get_button(4):
					print("Released: L1")
				elif j.get_button(5):
					print("Released: R1")
				elif j.get_button(6):
					print("Released: L2")
				elif j.get_button(7):
					print("Released: R2")
                elif j.get_button(8):
					print("Released: SHARE")
                elif j.get_button(9):
					print("Released: OPTIONS")
                elif j.get_button(10):
					print("Released: PS Button")
                elif j.get_button(11):
					print("Released: Left Analog")
                elif j.get_button(12):
					print("Released: Right Analog")
            elif event.type == pygame.JOYAXISMOTION:
                    moveUp = False
                    moveDown = False
                    moveRight = False
                    moveLeft = False

					# A joystick has been moved, read axis positions (-1 to +1)
					upDown = j.get_axis(axisUpDown)
					leftRight = j.get_axis(axisLeftRight)

					# Invert any axes which are incorrect
					if axisUpDownInverted:
						upDown = -upDown
					if axisLeftRightInverted:
						leftRight = -leftRight

					# Determine Up / Down values
					if upDown < -0.1:
						moveUp = True
						moveDown = False
					elif upDown > 0.1:
						moveUp = False
						moveDown = True
					else:
						moveUp = False
						moveDown = False

					# Determine Left / Right values
					if leftRight < -0.1:
						moveLeft = True
						moveRight = False
					elif leftRight > 0.1:
						moveLeft = False
						moveRight = True
					else:
						moveLeft = False
						moveRight = False

					if moveLeft:
						leftState = GPIO.LOW
						rightState = GPIO.HIGH
					elif moveRight:
						leftState = GPIO.HIGH
						rightState = GPIO.LOW
					elif moveUp:
						leftState = GPIO.HIGH
						rightState = GPIO.HIGH
					else:
						leftState = GPIO.LOW
						rightState = GPIO.LOW

					GPIO.output(DRIVE_1, leftState)
					GPIO.output(DRIVE_4, rightState)

        # Wait for the interval period
        # time.sleep(0.1)
    # Disable all drives
except KeyboardInterrupt:
    # CTRL+C exit, disable all drives
    print("EXITING NOW")
    j.quit()

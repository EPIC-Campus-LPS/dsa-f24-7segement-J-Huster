#Importing modules and classes
import tm1637
import time
import numpy as np
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Creating 4-digit 7-segment diplay object
#Using GPIO pins, 18 for clk and 23 for dio
tm = tm1637.TM1637(clk=18, dio=23)
tm.brightness(7)
#Defining values as zeros to clear display
clear = [0, 0, 0, 0]
#Setup the s pin as output for the button
BUTTON_PIN = 17
#Setup the GPIO pins for the program
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, GPIO.LOW)
#Clear display
tm.write(clear)

def start():
	#Assign the value 0000 to the variable digits sp the stopwatch can start at zero seconds
	digits = 0000
	#Clear the display
	tm.write(clear)
	#While loop runs only after the button has been [ressed
	while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
		#Turns on the LED
		GPIO.output(19, GPIO.HIGH)
		#Adjust the digits variable so it's one number higher and making the stopwatch go up one second
		digits += 1
		#Display the digits varuable acroos the screen
		tm.show(str(digits))
		#pause the program for one second
		time.sleep(1)
		#Conditional statement only runs when the button is pressed a second time, pauses the stopwatch
		if GPIO.input(BUTTON_PIN) == GPIO.LOW:
			time.sleep(2)
			pass
#Creates variable so that program will run until the button is pressed
n = 1
#Whiel loop only runs why the variable above hasn't changed
while n == 1:
	#If statement only runs when the button is pressed
	if GPIO.input(BUTTON_PIN) == GPIO.LOW:
		#Begins the stopwatch
		start()

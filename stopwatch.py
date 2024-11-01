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
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, GPIO.LOW)
#Clear display
tm.write(clear)

def start():
	digits = 0000
	tm.write(clear)
	while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
		GPIO.output(19, GPIO.HIGH)
		digits += 1
		tm.show(str(digits))
		time.sleep(1)
		if GPIO.input(BUTTON_PIN) == GPIO.LOW:
			time.sleep(2)
			pass
			
n = 1
while n == 1:
	if GPIO.input(BUTTON_PIN) == GPIO.LOW:
		start()
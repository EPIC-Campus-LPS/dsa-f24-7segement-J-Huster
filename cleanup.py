import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

x = 1
y = 1

while x < 40:
	GPIO.setup(x,GPIO.OUT)
	GPIO.output(x,GPIO.HIGH)
	print("Working, LED on")
	x += 1

time.sleep(5)

while y < 40:
	GPIO.output(y,GPIO.LOW)
	print("Cleanup, LED off")
	y += 1
print("Done")

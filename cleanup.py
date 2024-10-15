import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

y = 1

while y < 40:
	GPIO.setup(y, GPIO.OUT)
	GPIO.output(y,GPIO.LOW)
	print("Cleanup, LED off")
	y += 1

print("Done")

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RED = 21
BLUE = 16
GREEN = 24

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

def reset_light():
	GPIO.output(RED, False)
	GPIO.output(BLUE, False)
	GPIO.output(GREEN, False)


reset_light()

GPIO.cleanup()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	input_value = GPIO.input(5)
	input_value2 = GPIO.input(20)

	if (input_value == False):
		print("Button1 Pressed!")

	if (input_value2 == False):
		print("Button2 Pressed!")

	time.sleep(0.3)

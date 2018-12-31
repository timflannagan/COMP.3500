import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PUSH = 20
LED = 16

GPIO.setup(PUSH, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

LED_state = False

while True:
	new_input = GPIO.input(PUSH)

	if (new_input == False):
		LED_state = not LED_state
		GPIO.output(LED, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(LED, GPIO.LOW)
	time.sleep(0.5)

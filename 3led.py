import RPi.GPIO as GPIO
from time import sleep

RED = 21
BLUE = 16
GREEN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

count = 0

try:
    while (count < 3):
        GPIO.output(RED, 1)
        GPIO.output(BLUE, 1)
        GPIO.output(GREEN, 1)
        sleep(1)
        GPIO.output(RED, 0)
        GPIO.output(BLUE, 0)
        GPIO.output(GREEN, 0)
        sleep(1)
        count += 1
    
except KeyboardInterrupt:
    GPIO.cleanup()
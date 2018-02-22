import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)

count = 0;

try:
    while True:
        if ((count & 3) == 0):
            GPIO.output(21, False)
            GPIO.output(16, False)
            GPIO.output(24, False)
            
        if ((count & 3) == 1):
            GPIO.output(21, True)
            GPIO.output(16, False)
            GPIO.output(24, False)
            
        if ((count & 3) == 2):
            GPIO.output(21, True)
            GPIO.output(16, True)
            GPIO.output(24, False)
            
        if ((count & 3) == 3):
            GPIO.output(21, True)
            GPIO.output(16, True)
            GPIO.output(24, True)
            
        if (GPIO.input(5) == GPIO.HIGH):
            count = 0

        if (GPIO.input(20) == GPIO.HIGH):
            print("I'm being pressed!\n")
            count += 1       
        
        sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    
